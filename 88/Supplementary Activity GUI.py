#  GUI Conversion of the Calculator:
import tkinter as tk

def add():
    result.set(float(entry1.get()) + float(entry2.get()))

def subtract():
    result.set(float(entry1.get()) - float(entry2.get()))

def multiply():
    result.set(float(entry1.get()) * float(entry2.get()))

def clear():
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')
    result.set("")

def square_root():
    result.set(float(entry1.get()) ** 0.5)
    result.set(float(entry2.get()) ** 0.5)

def divide():
    try:
        result.set(float(entry1.get()) / float(entry2.get()))
    except ZeroDivisionError:
        result.set("Error! Division by zero.")

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")

# Create StringVar to hold the result
result = tk.StringVar()

# Create the layout
tk.Label(root, text="Enter first number:", bg = "#6495ED").place(x=50, y=50)
entry1 = tk.Entry(root, bg= "#CCCCFF")
entry1.place(x=160, y=50)

tk.Label(root, text="Enter second number:", bg = "#6495ED").place(x=50, y=80)
entry2 = tk.Entry(root, bg= "#CCCCFF")
entry2.place(x=180, y=80)

tk.Label(root, text="CALCULATOR", bg = "#6495ED").place(x=50, y=20)

# Buttons for operations
tk.Button(root, text="Add", bg= "#cce1ea", command=add).place(x=70, y=160)
tk.Button(root, text="Subtract", bg= "#cce1ea", command=subtract).place(x=70,y=200)
tk.Button(root, text="Multiply", bg= "#cce1ea", command=multiply).place(x=120,y=160)
tk.Button(root, text="Divide", bg= "#cce1ea", command=divide).place(x=140, y=200)
tk.Button(root, text= "Clear", bg= "#d34a6e", command=clear).place(x=70, y=285)
tk.Button(root, text= "√Square Root", bg= "#cce1ea", command=square_root).place(x=70, y=240)
tk.Button(root, text= "x^", bg= "#cce1ea", command=clear).place(x=160, y=240)
tk.Button(root, text= "sin", bg= "#cce1ea", command=clear).place(x=195, y=160)
tk.Button(root, text= "cos", bg= "#cce1ea", command=clear).place(x=195, y=200)
tk.Button(root, text= "tan", bg= "#cce1ea", command=clear).place(x=195, y=240)

# Label to show result
tk.Label(root, text="Result:", bg = "#6495ED").place(x=50, y=110)
result_label = tk.Label(root, bg= "#CCCCFF", textvariable=result)
result_label.place(x=100, y=110)

# History


root.geometry("600x400+10+10")
root.configure(bg="#6495ED")
# Start the main loop
root.mainloop()