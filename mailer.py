from docx import Document

def format(filename, text, originalstring = "{\TEXT}"):
    with open(filename) as f:
        s = f.read()
    s = s.replace(originalstring, text)
    return s

def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print ('"{old_string}" not found in {filename}.'.format(**locals()))
            return

    with open(filename, 'w') as f:
        s = s.replace(old_string, new_string)
        f.write(s)

document = Document('email.docx')

f = open("email.html", "w+")


#articles
articles = []
count = 0
heading_text = ""
paragraph_text = ""
vice_text = ""
terminy = False
terminy_text = ""
for p in document.paragraphs:
    if not terminy:
        if p.style.name == "Heading 1":
            heading_text += (format("template/heading.html", p.text)) + "\n"
        elif p.style.name == "Normal":
            if "{vice}" in p.text:
                vice_text += (format("template/vice.html", p.text.replace("{vice}", ""))) + "\n"
            elif "{terminy}" in p.text:
                terminy = True
            else:
                paragraph_text += (format("template/paragraph.html", p.text)) + "\n"

        if heading_text != "" and paragraph_text != "":
            output = heading_text + paragraph_text
            if vice_text != "":
                output += vice_text
                vice_text = ""
            articles.append(format("template/article.html", output))
            count += 1
            heading_text = ""
            paragraph_text = ""
    else:
        terminy_text += p.text

if count % 2 == 0:
    first = ""
    second = ""
    for i in range(int(len(articles)/2)):
        first += articles[i]
    for i in range(int(len(articles)/2), len(articles)):
        second += articles[i]
else:
    first = ""
    second = ""
    for i in range(int(len(articles)/2+1)):
        first += articles[i]
    for i in range(int(len(articles)/2+1), len(articles)):
        second += articles[i]

f.write(format("template/main.html", first, "{\MAIN_FIRST}"))
inplace_change("email.html", "{\MAIN_SECOND}", second)
inplace_change("email.html", "{\TERMINY}", terminy_text)

f.close()
