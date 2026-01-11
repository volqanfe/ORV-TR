import re
import os
import urllib
import random
import urllib.parse
import csv

with open('./scripts/side/data.csv', 'r') as file:
    data = csv.DictReader(file)
    systemLines = []
    for i in data:
        if i["type"] == "true":
            systemLines.append(i["line"])

with open("scripts/side/newFiles.txt", "r", encoding="utf-8") as f:
    newFiles = f.read().split("\n")
    if newFiles[0] == "":
        exit(code=0)


images = []
counter = 0

for file in newFiles:
    if not file.endswith(".txt"):
        continue
    file_index = re.match(r"[0-9]+", file).group(0)
    
    with open(f"./chapters/cont/{file}", "r", encoding="utf-8") as f:
        textStr = f.read()
        text = textStr.split("\n")
    
    for index,line in enumerate(text):
        if line.startswith("<!>"):
            match = line.replace("<!>", "")
            match: str = match.lower()
            match = re.findall(r"[a-z0-9'<> ]?", match)
            match = "".join(match)
            match = re.sub(r"(\w)'(\w)", r"\1\2", match)
            match = re.sub(r"'.*?'", "BLANK", match)
            match = re.sub(r"[0-9]+", "0", match)
            match = re.sub(r"<.*?>", "NEBULA", match)
            match = match.replace("'", "")
            if not match in systemLines:
                counter += 1
                text[index] = line.replace("<!>", "<@>")
                

    with open(f"./chapters/cont/{file}", "w", encoding="utf-8") as f:
        f.write("\n".join(text))


print(counter)

