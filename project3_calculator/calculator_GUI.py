from tkinter import *
from PIL import Image, ImageTk
import math

class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.width = 350
        self.height = 460
        self.geometry(f"{self.width}x{self.height}")
        self.minsize(width=350,height=400)
        self.maxsize(width=400,height=500)

    def Title(self,titleName):
        self.title((titleName).title())

    def changeBackground(self,component,color):
        self = component
        component.configure(background=color)

    def createFrame(self):
        f = Frame(self,background="#1E1E2D")
        return f
    
    def createLabel(self,frame,Imagefile,Row,Column):
        image = Image.open(Imagefile)
        resized_image = image.resize((75, 45))  # Resize image to 75x45 pixels
        file = ImageTk.PhotoImage(resized_image)
        label = Label(
        frame,
        image=file
    )
        label.image = file  # Keep a reference to avoid garbage collection
        label.grid(padx=2,pady=2,row=Row,column=Column)
        return label

    def defineCalvalue(self):
        self.Scvalue = StringVar()
        self.Scvalue.set("")

    def createEntry(self, frame):
        self.screenentry = Entry(
            frame,
            textvariable=self.Scvalue,
            font="bold 30",
            fg="white",            # Set text color to white
            bg="#1E1E2D",          # Set background color
            insertbackground="white",  # Set cursor color to white
            highlightthickness=0,   # Set outline thickness
            highlightbackground="white",  # Outline color when not focused
            highlightcolor="white",  # Outline color when focused
            justify=RIGHT,  # Insert text from the right side
            insertwidth=0  # Hide the cursor (this hides the cursor completely)
    )
        self.screenentry.pack(ipadx=10, ipady=10, fill=X, padx=15, pady=20)

    def createbutton(self, frame, textname, Row, Column, ImageFile=None, color=None):
        if ImageFile:
            # Load and resize the image if provided
            image = Image.open(ImageFile)
            resized_image = image.resize((34, 34))  # Resize the image
            file = ImageTk.PhotoImage(resized_image)
        
            # Create a button with both image and text
            button = Button(
                frame,
                text=textname,     # Button text
                image=file,        # Button image (optional)
                compound="left",   # Image on the left side of the text
                bg="#2D2D3B",      # Background color
                fg="white",        # Text color
                font="bold 15"     # Font style
            )
            button.image = file  # Keep a reference to avoid garbage collection

        elif color:
            # Create a button with custom background color (without image)
            button = Button(
                frame,
                text=textname,     # Button text
                bg=color,          # Use provided color
                fg="white",        # Text color
                font="bold 15",     # Font style
                width=3,           # Button width
                height=1
            )

        else:
            # Create a default button without image and custom color
            button = Button(
                frame,
                text=textname,     # Button text
                bg="#2D2D3B",      # Default background color
                fg="white",        # Text color
                font="bold 15",    # Font style
                width=3,           # Button width
                height=1           # Button height
            )

    # Grid layout positioning
        button.grid(padx=2, pady=2, row=Row, column=Column, ipadx=20, ipady=7)

    # Bind the button click event
        button.bind('<Button-1>', self.click)

    
    
    def click(self,event):

        text = event.widget.cget("text")
        backspace = event.widget.cget("image")

        if text == "=":
            if self.Scvalue.get().isdigit():
                value = int(self.Scvalue.get())
            else:
                value = eval(self.screenentry.get())

            self.Scvalue.set(value)
            self.screenentry.update()

        elif text == "C" or text == "CE":
            self.Scvalue.set('')
            self.screenentry.update()

        elif text == "x²":
            current_value = self.Scvalue.get()

            try:
                # Convert the current value to a float (handles both integers and floats)
                value = float(current_value)
                squared_value = value ** 2  # Square the value

                # Set the squared value back to the entry field
                self.Scvalue.set(str(squared_value))
                self.screenentry.update()

            except ValueError:
                # If conversion fails (non-numeric input), display an error message
                self.Scvalue.set("Error")
                self.screenentry.update()

        elif text == "sqrt":
            current_value = self.Scvalue.get()

            try:
                # Convert the current value to a float (handles both integers and floats)
                value = float(current_value)
                squaroot_value = math.sqrt(value)  # Square the value

                # Set the squared value back to the entry field
                self.Scvalue.set(str(squaroot_value))
                self.screenentry.update()

            except ValueError:
                # If conversion fails (non-numeric input), display an error message
                self.Scvalue.set("Error")
                self.screenentry.update()

        elif text == "1/x":
            current_value = self.Scvalue.get()

            try:
                # Convert the current value to a float (handles both integers and floats)
                value = float(current_value)

                # Check if value is zero to prevent division by zero
                if value == 0:
                    self.Scvalue.set("Error")  # Display an error for division by zero
                else:
                    reciprocal_value = 1 / value  # Calculate the reciprocal

                # Set the reciprocal value back to the entry field
                self.Scvalue.set(str(reciprocal_value))

                self.screenentry.update()

            except ValueError:
                # If conversion fails (non-numeric input), display an error message
                self.Scvalue.set("Error")
                self.screenentry.update()


        elif text == "Backspace" or backspace:  
            current_value = self.Scvalue.get()
            if current_value:
            # Remove the last character
                new_value = current_value[:-1]
                self.Scvalue.set(new_value)
                self.screenentry.update()

        else:
            self.Scvalue.set(self.Scvalue.get() + text)
            self.screenentry.update()

            

