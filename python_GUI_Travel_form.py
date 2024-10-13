from tkinter import *

root = Tk()

def saveDetails():
    
    with open("records.txt","a") as f:
        f.write(f"({nameval.get()},{ageval.get()},{Emailval.get()},{contactval.get()},{departureval.get()},{destinationval.get()},{departure_dateval.get()},{Return_dateval.get()},{foodserviceval.get()})\n")

root.title(("travel form").title())
root.geometry("900x500")
root.minsize(width=300,height=300)

# Frame
f1 = Frame(root, padx=10,pady=10)
#label1
l1 = Label(f1,text="Personal Details",font="bold 20").grid(row=0,column=2)

#label2
name = Label(f1,text="Full Name:",font="bold").grid(row=1,column=0,pady=10)
nameval = StringVar()
nameEntry = Entry(f1,textvariable=nameval).grid(row=1,column=1,pady=15)

#label2
age = Label(f1,text="Age:",font="bold").grid(row=1,column=4,pady=10)
ageval = IntVar()
ageEntry = Entry(f1, textvariable=ageval).grid(row=1,column=5,pady=15)

#label4
email = Label(f1,text="Email:",font="bold").grid(row=2,column=0,pady=10)
Emailval = StringVar()
emailEntry = Entry(f1,textvariable=Emailval).grid(row=2,column=1)

#label5
contact = Label(f1,text="Contact Number:",font="bold").grid(row=2,column=4,pady=10)
contactval = IntVar()
nameEntry = Entry(f1,textvariable=contactval).grid(row=2,column=5)

#label6
l2 = Label(f1,text="Travel Details",font="bold 20").grid(row=3,column=2)

#label7
departure_country = Label(f1,text="Depature Country:",font="bold").grid(row=4,column=0,pady=10)
departureval = StringVar()
departureEntry = Entry(f1,textvariable=departureval).grid(row=4,column=1,pady=15)

#label8
destination_country = Label(f1,text="Destination Country:",font="bold").grid(row=4,column=4,pady=10)
destinationval = StringVar()
destinationEntry = Entry(f1,textvariable=destinationval).grid(row=4,column=5,pady=15)

#label9
departure_date = Label(f1,text="Departure Date:",font="bold").grid(row=5,column=0,pady=10)
departure_dateval = StringVar()
departure_dateEntry = Entry(f1,textvariable=departure_dateval).grid(row=5,column=1,pady=15)

#label9
Return_date = Label(f1,text="Return Date:",font="bold").grid(row=5,column=4,pady=10)
Return_dateval = StringVar()
Return_date_Entry = Entry(f1,textvariable=Return_dateval).grid(row=5,column=5,pady=15)

foodserviceval = IntVar()
foodservice = Checkbutton(f1,text="Want food service.",font="bold 12",variable=foodserviceval).grid(row=6,column=0,pady=10)

submit = Button(f1,text="Submit",padx=6,pady=6,bg="grey",width=10,font="bold 10",borderwidth=6,command=saveDetails).grid(row=7,column=2)
f1.pack(pady=30)
root.mainloop()