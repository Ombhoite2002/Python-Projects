from Notepad_GUI import *
from tkinter import *

if __name__ == "__main__":
    Notepad = Notepad()
    Notepad.setTitle()
    mainmenu = Notepad.setMenu()
    Notepad.set_Filemenu(mainmenu)
    Notepad.set_Editmenu(mainmenu)
    Notepad.set_Helpmenu(mainmenu)
    scrollbar = Notepad.set_Scrollbar()
    Notepad.set_TextArea(scrollbar)
    Notepad.mainloop()

