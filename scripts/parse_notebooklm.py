#!/usr/bin/env python3
"""Parse NotebookLM exports into staging format for wiki ingestion."""

import json
import os
import re
import glob
import sys

try:
    import html2text
    H2T = html2text.HTML2Text()
    H2T.ignore_links = False
    H2T.ignore_images = True
    H2T.body_width = 0
except ImportError:
    print("html2text not installed. Run: pip install html2text")
    sys.exit(1)

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'NotebookLM-20260415')
STAGING_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'staging', 'notebooklm')


def slugify(title):
    slug = title.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def parse_notebook(notebook_dir):
    """Parse a single NotebookLM notebook directory."""
    notebook_name = os.path.basename(notebook_dir)

    # Read metadata
    meta_path = os.path.join(notebook_dir, f'{notebook_name} metadata.json')
    metadata = {}
    if os.path.exists(meta_path):
        with open(meta_path) as f:
            metadata = json.load(f)

    result = {
        'id': f'notebooklm-{slugify(notebook_name)}',
        'origin': 'notebooklm',
        'title': metadata.get('title', notebook_name),
        'emoji': metadata.get('emoji', ''),
        'created': metadata.get('metadata', {}).get('createTime', ''),
        'last_viewed': metadata.get('metadata', {}).get('lastViewed', ''),
        'sources': [],
        'artifacts': [],
        'notes': [],
        'skipped_media': []
    }

    # Parse Sources (HTML files with companion metadata JSONs)
    sources_dir = os.path.join(notebook_dir, 'Sources')
    if os.path.exists(sources_dir):
        html_files = glob.glob(os.path.join(sources_dir, '*.html'))
        for html_path in html_files:
            basename = os.path.splitext(os.path.basename(html_path))[0]

            # Read HTML and convert to markdown
            with open(html_path, encoding='utf-8', errors='replace') as f:
                html_content = f.read()
            md_content = H2T.handle(html_content).strip()

            # Look for companion metadata JSON
            source_meta = {}
            for json_candidate in glob.glob(os.path.join(sources_dir, '*.json')):
                json_basename = os.path.splitext(os.path.basename(json_candidate))[0]
                # Metadata files often have truncated names matching the HTML
                if json_basename.startswith(basename[:30]) or basename.startswith(json_basename[:30]):
                    with open(json_candidate) as f:
                        source_meta = json.load(f)
                    break

            result['sources'].append({
                'title': source_meta.get('title', basename),
                'content_type': source_meta.get('metadata', {}).get('originalSourceContentType', 'unknown'),
                'date_added': source_meta.get('metadata', {}).get('sourceAddedTimestamp', ''),
                'content': md_content
            })

    # Parse Artifacts (markdown files, skip WAV/audio)
    artifacts_dir = os.path.join(notebook_dir, 'Artifacts')
    if os.path.exists(artifacts_dir):
        for artifact_file in os.listdir(artifacts_dir):
            artifact_path = os.path.join(artifacts_dir, artifact_file)

            if artifact_file.endswith('.wav') or artifact_file.endswith('.mp4') or artifact_file.endswith('.mp3'):
                result['skipped_media'].append(artifact_file)
                continue

            if artifact_file.endswith('.json'):
                # Artifact metadata - read for context
                with open(artifact_path) as f:
                    art_meta = json.load(f)
                art_type = art_meta.get('type', 'unknown')
                if art_type == 'ARTIFACT_TYPE_AUDIO_OVERVIEW':
                    continue  # Skip audio overview metadata
                # Other artifact metadata is informational, skip for now
                continue

            if artifact_file.endswith('.md'):
                with open(artifact_path, encoding='utf-8', errors='replace') as f:
                    content = f.read().strip()
                result['artifacts'].append({
                    'title': os.path.splitext(artifact_file)[0],
                    'format': 'markdown',
                    'content': content
                })
            elif artifact_file.endswith('.html'):
                with open(artifact_path, encoding='utf-8', errors='replace') as f:
                    html_content = f.read()
                md_content = H2T.handle(html_content).strip()
                result['artifacts'].append({
                    'title': os.path.splitext(artifact_file)[0],
                    'format': 'html_converted',
                    'content': md_content
                })

    # Parse Notes
    notes_dir = os.path.join(notebook_dir, 'Notes')
    if os.path.exists(notes_dir):
        for note_file in os.listdir(notes_dir):
            note_path = os.path.join(notes_dir, note_file)
            if note_file.endswith('.html'):
                with open(note_path, encoding='utf-8', errors='replace') as f:
                    html_content = f.read()
                md_content = H2T.handle(html_content).strip()
                result['notes'].append({
                    'title': os.path.splitext(note_file)[0],
                    'content': md_content
                })
            elif note_file.endswith('.md'):
                with open(note_path, encoding='utf-8', errors='replace') as f:
                    content = f.read().strip()
                result['notes'].append({
                    'title': os.path.splitext(note_file)[0],
                    'content': content
                })

    return result


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)

    raw_dir = os.path.abspath(RAW_DIR)
    if not os.path.exists(raw_dir):
        print(f"NotebookLM raw directory not found: {raw_dir}")
        sys.exit(1)

    notebooks = [d for d in os.listdir(raw_dir)
                 if os.path.isdir(os.path.join(raw_dir, d))]

    manifest_entries = []
    for notebook_name in sorted(notebooks):
        notebook_dir = os.path.join(raw_dir, notebook_name)
        print(f"Parsing: {notebook_name}")

        result = parse_notebook(notebook_dir)

        # Calculate content size for prioritization
        total_content = sum(len(s.get('content', '')) for s in result['sources'])
        total_content += sum(len(a.get('content', '')) for a in result['artifacts'])
        total_content += sum(len(n.get('content', '')) for n in result['notes'])

        slug = slugify(notebook_name)
        output_path = os.path.join(STAGING_DIR, f'{slug}.json')
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        manifest_entries.append({
            'id': result['id'],
            'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
            'status': 'pending',
            'priority': 1,
            'origin': 'notebooklm',
            'title': result['title'],
            'sources_count': len(result['sources']),
            'artifacts_count': len(result['artifacts']),
            'notes_count': len(result['notes']),
            'content_chars': total_content,
            'skipped_media': len(result['skipped_media'])
        })

        print(f"  -> {slug}.json ({len(result['sources'])} sources, "
              f"{len(result['artifacts'])} artifacts, {len(result['notes'])} notes, "
              f"{total_content:,} chars)")

    print(f"\nDone. Parsed {len(manifest_entries)} notebooks to {STAGING_DIR}")
    return manifest_entries


if __name__ == '__main__':
    entries = main()
    # Print summary
    total_chars = sum(e['content_chars'] for e in entries)
    print(f"Total content: {total_chars:,} chars across {len(entries)} notebooks")
