import os
import re
import json
import pickle
import csv

lines = []
linesBackup1 = []
data = []
validChars = "abcdefghijklmnopqrstuvwxyz 0123456789'"

with open("scripts/side/newFiles.txt", "r", encoding="utf-8") as f:
    newFiles = f.read().split("\n")
    if newFiles[0] == "":
        exit(code=0)

for file in newFiles:

    try:
        if not file.endswith("txt"):
            continue
        with open(f"./chapters/cont/{file}", "r", encoding="utf-8") as f:
            chap = f.readlines()
            for line in chap:
                if line.startswith("<!>["):
                    line = line.replace("<!>[", "").replace("]", "").replace("\n", "")
                    lines.append(line)
    except Exception as e:
        print(e)

linesBackup1 = lines.copy()


for index, line in enumerate(lines):
    match: str = line.lower()
    match = re.findall(r"[a-z0-9'<> ]?", match)
    match = "".join(match)
    match = re.sub(r"(\w)'(\w)", r"\1\2", match)
    match = re.sub(r"'.*?'", "BLANK", match)
    match = re.sub(r"[0-9]+", "0", match)
    match = re.sub(r"<.*?>", "NEBULA", match)
    match = match.replace("'", "")
    lines[index] = match

    print(match)

print(len(lines))
print(len(list(set(lines))))

csvData = csv.DictReader(open("scripts/side/data.csv", "r", encoding="utf-8"))

newLines = []
ParsedLines = []

for index,row in enumerate(csvData):
    ParsedLines.append(row["line"])

for line in set(lines):
    if not line in ParsedLines:
        newLines.append(line)

print(len(newLines))

with open ("scripts/side/lines.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(list(set(newLines))))

for line in list(set(newLines)):
    print(line)
