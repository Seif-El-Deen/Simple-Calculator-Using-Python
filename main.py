class Calculator:
    def __init__(self, num1, num2):
        self.number1 = num1
        self.number2 = num2
    def subtract(self):
        print(self.number1, "-", self.number2, "=", self.number1-self.number2)
        subtractValueLabel['text'] = str(self.number1-self.number2)
    def add(self):
        print(self.number1, "+", self.number2, "=", self.number1+self.number2)
        addValueLabel['text'] = str(self.number1+self.number2)
    def divide(self):
        print(self.number1, "/", self.number2, "=", self.number1/self.number2)
        divideValueLabel['text'] = str(self.number1/self.number2)
    def multiply(self):
        print(self.number1, "*", self.number2, "=", self.number1*self.number2)
        multiplyValueLabel['text'] = str(self.number1*self.number2)
    def mod(self):
        print(self.number1, "%", self.number2, "=", self.number1%self.number2)
        modValueLabel['text'] = str(self.number1%self.number2)
    def calculate(self):
        self.add()
        self.subtract()
        self.divide()
        self.multiply()
        self.mod()


# calc = Calculator(13, 9)
#
# calc.subtract()
#
# print(calc.number1)
#
# print(calc.number2)

from tkinter import *


# Create the main window
root = Tk()
# root.overrideredirect(True)

# root.title("Get Text Box Value")
# Set the window size
root.geometry("480x500")
# Move the window to position (100, 100)
root.geometry("+500+50")
root.configure(bg="#bfdeff")

# Labels
app_title = Label(root, text="Simple Calculator", bg="#1D80AD", fg="white", font=("Helvetica", 20,'bold'), padx="10",pady="10" )
app_title.place(x=120, y=15)

num1Label = Label(root, text="Number 1", bg="#1D80AD", fg="white", font=("Helvetica", 16,'bold'), padx="10",pady="10" )
num1Label.place(x=100, y=100)

num2Label = Label(root, text="Number 2", bg="#1D80AD", fg="white", font=("Helvetica", 16, 'bold'), padx="5", pady="5")
num2Label.place(x=280, y=100)

 # Title Label 

addLabel = Label(root, text="Add", bg="#1D80AD", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
addLabel.place(x=35, y=230)

subtractLabel = Label(root, text="Subtract", bg="#1D80AD", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
subtractLabel.place(x=35, y=270)

divideLabel = Label(root, text="Divide", bg="#1D80AD", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
divideLabel.place(x=35, y=310)

multiplyLabel = Label(root, text="Multiply", bg="#1D80AD", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
multiplyLabel.place(x=35, y=350)

modLabel = Label(root, text="Mod", bg="#1D80AD", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
modLabel.place(x=35, y=390)

 
# Value Labels

addValueLabel = Label(root, text="Add", bg="#9B9B9C", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
addValueLabel.place(x=190, y=230)

subtractValueLabel = Label(root, text="Subtract", bg="#9B9B9C", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
subtractValueLabel.place(x=190, y=270)

divideValueLabel = Label(root, text="Divide", bg="#9B9B9C", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
divideValueLabel.place(x=190, y=310)

multiplyValueLabel = Label(root, text="Multiply", bg="#9B9B9C", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
multiplyValueLabel.place(x=190, y=350)

modValueLabel = Label(root, text="Mod", bg="#9B9B9C", fg="white", font=("Helvetica", 14, 'bold'), padx="5", pady="5")
modValueLabel.place(x=190, y=390)


# Text Inputs

num1InputText = Text(root, bg="#FFFFFF", font=("Helvetica", 16,'bold'))

num1InputText.place(x=120, y=160, height=40, width=80,)

num2InputText = Text(root, bg="#FFFFFF", font=("Helvetica", 16,'bold'))

num2InputText.place(x=300, y=160, height=40, width=80,)


def get_input():
    num1Input = int(num1InputText.get("1.0", "end-1c"))
    num2Input = int(num2InputText.get("1.0", "end-1c"))

    print(num1Input)
    print(num2Input)

    myCalculator = Calculator(num1Input, num2Input)

    myCalculator.calculate()





calculateButton = Button(root, text=" Calculate", command=lambda: get_input(), bg="#4287f5",font=("Helvetica", 16,'bold'), fg="white")
calculateButton.place(x=110, y=440)

closeButton = Button(root, text="Close", command=root.destroy, bg="#4287f5",font=("Helvetica", 16,'bold'), fg="white")
closeButton.place(x=300, y=440)


# Create the button
# button.pack()
# Create the close
# button_close.pack()

# Start the main loop
root.mainloop()




