#!/usr/bin/env python3
"""Parse Claude data exports into staging format for wiki ingestion."""

import json
import os
import re
import sys

RAW_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'claude-20260415')
STAGING_DIR = os.path.join(os.path.dirname(__file__), '..', 'raw', 'staging', 'claude')

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
    """Split conversations.json into individual files, filtering short ones."""
    convs_path = os.path.join(RAW_DIR, 'conversations.json')
    if not os.path.exists(convs_path):
        print(f"conversations.json not found: {convs_path}")
        return []

    print("Loading conversations.json (this may take a moment for 309MB)...")
    with open(convs_path) as f:
        conversations = json.load(f)

    out_dir = os.path.join(STAGING_DIR, 'conversations')
    os.makedirs(out_dir, exist_ok=True)

    manifest_entries = []
    skipped = 0

    for conv in conversations:
        messages = conv.get('chat_messages', [])
        if len(messages) < MIN_MESSAGES:
            skipped += 1
            continue

        uuid = conv.get('uuid', 'unknown')
        name = conv.get('name', '') or 'Unnamed'
        created = conv.get('created_at', '')
        updated = conv.get('updated_at', '')
        summary = conv.get('summary', '')

        # Extract text from messages
        text_parts = []
        for msg in messages:
            sender = msg.get('sender', 'unknown')
            text = msg.get('text', '')
            if not text:
                # Try content field as fallback
                content = msg.get('content', [])
                if isinstance(content, list):
                    text = ' '.join(
                        c.get('text', '') for c in content
                        if isinstance(c, dict) and c.get('text')
                    )
                elif isinstance(content, str):
                    text = content
            if text:
                text_parts.append(f"[{sender}]: {text}")

        full_text = '\n\n'.join(text_parts)
        total_chars = len(full_text)

        result = {
            'id': f'claude-conv-{uuid}',
            'origin': 'claude',
            'type': 'conversation',
            'title': name,
            'created': created,
            'updated': updated,
            'summary': summary,
            'message_count': len(messages),
            'content': full_text,
            'content_chars': total_chars
        }

        output_path = os.path.join(out_dir, f'{uuid}.json')
        with open(output_path, 'w') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

        manifest_entries.append({
            'id': result['id'],
            'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
            'status': 'pending',
            'priority': 3,
            'origin': 'claude',
            'title': name,
            'message_count': len(messages),
            'content_chars': total_chars,
            'created': created
        })

    # Sort by message count descending (longest first = most developed thinking)
    manifest_entries.sort(key=lambda x: x['message_count'], reverse=True)

    print(f"Conversations: {len(manifest_entries)} staged, {skipped} skipped (<{MIN_MESSAGES} messages)")
    return manifest_entries


def parse_memories():
    """Parse memories.json — pre-distilled knowledge."""
    mem_path = os.path.join(RAW_DIR, 'memories.json')
    if not os.path.exists(mem_path):
        print("memories.json not found")
        return []

    with open(mem_path) as f:
        data = json.load(f)

    # memories.json is a list with one item containing conversations_memory, project_memories, account_uuid
    item = data[0] if isinstance(data, list) and data else data

    result = {
        'id': 'claude-memories',
        'origin': 'claude',
        'type': 'memories',
        'title': 'Claude Memories — Pre-distilled Knowledge',
        'conversations_memory': item.get('conversations_memory', ''),
        'project_memories': {},
        'content_chars': 0
    }

    # Parse project memories
    project_mems = item.get('project_memories', {})
    if isinstance(project_mems, dict):
        for proj_id, proj_data in project_mems.items():
            if isinstance(proj_data, str):
                result['project_memories'][proj_id] = proj_data
            elif isinstance(proj_data, dict):
                result['project_memories'][proj_id] = json.dumps(proj_data)

    result['content_chars'] = len(result['conversations_memory']) + sum(
        len(v) for v in result['project_memories'].values()
    )

    out_dir = os.path.join(STAGING_DIR, 'memories')
    os.makedirs(out_dir, exist_ok=True)
    output_path = os.path.join(out_dir, 'memories.json')
    with open(output_path, 'w') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"Memories: {len(result['conversations_memory']):,} chars global, "
          f"{len(result['project_memories'])} project memories")

    return [{
        'id': result['id'],
        'path': os.path.relpath(output_path, os.path.join(os.path.dirname(__file__), '..')),
        'status': 'pending',
        'priority': 2,
        'origin': 'claude',
        'title': result['title'],
        'content_chars': result['content_chars']
    }]


def parse_projects():
    """Parse projects.json into individual project files."""
    proj_path = os.path.join(RAW_DIR, 'projects.json')
    if not os.path.exists(proj_path):
        print("projects.json not found")
        return []

    with open(proj_path) as f:
        projects = json.load(f)

    out_dir = os.path.join(STAGING_DIR, 'projects')
    os.makedirs(out_dir, exist_ok=True)

    manifest_entries = []
    for proj in projects:
        if isinstance(proj, dict):
            name = proj.get('name', '') or 'Unnamed'
            uuid = proj.get('uuid', slugify(name))
            description = proj.get('description', '')
            prompt_template = proj.get('prompt_template', '')
            docs = proj.get('docs', [])

            # Combine all text content
            content_parts = []
            if description:
                content_parts.append(f"## Description\n{description}")
            if prompt_template:
                content_parts.append(f"## Prompt Template\n{prompt_template}")
            for doc in docs:
                if isinstance(doc, dict):
                    doc_name = doc.get('filename', doc.get('name', 'doc'))
                    doc_content = doc.get('content', '')
                    if doc_content:
                        content_parts.append(f"## Document: {doc_name}\n{doc_content}")

            full_content = '\n\n'.join(content_parts)
            if not full_content.strip():
                continue

            result = {
                'id': f'claude-project-{uuid}',
                'origin': 'claude',
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
                'priority': 3,
                'origin': 'claude',
                'title': name,
                'content_chars': len(full_content)
            })

    print(f"Projects: {len(manifest_entries)} staged")
    return manifest_entries


def main():
    os.makedirs(STAGING_DIR, exist_ok=True)

    all_entries = []
    all_entries.extend(parse_memories())
    all_entries.extend(parse_projects())
    all_entries.extend(parse_conversations())

    print(f"\nDone. Total Claude sources staged: {len(all_entries)}")
    return all_entries


if __name__ == '__main__':
    entries = main()
    total_chars = sum(e.get('content_chars', 0) for e in entries)
    print(f"Total content: {total_chars:,} chars")
