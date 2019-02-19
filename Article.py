from Functions import format

class Article:
    def __init__(self):
        self.heading = ""
        self.paragraphs = []
        self.vice = ""

    def addParagraph(self, paragraph):
        self.paragraphs.append(paragraph)

    def format(self):
        paragraphs_text = ""
        for paragraph in self.paragraphs:
            if paragraph != "<terminy>":
                paragraphs_text += format("template/paragraph.html", paragraph)
        output = format("template/article.html", format("template/heading.html", self.heading) + paragraphs_text)
        if self.vice != "":
            output += format("template/vice.html", self.vice)
        return output
