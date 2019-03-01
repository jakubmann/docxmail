from Functions import format

class Article:
    def __init__(self):
        self.heading = ""
        self.paragraphs = []
        self.vice = ""
        self.img = ""

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
        if self.img != "":
            output += format("template/image.html", self.img, "{\IMG}")
        return output
