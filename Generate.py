# coding=utf-8
import datetime


from docx import Document

from Functions import format
from Article import Article
from Termin import Termin

#Month
now = datetime.datetime.now()
months = {
    1   :   "Leden",
    2   :   "Únor",
    3   :   "Březen",
    4   :   "Duben",
    5   :   "Květen",
    6   :   "Červen",
    7   :   "Červenec",
    8   :   "Srpen",
    9   :   "Září",
    10  :   "Říjen",
    11  :   "Listopad",
    12  :   "Prosinec",
}


def generate(input_file, output_file):
    #Open files
    document = Document(input_file)
    f = open(output_file + ".html", "w+", encoding="utf-8")

    #Article Loop
    articles = []
    terminy = []
    isTermin = False
    for p in document.paragraphs:
        #Aktuality
        if not isTermin:
            if p.style.name == "Heading 1":
                articles.append(Article())
                articles[len(articles)-1].heading = p.text

            elif p.style.name == "Normal":
                if "<vice>" in p.text:
                    articles[len(articles)-1].vice = p.text.replace("<vice>", "")
                elif "<img>" in p.text:
                	if len(articles) < 1:
                		articles.append(Article())
                	articles[len(articles)-1].img = p.text.replace("<img>", "")
                else:
                    articles[len(articles)-1].addParagraph(p.text)
        #Terminy
        else:
            if p.style.name == "Normal":
                if "<vice>" in p.text:
                    terminy[len(terminy)-1].vice = p.text.replace("<vice>", "")
                else:
                    termin = p.text.split(" ")
                    terminy.append(Termin())
                    terminy[len(terminy)-1].date = termin[0]
                    for text in termin[1:]:
                        terminy[len(terminy)-1].text += " " + text
        if p.text == "<terminy>":
            isTermin = True

    #Output
    output_terminy = ""
    for termin in terminy:
        output_terminy += termin.format()


    if len(articles) % 2 == 0:
        first = articles[:int(len(articles)/2)]
        second = articles[int(len(articles)/2):len(articles)]

    else:
        first = articles[:int(len(articles)/2+1)]
        second = articles[int(len(articles)/2+1):len(articles)]

    body = ""
    output_first = ""
    output_second = ""
    for article in first:
        output_first += article.format()
    for article in second:
        output_second += article.format()

    body = format("template/main.html", output_first, "{MAIN_FIRST}").replace("{TERMINY}", output_terminy)
    f.write(body
                .replace("{MAIN_SECOND}", output_second)
                .replace("{MONTH}", months[now.month])
                .replace("{YEAR}", str(now.year))
            )
    f.close()
