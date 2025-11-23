
import re

file_path = r"C:\Users\CHUTIMAN.C\Desktop\onmyojiTH\onmyoji-db\src\lib\data\shikigami.ts"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

ids = re.findall(r'id:\s*"(.*?)"', content)
ids += re.findall(r'"id":\s*"(.*?)"', content)

seen = set()
duplicates = []
for i in ids:
    if i in seen:
        duplicates.append(i)
    seen.add(i)

if duplicates:
    print(f"Found duplicates: {duplicates}")
else:
    print("No duplicates found.")
