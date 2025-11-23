
import re

file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find all occurrences of lantern-boy id
matches = list(re.finditer(r'id:\s*"lantern-boy"', content))

if len(matches) > 1:
    print(f"Found {len(matches)} occurrences of lantern-boy.")
    # We want to remove the second one.
    # The second one is likely the N rarity one (since SSN came first in the list).
    # Let's find the block for the second match.
    
    second_match_start = matches[1].start()
    
    # Find the start of the object (the { before the id)
    block_start = content.rfind('{', 0, second_match_start)
    
    # Find the end of the object (the }, after the id)
    # We need to be careful to match the correct closing brace.
    # Assuming standard formatting:
    #     {
    #         id: "lantern-boy",
    #         ...
    #     },
    
    block_end = content.find('},', second_match_start) + 2
    
    # Remove the block
    # We also need to remove the comma if it's not the last element, or the preceding comma if it is.
    # In the array, it looks like:
    # ...
    # },
    # {
    #    id: "lantern-boy",
    #    ...
    # },
    # {
    # ...
    
    # So removing from block_start to block_end should work, but might leave an extra comma or newline.
    # Let's see what's around it.
    
    print(f"Removing block from {block_start} to {block_end}")
    
    new_content = content[:block_start] + content[block_end:]
    
    # Clean up potential double commas or empty lines
    # If we have ",\n\n,", replace with ",\n"
    # But simpler: just write it back and let the user format it or just leave it valid JS.
    # The comma is usually after the }, so if we remove "{\n ... \n    }," we might leave a trailing comma from the previous item.
    # Wait, the list is comma separated.
    # item1,
    # item2,
    # item3
    
    # If we remove item2 (including the comma after it), we get:
    # item1,
    # item3
    
    # If the block includes the trailing comma (which my find('},') + 2 does), then we are good.
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("Removed duplicate Lantern Boy.")
else:
    print("Did not find duplicate Lantern Boy.")
