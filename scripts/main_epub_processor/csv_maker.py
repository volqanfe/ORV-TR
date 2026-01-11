import os
import re
import json
import pickle
import re

lines = []
linesBackup1 = []
data = []
csv = []
csv2 = []
validChars = "abcdefghijklmnopqrstuvwxyz 0123456789'"

data: dict = pickle.loads(open("temp.pkl", "rb").read())["data"]


for file in os.listdir("formatted"):
    if not file.endswith("txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        chap = f.readlines()
        for line in chap:
            if line.startswith("<system>["):
                line = line.replace("<system>[", "").replace("]", "").replace("\n", "")
                lines.append(line)

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

linesBackup2 = lines.copy()

for i in range(200):
    index = data[-i]["index"][0]
    line = lines[index]
    if re.search(r"BLANK", line):
        csv2.append(f"{line}, true\n")
    else:
        csv.append(f"{line}, false\n")

csv.extend(csv2)

with open("temp.csv", "w", encoding="utf-8") as f:
    f.write("".join(csv))
