import os.path
import sys

original_path = sys.argv[1]

originals = list(filter(lambda x: len(x) > 0, original_path.split(";")))
standards = list(map(os.path.realpath, originals))

# Gpg4win's path is a special case 'c:\program files (x86)\gpg4win\..\gnupg\bin'
special = "\\..\\"
for i, line in enumerate(originals):
    lowercase = line.lower()
    if special in lowercase:
        part1 = os.path.realpath(lowercase.split(special)[0])
        prefix = part1.rsplit("\\", maxsplit=1)[0] + "\\"
        part2 = os.path.realpath(lowercase).removeprefix(prefix)
        standards[i] = part1 + special + part2

dedup = list()
for line in standards:
    if line not in dedup:
        dedup.append(line)
        print(line)
