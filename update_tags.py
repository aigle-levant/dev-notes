import os
import re
import yaml
from collections import defaultdict

NOTES_DIR = 'Documentation'
TAGS_DIR = 'tags'
README_FILE = 'README.md'

def extract_tags(file_path):
    with open(file_path, 'r') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        metadata = yaml.safe_load(match.group(1))
        return metadata.get('tags', [])
    return []

def main():
    tag_map = defaultdict(list)

    # Ensure tags directory exists
    os.makedirs(TAGS_DIR, exist_ok=True)

    # Process notes
    for filename in os.listdir(NOTES_DIR):
        if filename.endswith('.md'):
            filepath = os.path.join(NOTES_DIR, filename)
            tags = extract_tags(filepath)
            for tag in tags:
                tag_map[tag].append(filename)

    # Update tag files
    for tag, files in tag_map.items():
        with open(os.path.join(TAGS_DIR, f'{tag}.md'), 'w') as f:
            f.write(f'# Notes Tagged with "{tag}"\n\n')
            for file in files:
                f.write(f'- [{file[:-3]}](../{NOTES_DIR}/{file})\n')

    # Update README.md
    with open(README_FILE, 'r') as f:
        content = f.read()

    tag_index = '## 🏷️ Tag Index\n\n| Tag | Count |\n|-----|-------|\n'
    for tag, files in tag_map.items():
        tag_index += f'| [{tag}]({TAGS_DIR}/{tag}.md) | {len(files)} |\n'

    # Replace existing tag index or append
    if '## 🏷️ Tag Index' in content:
        content = re.sub(r'## 🏷️ Tag Index.*?(?=\n## |\Z)', tag_index, content, flags=re.DOTALL)
    else:
        content += '\n\n' + tag_index

    with open(README_FILE, 'w') as f:
        f.write(content)

if __name__ == '__main__':
    main()
