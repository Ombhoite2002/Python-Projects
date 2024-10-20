from tkinter import *
import os
import tkinter.messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename

class Notepad(Tk):
    def __init__(self):
        super().__init__()
        self.width = 800
        self.height = 400
        self.geometry(f'{self.width}x{self.height}')
        self.minsize(width=400, height=300)
        self.maxsize(width=1200, height=800)

        # Initialize filename and textarea
        self.filename = None
        self.textarea = None

    def setTitle(self):
        self.title("Untitled - Notepad")

    def setMenu(self):
        mainmenu = Menu(self)
        self.config(menu=mainmenu)
        return mainmenu

    def set_Filemenu(self, mainmenu):
        Filemenu = Menu(mainmenu, tearoff=0)
        Filemenu.add_command(label="New", command=self.newFile)
        Filemenu.add_command(label="Open", command=self.openFile)
        Filemenu.add_command(label="Save", command=self.saveFile)
        Filemenu.add_separator()
        Filemenu.add_command(label="Exit", command=self.exit)
        mainmenu.add_cascade(label="File", menu=Filemenu)

    def set_Editmenu(self, mainmenu):
        Editmenu = Menu(mainmenu, tearoff=0)
        Editmenu.add_command(label="Cut", command=self.cut)
        Editmenu.add_command(label="Copy", command=self.copy)
        Editmenu.add_command(label="Paste", command=self.paste)
        mainmenu.add_cascade(label="Edit", menu=Editmenu)

    def set_Helpmenu(self, mainmenu):
        Helpmenu = Menu(mainmenu, tearoff=0)
        Helpmenu.add_command(label="About Notepad", command=self.about)
        mainmenu.add_cascade(label="Help", menu=Helpmenu)

    def set_Scrollbar(self):
        scrollbar = Scrollbar(self)
        scrollbar.pack(side=RIGHT, fill=Y)
        return scrollbar

    def set_TextArea(self, scrollbar):
        self.textarea = Text(self, yscrollcommand=scrollbar.set)
        self.textarea.pack(expand=True, fill=BOTH)
        scrollbar.config(command=self.textarea.yview)

    # Class Methods

    def newFile(self):
        self.filename = None
        self.setTitle()
        self.textarea.delete(1.0, END)
        print("New File Created")

    def openFile(self):
        self.filename = askopenfilename(defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if self.filename:
            with open(self.filename, "r") as file:
                self.textarea.delete(1.0, END)
                self.textarea.insert(1.0, file.read())
            self.title(os.path.basename(self.filename) + " - Notepad")

    def saveFile(self):
        if self.filename is None:
            # Save as new file
            self.filename = asksaveasfilename(initialfile='Untitled.txt',
                                              defaultextension=".txt",
                                              filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
            if not self.filename:
                return
        with open(self.filename, "w") as file:
            file.write(self.textarea.get(1.0, END))
        self.title(os.path.basename(self.filename) + " - Notepad")

    def exit(self):
        self.destroy()

    def cut(self):
        self.textarea.event_generate("<<Cut>>")

    def copy(self):
        self.textarea.event_generate("<<Copy>>")

    def paste(self):
        self.textarea.event_generate("<<Paste>>")

    def about(self):
        tmsg.showinfo("Notepad", "Code with @Om")


