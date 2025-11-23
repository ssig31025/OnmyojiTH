
import os
import re

ts_file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"
base_image_dir = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\public\images\shikigami"

with open(ts_file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Extract IDs
# Matches id: "foo" or "id": "foo"
ids = re.findall(r'^\s*"?id"?: "(.*?)",', content, re.MULTILINE)

print(f"Found {len(ids)} Shikigami IDs.")

created_count = 0
for shiki_id in ids:
    folder_path = os.path.join(base_image_dir, shiki_id)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        created_count += 1
        # print(f"Created: {folder_path}")

print(f"Created {created_count} new folders in {base_image_dir}.")
