
import re

file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Extract the array content
start_marker = "export const shikigamiData: Shikigami[] = ["
end_marker = "];"

start_idx = content.find(start_marker)
end_idx = content.rfind(end_marker)

if start_idx == -1 or end_idx == -1:
    print("Could not find array boundaries.")
    exit()

header = content[:start_idx + len(start_marker)]
footer = content[end_idx:]
array_content = content[start_idx + len(start_marker):end_idx]

# 2. Split into object blocks
# Split by closing brace + optional comma + newline
# We use a lookahead or just split and clean up.
# Regex: newline, optional whitespace, closing brace, optional comma
# This consumes the closing brace.
raw_blocks = re.split(r'\n\s*},?', array_content)

unique_blocks = []
seen_ids = set()

# Regex to find ID within a block (multiline)
id_pattern = re.compile(r'^\s*"?id"?: "(.*)"', re.MULTILINE)

for block in raw_blocks:
    clean_block = block.strip()
    if not clean_block:
        continue
        
    # Remove leading comma if present (from previous split residue)
    if clean_block.startswith(','):
        clean_block = clean_block[1:].strip()
    
    # Ensure it starts with {
    if not clean_block.startswith('{'):
        first_brace = clean_block.find('{')
        if first_brace != -1:
            clean_block = clean_block[first_brace:]
        else:
            continue # Invalid block
            
    # Extract ID
    match = id_pattern.search(clean_block)
    if match:
        shiki_id = match.group(1)
        if shiki_id in seen_ids:
            continue # Skip duplicate
        seen_ids.add(shiki_id)
        
        # Fix indentation for the first line
        lines = clean_block.split('\n')
        # The first line is "{", needs 4 spaces.
        # The rest are likely indented by 8 spaces (relative to file) or 4 (relative to block).
        # We'll assume they are okay but ensure the first line is indented.
        formatted_block = "    " + lines[0]
        if len(lines) > 1:
             formatted_block += "\n" + "\n".join(lines[1:])
        
        unique_blocks.append(formatted_block)

# 3. Reconstruct
new_array_content = "\n"
for i, block in enumerate(unique_blocks):
    new_array_content += block
    # Add the closing brace (which was consumed by split)
    new_array_content += "\n    }"
    
    if i < len(unique_blocks) - 1:
        new_array_content += ",\n"
    else:
        new_array_content += "\n"

final_content = header + new_array_content + footer

with open(file_path, "w", encoding="utf-8") as f:
    f.write(final_content)

print(f"Deduplicated. Total unique items: {len(seen_ids)}")
