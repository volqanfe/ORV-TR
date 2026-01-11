import os
import re
import json
import pickle

lines = []
linesBackup1 = []
data = []
validChars = "abcdefghijklmnopqrstuvwxyz 0123456789'"

for file in os.listdir("formatted"):
    if not file.endswith("txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        chap = f.readlines()
        for line in chap:
            if line.startswith("<!>["):
                line = line.replace("<!>[", "").replace("]", "").replace("\n", "")
                lines.append(line)

linesBackup1 = lines.copy()

print(len(lines))
print(len(list(set(lines))))

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
print(len(linesBackup2))

regexList = [
    {
        "line": r"^(the constellation|constellation)",
        "count": 0,
        "length": 100,
        "index": [],
    },
    {"line": r"(giant story |story )BLANK", "count": 0, "length": 100, "index": []},
    {"line": r"character BLANK", "count": 0, "length": 100, "index": []},
    {"line": r"points 0", "count": 0, "length": 100, "index": []},
    {"line": r"looking at you", "count": 0, "length": 100, "index": []},
    {"line": r"(is|has) activat", "count": 0, "length": 100, "index": []},
    {"line": r"0 coins", "count": 0, "length": 20, "index": []},
    {"line": r"NEBULA", "count": 0, "length": 20, "index": []},
    {"line": r"dokkaebi.*?BLANK+", "count": 0, "length": 20, "index": []},
    {"line": r"is shaking", "count": 0, "length": 20, "index": []},
    {"line": r"skill .*?", "count": 0, "length": 15, "index": []},
    {"line": r"scenario has arrived", "count": 0, "length": 15, "index": []},
    {"line": r"(acquired|audience|your story)", "count": 0, "length": 15, "index": []},
    {"line": r"(\bmember|>)", "count": 0, "length": 20, "index": []},
]
for index, line in enumerate(set(lines)):
    match = False
    for regex in regexList:
        if len(line.split()) > regex["length"]:
            continue
        if match:
            break
        if re.search(regex["line"], line):
            regex["count"] += 1

            match = True
            # for i in range(lines.count(line)):
            #     regex["index"].append(linesBackup2.index(line))
            #     lines.remove(line)
        # regex["index"] = sorted(regex["index"])


data.extend(regexList)
for line in set(lines):
    # indices = [i for i, x in enumerate(lines) if x == line]
    # indices = sorted(indices)

    count = lines.count(line)
    # if count <= 1: continue
    # data.append({"line": line, "count": count, "index": indices})
    data.append({"line": line, "count": count})

print(len(data))
data = sorted(data, key=lambda x: x["count"], reverse=True)

with open("./temp.json", "w", encoding="utf-8") as f:
    f.write(json.dumps(data, indent=4))

with open("./temp.txt", "w", encoding="utf-8") as f:
    chap = []
    lines = linesBackup2
    lines = list(set(lines))
    for index, line in enumerate(lines):
        if re.search(r"", line):
            if len(line.split()) <= 1000:
                chap.append(line)
    f.write("\n".join(chap))

with open("./lines.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(linesBackup2))

pickle.dump(
    {"lines": linesBackup1, "data": data, "linesProcessed": linesBackup2},
    open("./temp.pkl", "wb"),
)
