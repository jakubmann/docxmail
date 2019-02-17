from Functions import format

class Termin:
    def __init__(self):
        self.date = ""
        self.text = ""
        self.vice = ""
    def format(self):
        output = format("template/termin.html", self.text).replace("{\DATUM}", self.date)
        if self.vice != "":
            output = output.replace("{\VICE}", format("template/vice_termin.html", self.vice))
        return output.replace("{\VICE}", "")
