#!/usr/bin/env python3
"""Parse Grok data exports into staging format for wiki ingestion."""

import json
import os
import re
import sys

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'grok-20260415')
STAGING_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'staging', 'grok')

MIN_MESSAGES = 4


def slugify(text):
    if not text:
        return 'unnamed'
    slug = text.lower().strip()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[\s_]+', '-', slug)
    slug = re.sub(r'-+', '-', slug)
    return slug.strip('-')[:80]


def parse_conversations():
    """Parse Grok conversations from prod-grok-backend.json."""
    backend_path = os.path.join(RAW_DIR, 'prod-grok-backend.json')
    if not os.path.exists(backend_path):
        print(f"prod-grok-backend.json not found: {backend_path}")
        return []

    print("Loading prod-grok-backend.json...")
    with open(backend_path) as f:
        data = json.load(f)

    conversations = data.get('conversations', [])
    out_dir = os.path.join(STAGING_DIR, 'conversations')
    os.makedirs(out_dir, exist_ok=True)

    manifest_entries = []
    skipped = 0

    for conv_item in conversations:
        conv_meta = conv_item.get('conversation', {})
        responses = conv_item.get('responses', [])

        if len(responses) < MIN_MESSAGES:
            skipped += 1
            continue

        conv_id = conv_meta.get('id', 'unknown')
        title = conv_meta.get('title', '') or 'Unnamed'
        created = conv_meta.get('create_time', '')
        modified = conv_meta.get('modify_time', '')
        summary = conv_meta.get('summary', '')

        # Extract text from responses
        text_parts = []
        for resp_item in responses:
            resp = resp_item.get('response', {})
            sender = resp.get('sender', 'unknown')
            message = resp.get('message', '')
            if message:
                # Normalize sender names
                sender_label = 'human' if sender.lower() == 'human' else 'assistant'
                text_parts.append(f"[{sender_label}]: {message}")

        full_text = '\n\n'.join(text_parts)
        total_chars = len(full_text)

        result = {
            'id': f'grok-conv-{conv_id}',
            'origin': 'grok',
            'type': 'conversation',
            'title': title,
            'created': created,
            'modified': modified,
            'summary': summary,
            'message_count': len(responses),
            'content': full_text,
            'content_chars': total_chars
        }

        output_path = os.path.join(out_dir, f'{conv_id}.json')
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        manifest_entries.append({
            'id': result['id'],
            'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
            'status': 'pending',
            'priority': 4,
            'origin': 'grok',
            'title': title,
            'message_count': len(responses),
            'content_chars': total_chars,
            'created': created
        })

    # Sort by message count descending
    manifest_entries.sort(key=lambda x: x['message_count'], reverse=True)

    print(f"Conversations: {len(manifest_entries)} staged, {skipped} skipped (<{MIN_MESSAGES} messages)")
    return manifest_entries


def parse_projects():
    """Parse Grok projects."""
    backend_path = os.path.join(RAW_DIR, 'prod-grok-backend.json')
    with open(backend_path) as f:
        data = json.load(f)

    projects = data.get('projects', [])
    out_dir = os.path.join(STAGING_DIR, 'projects')
    os.makedirs(out_dir, exist_ok=True)

    manifest_entries = []
    for proj in projects:
        name = proj.get('name', '') or 'Unnamed'
        workspace_id = proj.get('workspace_id', slugify(name))
        personality = proj.get('custom_personality', '')
        starters = proj.get('conversation_starters', [])

        content_parts = []
        if personality:
            content_parts.append(f"## Custom Personality\n{personality}")
        if starters:
            content_parts.append(f"## Conversation Starters\n" +
                               '\n'.join(f"- {s}" for s in starters if s))

        full_content = '\n\n'.join(content_parts)
        if not full_content.strip():
            continue

        result = {
            'id': f'grok-project-{workspace_id}',
            'origin': 'grok',
            'type': 'project',
            'title': name,
            'content': full_content,
            'content_chars': len(full_content)
        }

        slug = slugify(name)
        output_path = os.path.join(out_dir, f'{slug}.json')
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        manifest_entries.append({
            'id': result['id'],
            'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
            'status': 'pending',
            'priority': 4,
            'origin': 'grok',
            'title': name,
            'content_chars': len(full_content)
        })

    print(f"Projects: {len(manifest_entries)} staged")
    return manifest_entries


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)

    all_entries = []
    all_entries.extend(parse_projects())
    all_entries.extend(parse_conversations())

    print(f"\nDone. Total Grok sources staged: {len(all_entries)}")
    return all_entries


if __name__ == '__main__':
    entries = main()
    total_chars = sum(e.get('content_chars', 0) for e in entries)
    print(f"Total content: {total_chars:,} chars")
