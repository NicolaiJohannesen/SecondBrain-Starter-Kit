# Deploying to Cloudflare — Pages and Workers, done correctly

The how-to for the kit's default deploy target ([building-software-projects.md](building-software-projects.md) explains *why* Cloudflare: unlimited-bandwidth free tier, git-push deploys, a full $0 stack until real scale). Verified against Cloudflare's own docs 2026-07; limits and UI paths drift — when a number matters, re-check [developers.cloudflare.com](https://developers.cloudflare.com/).

## Step 0 — Pages or Workers? (the 2026 answer)

Cloudflare now steers **new** projects toward **Workers with static assets** — one Worker can serve frontend + backend and gets the full feature set (Durable Objects, cron triggers, better observability). **Pages is not deprecated** (no sunset date anywhere in the docs) and remains the simplest choice for a pure static site.

- Blog / portfolio / docs / marketing page, no server logic → **Pages** (simplest git-push-to-deploy).
- Anything with functions, scheduled jobs, or storage → **Workers with static assets**.
- Good news for migrations: `_headers`/`_redirects`, custom domains, secrets, and KV/D1/R2 bindings all carry over; CLI changes from `wrangler pages deploy` → `wrangler deploy`. One reversal to know: on Workers, **static assets are served before your Worker code by default** (Pages ran Functions first) — middleware needs `run_worker_first` in config.

## Step 1 — Create the project

**Git integration (recommended)**: Dashboard → Workers & Pages → *Connect to Git* → pick the repo. Set the **build command** (blank for plain HTML), the **build output directory**, and — monorepos — the **root directory**. Two facts that prevent the most common failure: *build output directory is relative to root directory, not repo root* (root `apps/web` + output `apps/web/dist` → enter `dist`); and a project created via git integration **can't be switched to direct upload later** (you can disable auto-deploy and push with wrangler instead).

**Direct upload** (your own CI, or no repo): `npx wrangler pages deploy <dir> --project-name=<name>`.

From then on: every push to the production branch (default `main`) deploys live; **every other branch and every PR gets its own preview URL** (`<branch>.<project>.pages.dev`) — this is how you test at the deployed configuration before promoting, and promotion is just the git merge.

## Step 2 — wrangler essentials

```bash
npm install -g wrangler    # or npx wrangler per-invocation
wrangler login             # interactive OAuth; CI uses CLOUDFLARE_API_TOKEN env var instead
wrangler dev               # local dev (add --remote to hit real KV/D1 data — local emulation returns null for keys you never wrote locally)
wrangler deploy            # Workers; Pages: wrangler pages deploy <dir>
```

Config: `wrangler.jsonc` is now recommended over `.toml` for new projects (some newer features are JSON-only). Minimum keys: `name`, `main`, `compatibility_date`. **The gotcha that causes "works in dev, 500s in prod"**: `[env.x]` blocks do NOT inherit bindings or vars — every environment redeclares its KV/D1/R2/vars explicitly.

## Step 3 — Secrets and variables

- Plaintext config → `[vars]` in the config file. **Secrets never go in the config file** (it's committed): `wrangler secret put KEY` (Workers) or `wrangler pages secret put KEY --project-name=<name>`.
- Local dev secrets → a `.dev.vars` file next to the config (picked up by `wrangler dev`, never deployed) — gitignore it like a `.env` (see [external-tools-and-apis.md](external-tools-and-apis.md) for the full key-hygiene discipline).
- Production and preview environments can hold different values — set both, or preview deploys run against production credentials.

## Step 4 — Headers, redirects, SPA behavior

Two plain-text files at the build output root (they also work on Workers-with-static-assets):

```
# _redirects            <source> <destination> <status>; first match wins; 2,000 static + 100 dynamic max
/old-path  /new-path  301
/*         /index.html  200        # SPA fallback — 200 = rewrite, not redirect

# _headers              path pattern, then indented headers; 100 rules max
/*
  X-Frame-Options: DENY
/assets/*
  Cache-Control: public, max-age=31536000, immutable
```

Three gotchas: **redirects run before headers** (a matched redirect skips your header rules for that path) · **a matching Pages Function bypasses `_redirects` entirely** (replicate the redirect in the Function or exclude the route in `_routes.json`) · **no top-level `404.html` = automatic SPA fallback** — a feature for SPAs, a silent loss of your custom 404 for multi-page sites.

## Step 5 — Custom domain

- **Subdomain** (`app.example.com`): attach the domain in the Pages/Workers dashboard **first**, then CNAME at your DNS host to `<project>.pages.dev`. Order matters — a CNAME without the dashboard attachment returns error 522.
- **Apex** (`example.com`): the domain must be a zone on your Cloudflare account (nameservers at Cloudflare); Cloudflare handles the apex via CNAME flattening and creates the record for you. SSL is automatic in both cases.

## Migrating an existing Apache/.htaccess site (zero-downtime sequence)

1. Lower DNS TTLs to ~300s, 24–48h before cutover.
2. Translate `.htaccess` rule-by-rule: RewriteRules → `_redirects`; Header directives → `_headers`. Any rule overlapping a Function route must live in the Function.
3. Deploy and fully test on the `*.pages.dev` URL (the preview surface is the staging environment).
4. Attach the custom domain in the dashboard *before* touching DNS (the 522 rule).
5. Cut over by flipping the DNS record (bounded by your TTL — minutes), not by changing nameservers if avoidable (up to 48h propagation).
6. Keep the old origin alive for a rollback window before decommissioning.
7. **If the old site had a service worker**: browsers can keep serving the old cached app shell indefinitely regardless of your new deploy — ship version-named caches, a `no-cache` `/version` endpoint the app polls, or a one-time self-unregistering SW update. (Community-verified practice; Cloudflare's edge cache can't reach the browser's SW layer by design.)

## The mistakes list (what actually bites)

Build output directory wrong (the monorepo relative-path trap) · missing `index.html` at output root · a leftover "Cache Everything" page rule fighting Pages' own invalidation (fix: Purge Everything) · `wrangler login` in CI instead of `CLOUDFLARE_API_TOKEN` · the **500 builds/month** free-tier ceiling with bot-triggered rebuilds · the **25 MiB per-file limit** (big media belongs in R2) · a Function route silently eating your redirect · stale build cache (Settings → clear build cache).

## Free-tier numbers (as of 2026-07 — re-check before relying)

Pages: 500 builds/mo · 1 concurrent · 20-min timeout · 20k files · 25 MiB/file. Workers: 100k requests/day · 10ms CPU per invocation (CPU, not wall-clock — I/O wait doesn't count). KV: 100k reads / 1k writes per day, 1 GB. D1: 5M row-reads / 100k row-writes per day, 5 GB. R2: 10 GB stored, zero egress fees. Paid tier starts at $5/mo. Source: [Pages limits](https://developers.cloudflare.com/pages/platform/limits/) · [Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/).

## Related

- [building-software-projects.md](building-software-projects.md) — the build loop this deploy step belongs to (deploy only after the merge gate, verify at the live URL)
- [external-tools-and-apis.md](external-tools-and-apis.md) — key hygiene for the API token
- [[Intent-Driven Development]] — test at the deployed configuration; the preview URL is the deployed configuration
