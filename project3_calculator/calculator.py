from tkinter import *
from calculator_GUI import * 
if __name__ == '__main__':

    windows = GUI()
    windows.Title("calculator")

    windows.iconbitmap("calculator.ico")

    windows.changeBackground(windows,"#1E1E2D")

    f1 = windows.createFrame()
    f1.pack(fill=X)

    windows.defineCalvalue()
    windows.createEntry(f1)
    
    f2 = windows.createFrame()
    f2.pack(padx=2)
    # 1st Row
    windows.createbutton(f2,"%",0,0)
    windows.createbutton(f2,"CE",0,1)
    windows.createbutton(f2,"C",0,2)
    windows.createbutton(f2,None,0,3,"backspace_icon.png",None)
    # 2nd Row
    windows.createbutton(f2,"1/x",1,0)
    windows.createbutton(f2,"x²",1,1)
    windows.createbutton(f2,"sqrt",1,2)
    windows.createbutton(f2,"/",1,3)
    # 3rd Row
    windows.createbutton(f2,"7",2,0)
    windows.createbutton(f2,"8",2,1)
    windows.createbutton(f2,"9",2,2)
    windows.createbutton(f2,"*",2,3)
    # 4th Row
    windows.createbutton(f2,"4",3,0)
    windows.createbutton(f2,"5",3,1)
    windows.createbutton(f2,"6",3,2)
    windows.createbutton(f2,"-",3,3)
    # 5th Row
    windows.createbutton(f2,"1",4,0)
    windows.createbutton(f2,"2",4,1)
    windows.createbutton(f2,"3",4,2)
    windows.createbutton(f2,"+",4,3)
    # 6th Row
    windows.createbutton(f2,"+/-",5,0)
    windows.createbutton(f2,"0",5,1)
    windows.createbutton(f2,".",5,2)
    windows.createbutton(f2,"=",5,3,None,"orange")
    windows.mainloop()


