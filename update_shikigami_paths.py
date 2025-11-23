
import re

file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Helper to replace value in a block
def update_paths(match):
    block = match.group(0)
    # Extract ID
    id_match = re.search(r'id:\s*"(.*?)"', block) or re.search(r'"id":\s*"(.*?)"', block)
    if not id_match:
        return block
    
    shiki_id = id_match.group(1)
    
    # Define new paths
    new_icon = f'/images/shikigami/{shiki_id}/icon.png'
    new_image = f'/images/shikigami/{shiki_id}/full.png'
    
    # Replace icon
    # Matches icon: "..." or "icon": "..."
    block = re.sub(r'(icon"?:\s*)"(.*?)"', f'\\1"{new_icon}"', block)
    
    # Replace image
    block = re.sub(r'(image"?:\s*)"(.*?)"', f'\\1"{new_image}"', block)
    
    return block

# Regex to find each shikigami object
# We assume they start with { and end with }, inside the array.
# This is tricky with regex.
# But we can iterate over the file line by line or use the fact that we just regenerated it and it has a consistent structure.
# Or we can just use a regex that matches `id: "...", ... icon: "...", image: "..."` if they are close.

# Better approach:
# The file structure is:
# {
#    id: "...",
#    ...
#    icon: "...",
#    image: "...",
#    ...
# }

# We can just replace all `icon: "..."` lines if we know the ID from context.
# But regex replacement with a callback is best.

# Pattern:
# Look for `id: "..."` then capture until `image: "..."`
# This is hard because `icon` and `image` might be far from `id`.

# Let's try a line-by-line state machine approach, similar to the deduplication but for modification.

lines = content.split('\n')
new_lines = []
current_id = None

for line in lines:
    # Check for ID
    id_match = re.search(r'^\s*"?id"?: "(.*?)",', line)
    if id_match:
        current_id = id_match.group(1)
        new_lines.append(line)
        continue
        
    # Check for icon
    if current_id and ('icon:' in line or '"icon":' in line):
        # Replace value
        # Preserve indentation and key
        prefix = line.split(':')[0]
        new_lines.append(f'{prefix}: "/images/shikigami/{current_id}/icon.png",')
        continue

    # Check for image
    if current_id and ('image:' in line or '"image":' in line):
        prefix = line.split(':')[0]
        new_lines.append(f'{prefix}: "/images/shikigami/{current_id}/full.png",')
        continue
        
    new_lines.append(line)

new_content = '\n'.join(new_lines)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("Updated image paths for all Shikigami.")
