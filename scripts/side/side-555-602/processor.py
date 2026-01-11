import os
import re


for i,file in enumerate(os.listdir("./side/chs")):

    file_index = int(file.replace(".txt", "").replace("ch_",""))

    if not file.endswith(".txt"):
        continue
    with open(f"./side/chs/{file}", "r", encoding="utf-8") as f:
        text = f.read().split("\n")

    chap = ""
    title = text[0]
    chap += f"<title>{title}\n"

    text.pop(0)
    counter = 0

    for index,line in enumerate(text):

        if line == "":
            chap += "\n"
        elif line.startswith("["):
            if re.match(r"^\[.*\]$", line):
                cleaned_text = re.sub(r"[\[\]]", "", line)
                chap += f"<!>[{cleaned_text}]\n"
        elif line.startswith("【"):
            if re.match(r"^【.*】$", line):
                cleaned_text = re.sub(r"[【】]", "", line)
                chap += f"<#>【{cleaned_text}】\n"
        elif line.startswith("「"):
            if re.match(r"^「.*」$", line):
                cleaned_text = re.sub(r"[「」]", "", line)
                chap += f"<&>「{cleaned_text}」\n"

        elif line.startswith("(TL"):
                cleaned_text = re.sub(r"[()]", "", line)
                chap += f"<?>{cleaned_text.replace("TL: ", "")}"
        elif line == "*":
            chap += f"***\n"
        else:
            counter += 1
            chap += line+"\n"

    
    print(file_index,len(text),len(text)-counter)
        
    with open(f"./side/chs/{file}", "w", encoding="utf-8") as f:
        f.write(chap)
