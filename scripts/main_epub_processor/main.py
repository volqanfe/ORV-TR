import urllib.parse
import bs4
import urllib
import os
import warnings
import re
from bs4 import BeautifulSoup

warnings.filterwarnings("ignore", category=bs4.XMLParsedAsHTMLWarning)


for file in os.listdir("OEBPS"):
    if not file.endswith(".xhtml"):
        continue
    with open(f"./OEBPS/{file}", "r", encoding="utf-8") as f:
        text = f.read()
        soup = BeautifulSoup(text, "lxml")

    chap = ""
    title = soup.h3.text
    chap += f"<title>{title.replace("Chapter","Ch")}\n"
    title_found = False

    for tag in soup.body.children:
        tag: bs4.element.Tag

        if tag.name == "div":
            title_found = True

        elif tag.name == "img":
            tag_src = ""
            tag_alt = ""
            if tag.has_attr("src"):
                tag_src = urllib.parse.unquote(tag["src"])
            if tag.has_attr("alt"):
                tag_alt = tag["alt"]

            if title_found:
                chap += f"<img>[{tag_src}][{tag_alt}]\n"
            else:
                chap += f"<cover>[{tag_src}][{tag_alt}]\n"

        if title_found == False:
            continue

        if tag.name == "p":
            tag_text = str(tag.text)
            if tag.has_attr("id"):
                tag_id = tag.a["href"]
                chap += f"{tag.text}\n"
                chap += f"<?>{tag_id}\n"
            elif tag_text.startswith("["):
                cleaned_text = re.sub(r"[\[\]]", "", tag_text)
                chap += f"<!>[{cleaned_text}]\n"
            elif tag_text.startswith("【"):
                cleaned_text = re.sub(r"[【】]", "", tag_text)
                chap += f"<#>【{cleaned_text}】\n"
            elif tag_text.startswith("「"):
                cleaned_text = re.sub(r"[「」]", "", tag_text)
                chap += f"<&>「{cleaned_text}」\n"
            else:
                chap += f"{tag.text}\n"

        elif tag.name == "br":
            chap += f"\n"

        elif tag.name == "hr":
            chap += f"***\n"

        elif tag.name == "fieldset":
            cleaned_text = str(tag.text).replace("<p>", "").replace("</p>", "")
            cleaned_text = re.sub(r"^\n+|\n+$", "", cleaned_text)

            chap += f"+\n{cleaned_text}\n+\n"


        elif tag.name == None or "div" or "aside":
            pass
        else:
            print(f"passed tag <{tag.name}>")
    for tag_aside in soup.find_all("aside"):
        tag_id = tag_aside["id"]
        chap = chap.replace(f"<?>#{tag_id}", f"<?>{tag_aside.text.strip()}")
    with open(f"./chapters/orv/{file[:-5]}txt", "w", encoding="utf-8") as f:
        f.write(chap)
