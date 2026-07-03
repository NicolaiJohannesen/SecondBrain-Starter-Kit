#!/usr/bin/env python3
"""Parse Google Keep exports into staging format for wiki ingestion.

Aggressive filtering: most Keep notes are trivial (todos, snippets, passwords).
Only Tier 1 notes (substantial content) are staged for wiki ingestion.
"""

import json
import os
import re
import glob
import sys

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'Keep-20260415')
STAGING_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'staging', 'keep')

# Minimum characters for a note to be considered
MIN_CHARS = 100

# Tier 1 threshold: notes with substantial content
TIER1_MIN_CHARS = 500

# Sensitive patterns to exclude entirely
SENSITIVE_PATTERNS = re.compile(
    r'(?i)(password|passcode|adgangskode|kodeord|pin\s*code|pin\s*kode|'
    r'swift\s*code|iban|cvv|cvc|secret\s*key|api[_\s]*key|'
    r'access[_\s]*token|private[_\s]*key|login\s*credentials|'
    r'sk-[a-zA-Z0-9]{20,}|ghp_[a-zA-Z0-9]{20,}|xoxb-)',
    re.IGNORECASE
)

# Sensitive title patterns
SENSITIVE_TITLE_PATTERNS = re.compile(
    r'(?i)(password|kode|login|credential|pin|swift|iban|secret)',
    re.IGNORECASE
)


def slugify(text):
    if not text:
        return 'unnamed'
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def is_sensitive(note):
    """Check if a note contains sensitive data."""
    title = note.get('title', '')
    content = note.get('textContent', '')

    if SENSITIVE_TITLE_PATTERNS.search(title):
        return True
    if SENSITIVE_PATTERNS.search(content):
        return True
    return False


def is_tier1(note):
    """Determine if a note is Tier 1 (wiki-worthy)."""
    content = note.get('textContent', '')
    labels = note.get('labels', [])
    annotations = note.get('annotations', [])

    char_count = len(content)

    # Tier 1: substantial content
    if char_count >= TIER1_MIN_CHARS:
        return True
    # Tier 1: has labels (user categorized it)
    if labels:
        return True
    # Tier 1: has multiple links (research note)
    if len(annotations) >= 2:
        return True

    return False


def parse_note(json_path):
    """Parse a single Keep JSON note."""
    with open(json_path, encoding='utf-8', errors='replace') as f:
        note = json.load(f)

    title = (note.get('title', '') or '').strip()
    content = (note.get('textContent', '') or '').strip()
    labels = [l.get('name', '') for l in note.get('labels', []) if isinstance(l, dict)]
    annotations = note.get('annotations', [])
    links = []
    for ann in annotations:
        if isinstance(ann, dict):
            url = ann.get('url', '')
            if url:
                links.append(url)

    # Timestamps are in microseconds
    created_usec = note.get('createdTimestampUsec', 0)
    edited_usec = note.get('userEditedTimestampUsec', 0)

    return {
        'title': title,
        'content': content,
        'labels': labels,
        'links': links,
        'is_pinned': note.get('isPinned', False),
        'is_archived': note.get('isArchived', False),
        'is_trashed': note.get('isTrashed', False),
        'color': note.get('color', ''),
        'created_usec': created_usec,
        'edited_usec': edited_usec,
        'content_chars': len(content)
    }


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)

    raw_dir = os.path.abspath(RAW_DIR)
    if not os.path.exists(raw_dir):
        print(f"Keep raw directory not found: {raw_dir}")
        sys.exit(1)

    json_files = sorted(glob.glob(os.path.join(raw_dir, '*.json')))
    print(f"Found {len(json_files)} Keep JSON files")

    manifest_entries = []
    stats = {
        'total': len(json_files),
        'trashed': 0,
        'too_short': 0,
        'sensitive': 0,
        'tier2_skipped': 0,
        'tier1_staged': 0,
        'errors': 0
    }

    for json_path in json_files:
        try:
            note = parse_note(json_path)
        except (json.JSONDecodeError, KeyError) as e:
            stats['errors'] += 1
            continue

        # Filter: trashed
        if note['is_trashed']:
            stats['trashed'] += 1
            continue

        # Filter: too short
        if note['content_chars'] < MIN_CHARS and not note['labels'] and not note['links']:
            stats['too_short'] += 1
            continue

        # Filter: sensitive
        if is_sensitive({'title': note['title'], 'textContent': note['content']}):
            stats['sensitive'] += 1
            continue

        # Filter: Tier 1 only
        if not is_tier1({'textContent': note['content'], 'labels': [{'name': l} for l in note['labels']], 'annotations': [{'url': u} for u in note['links']]}):
            stats['tier2_skipped'] += 1
            continue

        # Stage this note
        filename = os.path.splitext(os.path.basename(json_path))[0]
        slug = slugify(note['title'] or filename)

        result = {
            'id': f'keep-{slug}',
            'origin': 'keep',
            'type': 'note',
            'title': note['title'] or filename,
            'content': note['content'],
            'labels': note['labels'],
            'links': note['links'],
            'is_pinned': note['is_pinned'],
            'created_usec': note['created_usec'],
            'edited_usec': note['edited_usec'],
            'content_chars': note['content_chars']
        }

        output_path = os.path.join(STAGING_DIR, f'{slug}.json')
        # Handle slug collisions
        counter = 1
        while os.path.exists(output_path):
            output_path = os.path.join(STAGING_DIR, f'{slug}-{counter}.json')
            counter += 1

        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        manifest_entries.append({
            'id': result['id'],
            'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
            'status': 'pending',
            'priority': 5,
            'origin': 'keep',
            'title': result['title'],
            'content_chars': note['content_chars'],
            'labels': note['labels']
        })

        stats['tier1_staged'] += 1

    print(f"\nKeep parsing complete:")
    print(f"  Total files:    {stats['total']}")
    print(f"  Trashed:        {stats['trashed']}")
    print(f"  Too short:      {stats['too_short']}")
    print(f"  Sensitive:      {stats['sensitive']}")
    print(f"  Tier 2 skipped: {stats['tier2_skipped']}")
    print(f"  Tier 1 staged:  {stats['tier1_staged']}")
    print(f"  Errors:         {stats['errors']}")

    return manifest_entries


if __name__ == '__main__':
    entries = main()
    total_chars = sum(e.get('content_chars', 0) for e in entries)
    print(f"Total staged content: {total_chars:,} chars across {len(entries)} notes")
