from tkinter import *  # Import the tkinter module for GUI
import math  # Import the math module for mathematical operations
import tkinter.messagebox  # Import the messagebox module for displaying messages

# Create the main window
root = Tk()
root.title("Scientific Calculator")  # Set the title of the window
root.configure(background='white')  # Set background color
root.resizable(width=True, height=True)  # Allow resizing of the window
root.geometry("944x568+0+0")  # Set the initial size and position of the window

# Create a frame to hold the calculator elements
calc = Frame(root)
calc.grid()

# Define a class for the calculator
class Calc():
    def __init__(self):
        # Initialize various attributes to manage the calculator state
        self.total = 0
        self.current = ''
        self.input_value = True
        self.check_sum = False
        self.op = ''
        self.result = False

    # Method to handle number entry
    def numberEnter(self, num):
        self.result = False
        firstnum = txtDisplay.get()
        secondnum = str(num)
        if self.input_value:
            self.current = secondnum
            self.input_value = False
        else:
            if secondnum == '.':
                if secondnum in firstnum:
                    return
            self.current = firstnum + secondnum
        self.display(self.current)

    # Method to calculate the sum of total
    def sum_of_total(self):
        self.result = True
        self.current = float(self.current)
        if self.check_sum == True:
            self.valid_function()
        else:
            self.total = float(txtDisplay.get())

    # Method to update the display
    def display(self, value):
        txtDisplay.delete(0, END)
        txtDisplay.insert(0, value)

    # Method to perform valid arithmetic functions
    def valid_function(self):
        if self.op == "add":
            self.total += self.current
        if self.op == "sub":
            self.total -= self.current
        if self.op == "multi":
            self.total *= self.current
        if self.op == "divide":
            self.total /= self.current
        if self.op == "mod":
            self.total %= self.current
        self.input_value = True
        self.check_sum = False
        self.display(self.total)

    # Method to handle arithmetic operations
    def operation(self, op):
        self.current = float(self.current)
        if self.check_sum:
            self.valid_function()
        elif not self.result:
            self.total = self.current
            self.input_value = True
        self.check_sum = True
        self.op = op
        self.result = False

    # Method to clear the current entry
    def Clear_Entry(self):
        self.result = False
        self.current = "0"
        self.display(0)
        self.input_value = True

    # Method to clear all entries
    def All_Clear_Entry(self):
        self.Clear_Entry()
        self.total = 0

    # Method to display the mathematical constant pi
    def pi(self):
        self.result = False
        self.current = math.pi
        self.display(self.current)

    # Method to display the mathematical constant tau
    def tau(self):
        self.result = False
        self.current = math.tau
        self.display(self.current)

    # Method to display the mathematical constant e
    def e(self):
        self.result = False
        self.current = math.e
        self.display(self.current)

    # Method to toggle positive/negative
    def mathPM(self):
        self.result = False
        self.current = -(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate the square root
    def squared(self):
        self.result = False
        self.current = math.sqrt(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate cosine
    def cos(self):
        self.result = False
        self.current = math.cos(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate hyperbolic cosine
    def cosh(self):
        self.result = False
        self.current = math.cosh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate tangent
    def tan(self):
        self.result = False
        self.current = math.tan(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate hyperbolic sine
    def sinh(self):
        self.result = False
        self.current = math.sinh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate sine
    def sin(self):
        self.result = False
        self.current = math.sin(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate logarithm
    def log(self):
        self.result = False
        self.current = math.log(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate exponentiation
    def exp(self):
        self.result = False
        self.current = math.exp(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate inverse hyperbolic cosine
    def acosh(self):
        self.result = False
        self.current = math.acosh(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate inverse hyperbolic sine
    def asinh(self):
        self.result = False
        self.current = math.asinh(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate inverse hyperbolic tangent
    def atanh(self):
        self.result = False
        self.current = math.atanh(math.radians(float(txtDisplay.get())))
        self.display(self.current)

    # Method to calculate the floor
    def floor(self):
        self.result = False
        self.current = math.floor(float(txtDisplay.get()))
        self.display(self.current)

    # Method to convert to radians
    def radians(self):
        self.result = False
        self.current = math.radians(float(txtDisplay.get()))
        self.display(self.current)

    # Method to convert to degrees
    def degrees(self):
        self.result = False
        self.current = math.degrees(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate the ceiling
    def ceil(self):
        self.result = False
        self.current = math.ceil(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate the absolute value
    def abs(self):
        self.result = False
        self.current = abs(float(txtDisplay.get()))
        self.display(self.current)

    # Method to calculate the power
    def pow(self):
        self.result = False
        # Method to calculate the power
        self.result = False
        # You're missing the parameters for math.pow(). It should take two arguments.
        # Let's say we want to raise the current number to the power of 2.
        # We would do something like this:
        self.current = math.pow(float(txtDisplay.get()), 2)
        self.display(self.current)


# Create an instance of the Calc class
added_value = Calc()

# Create the display entry widget
txtDisplay = Entry(calc, font=('Helvetica', 20, 'bold italic'), bg='white', fg='grey', bd=30, width=28, justify=RIGHT)
txtDisplay.grid(row=0, column=0, columnspan=4)
txtDisplay.insert(0, "0")  # Insert initial value into the display

# Define the numbers and operators buttons
numberpadd = "789456123"  # Numbers
i = 0
btn = []  # List to hold the number buttons
# Create buttons for each number and assign the number to their command
for j in range(2, 5):
    for k in range(3):
        btn.append(Button(calc, width=6, height=2, bg='white', fg='pink', font=('Helvetica', 20, 'bold italic'), bd=4,
                          text=numberpadd[i]))
        btn[i].grid(row=j, column=k, pady=1)
        btn[i]["command"] = lambda x=numberpadd[i]: added_value.numberEnter(x)
        i += 1

# Define the Clear, All Clear, Square Root, and Arithmetic Operator buttons
btnClear = Button(calc, text=chr(67), width=6, height=2, bg='white',
                  font=('Helvetica', 20, 'bold italic'), bd=4,
                  command=added_value.Clear_Entry).grid(row=1, column=0, pady=1)

btnAllClear = Button(calc, text=chr(67) + chr(69), width=6, height=2, bg='white',
                     font=('Helvetica', 20, 'bold italic'), bd=4,
                     command=added_value.All_Clear_Entry).grid(row=1, column=1, pady=1)

btnsq = Button(calc, text="\u221A", width=6, height=2, bg='white',
               font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.squared).grid(row=1, column=2, pady=1)

btnAdd = Button(calc, text="+", width=6, height=2, bg='white',
                font=('Helvetica', 20, 'bold italic'), bd=4,
                command=lambda: added_value.operation("add")).grid(row=1, column=3, pady=1)

btnSub = Button(calc, text="-", width=6, height=2, bg='white',
                font=('Helvetica', 20, 'bold italic'), bd=4,
                command=lambda: added_value.operation("sub")).grid(row=2, column=3, pady=1)

btnMul = Button(calc, text="x", width=6, height=2, bg='white',
                font=('Helvetica', 20, 'bold italic'), bd=4,
                command=lambda: added_value.operation("multi")).grid(row=3, column=3, pady=1)

btnDiv = Button(calc, text="/", width=6, height=2, bg='white',
                font=('Helvetica', 20, 'bold italic'), bd=4,
                command=lambda: added_value.operation("divide")).grid(row=4, column=3, pady=1)

# Define the Zero, Decimal Point, Plus/Minus, and Equals buttons
btnZero = Button(calc, text="0", width=6, height=2, bg='white',
                 fg='pink', font=('Helvetica', 20, 'bold italic'), bd=4,
                 command=lambda: added_value.numberEnter("0")).grid(row=5, column=0, pady=1)

btnDot = Button(calc, text=".", width=6, height=2, bg='white',
                font=('Helvetica', 20, 'bold italic'), bd=4,
                command=lambda: added_value.numberEnter(".")).grid(row=5, column=1, pady=1)

btnPM = Button(calc, text=chr(177), width=6, height=2, bg='white',
               font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.mathPM).grid(row=5, column=2, pady=1)

btnEquals = Button(calc, text="=", width=6, height=2, bg='white',
                   font=('Helvetica', 20, 'bold italic'), bd=4,
                   command=added_value.sum_of_total).grid(row=5, column=3, pady=1)

# Define the buttons for additional mathematical functions
# Row 1
btnPi = Button(calc, text="pi", width=6, height=2, bg='white', fg='#b3048a',
               font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.pi).grid(row=1, column=4, pady=1)

btnsin = Button(calc, text="sin", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.sin).grid(row=1, column=5, pady=1)

btnCos = Button(calc, text="Cos", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.cos).grid(row=1, column=6, pady=1)

# Row 2
btntan = Button(calc, text="tan", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.tan).grid(row=2, column=4, pady=1)

btn2Pi = Button(calc, text="2pi", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.tau).grid(row=2, column=5, pady=1)

btnlog = Button(calc, text="log", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.log).grid(row=2, column=6, pady=1)

# Row 3
btnExp = Button(calc, text="exp", width=6, height=2, bg='white', fg='#b3048a',
                font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.exp).grid(row=3, column=4, pady=1)

btnMod = Button(calc, text="Mod", width=6, height=2, bg='white', fg='#b3048a',
font=('Helvetica', 20, 'bold italic'), bd=4, command=lambda: added_value.operation("mod")).grid(row=3, column=6, pady=1)

btnE = Button(calc, text="e", width=6, height=2, bg='white', fg='#b3048a',
font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.e).grid(row=3, column=5, pady=1)

btnpow = Button(calc, text="pow", width=6, height=2, bg='white',
fg='#b3048a', font=('Helvetica', 20, 'bold italic'), bd=4,
command=lambda: added_value.pow).grid(row=4, column=4, pady=1)

btndeg = Button(calc, text="deg", width=6, height=2, bg='white', fg='#b3048a',
font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.degrees).grid(row=4, column=5, pady=1)

btnradians = Button(calc, text="radians", width=6, height=2, bg='white', fg='#b3048a',
font=('Helvetica', 20, 'bold italic'), bd=4, command=added_value.radians).grid(row=4, column=6,
pady=1)

lblDisplay = Label(calc, text="Scientific Calculator", font=('Helvetica', 30, 'bold'), bg='#e055c0', fg='black',
justify=CENTER)
lblDisplay.grid(row=0, column=4, columnspan=4) # Position the label

Calc() # Create an instance of the Calc class

root.mainloop() # Start the GUI event loop