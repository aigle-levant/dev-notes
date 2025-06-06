import os
import re
import yaml
from collections import defaultdict

# Define directories
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
TAGS_DIR = os.path.join(ROOT_DIR, 'tags')
README_FILE = os.path.join(ROOT_DIR, 'README.md')

# Initialize tag mapping
tag_map = defaultdict(list)

def extract_frontmatter(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return {}
    return {}

# Traverse directories and extract tags
for dirpath, _, filenames in os.walk(ROOT_DIR):
    # Skip the tags directory itself
    if TAGS_DIR in dirpath:
        continue
    for filename in filenames:
        if filename.endswith('.md'):
            filepath = os.path.join(dirpath, filename)
            rel_path = os.path.relpath(filepath, ROOT_DIR)
            metadata = extract_frontmatter(filepath)
            tags = metadata.get('tags', [])
            title = metadata.get('title', os.path.splitext(filename)[0])
            description = metadata.get('description', '')
            for tag in tags:
                tag_map[tag].append({
                    'title': title,
                    'description': description,
                    'path': rel_path.replace('\\', '/')
                })

# Create tags directory if it doesn't exist
os.makedirs(TAGS_DIR, exist_ok=True)

# Generate tag files
for tag, notes in tag_map.items():
    tag_filename = os.path.join(TAGS_DIR, f"{tag}.md")
    with open(tag_filename, 'w', encoding='utf-8') as f:
        f.write(f"# 🏷️ {tag.capitalize()} Notes\n\n")
        f.write("| Title | Description |\n")
        f.write("|-------|-------------|\n")
        for note in notes:
            f.write(f"| [{note['title']}]({note['path']}) | {note['description']} |\n")

# Update README.md with tag index
tag_index = "## 🏷️ Tag Index\n\n| Tag | Count |\n|-----|-------|\n"
for tag, notes in sorted(tag_map.items()):
    tag_index += f"| [{tag}](tags/{tag}.md) | {len(notes)} |\n"

# Read existing README.md content
if os.path.exists(README_FILE):
    with open(README_FILE, 'r', encoding='utf-8') as f:
        readme_content = f.read()
else:
    readme_content = ""

# Replace or append tag index
if "## 🏷️ Tag Index" in readme_content:
    readme_content = re.sub(r"## 🏷️ Tag Index.*?(?=\n## |\Z)", tag_index, readme_content, flags=re.DOTALL)
else:
    readme_content += "\n\n" + tag_index

# Write updated README.md
with open(README_FILE, 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ Tag files and README.md have been updated.")
