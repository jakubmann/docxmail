from tkinter import *
from tkinter import filedialog
from tkinter import Menu
from tkinter import messagebox

from Generate import *

class GUI:
    def __init__(self):
        def _rgb(rgb):
            return "#%02x%02x%02x" % rgb
        window = Tk()
        window.title("Word Email Generator")
        icon = Image("photo", file="mail.png")
        window.call('wm','iconphoto', window._w, icon)
        window.geometry('400x200')

        '''
        #Menu
        self.menu = Menu(self.window)

        file = Menu(self.menu, tearoff=0)
        file = Menu(self.menu, tearoff=0)

        file.add_command(label='Open', command=self.findFile)
        file.add_separator()
        file.add_command(label='Format', command=self.format)

        self.menu.add_cascade(label='File', menu=file)
        self.window.config(menu=self.menu)
        '''

        _outputFrame = Frame(window)

        #Buttons
        _open = Button(window, text="Open a document", command=self.findFile, font=("Consolas", 10))
        _generate = Button(window, text="Generate email", command=self.generate, font=("Consolas", 10))

        self._output = Entry(_outputFrame,width=20, font=("Consolas ", 10))
        _lbl_output = Label(_outputFrame, text="Output filename:", font=("Consolas", 10))

        #Title
        _title = Label(window, text="Word Email Formatter", font=("Consolas", 20, "bold"))


        #Colors
        _color_bg = _rgb((20, 20, 186))
        _btn_bg = _rgb((50, 50, 252))

        window.configure(background=_color_bg)
        _outputFrame.configure(background=_color_bg)

        _title.configure(bg=_color_bg, fg="white")
        _lbl_output.configure(bg=_color_bg, fg="white")

        _open.configure(border=3, bg=_btn_bg, fg="white")
        _generate.configure(border=3, bg=_btn_bg, fg="white")

        #Layout
        _title.pack()
        _open.pack(fill=X, padx=50, pady=15, side=TOP)
        _lbl_output.pack(fill=X, padx=10, side=LEFT)
        self._output.pack(fill=X, padx=10, side=RIGHT)
        _outputFrame.pack()
        _generate.pack(fill=X, padx=100, pady=20, side=BOTTOM)
        window.mainloop()

    def findFile(self):
        self.file = filedialog.askopenfilename(filetypes = (("Word Documents","*.docx"),("all files","*.*")))

    def generate(self):
        if self._output.get() == "":
            output_file = "email"
        else:
            output_file = self._output.get()
        try:
            if self.file:
                generate(self.file, output_file)
                messagebox.showinfo("Success!", "Email successfuly generated!")
        except AttributeError:
            messagebox.showinfo("Error", "No document open")
