import os
import re
import json

lines = []

for file in os.listdir("formatted"):
    if not file.endswith("txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        chap = f.readlines()
        for line in chap:
            if line.startswith("<#>【"):
                lines.append(line.replace("<#>【", "").replace("】", ""))


print(len(lines))
print(len(lines))

collapsed_string = "".join(lines)

with open("./temp.txt", "w", encoding="utf-8") as f:
    f.write(collapsed_string)
