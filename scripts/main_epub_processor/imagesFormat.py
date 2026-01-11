import re
import os
import urllib
import random
import urllib.parse

images = []

for file_index,file in enumerate(os.listdir("./webpage/assets/images")):
    if not file.endswith(".jpg"):
        continue
    new_name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=10)) + ".jpg"
    os.rename(f"./webpage/assets/images/{file}", f"./webpage/assets/images/{new_name}")
    file = new_name
    images.append(file)


for file_index,file in enumerate(os.listdir("formatted")):
    if not file.endswith(".txt"):
        continue
    with open(f"./formatted/{file}", "r", encoding="utf-8") as f:
        textStr = f.read()
        text = textStr.split("\n")
    
    for index,line in enumerate(text):
        if line.startswith("<img>"):
            img = re.sub(r'<img>\[', "", line)
            img = re.sub(r'\].*?', "", img)
            img = re.sub(r'\[', "", img)
            if img not in images:
                print(f"Image: {img}\nFile: {file}")
            img = urllib.parse.quote(img)
            text[index] = f"<img>[{img}]"

    with open(f"./formatted/{file}", "w", encoding="utf-8") as f:
        f.write("\n".join(text))

