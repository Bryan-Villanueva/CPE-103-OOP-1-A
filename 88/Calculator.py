from tkinter import *
from tkinter import font
class MyWindow:
    def __init__(self, win):
        bold_font = font.Font(size= 9, weight="bold")
        # Labels and Buttons
        # Labels
        self.lbl1=Label(win, text='First number', bg= "#CD5C5C", font=bold_font)
        self.lbl1.place(x=100, y=50)
        self.t1 = Entry(bd=3)
        self.t1.place(x=200, y=50)

        self.lbl2=Label(win, text='Second number', bg= "#CD5C5C", font=bold_font)
        self.lbl2.place(x=100, y=100)
        self.t2 = Entry(bd=3)
        self.t2.place(x=200, y=100)

        self.lbl3=Label(win, text='Result', bg= "#CD5C5C", font=bold_font)
        self.lbl3.place(x=100, y=150)
        self.t3=Entry(bd=3)
        self.t3.place(x=200, y=150)

        # Buttons
        self.btn1 = Button(win, text='Add')
        self.btn1 = Button(win, text='Add', fg="Blue", bg="Gray",font=bold_font, command=self.add)
        self.btn1.place(x=50, y=200)

        self.btn2=Button(win, text='Subtract')
        self.btn2 = Button(win, text='Subtract', fg = "Red", bg = "Gray", font=bold_font)
        self.btn2.bind('<Button-1>', self.sub)
        self.btn2.place(x=100, y=200)

        self.btn3=Button(win, text='Multiply')
        self.btn3 = Button(win, text='Multiply', fg = "Orange", bg = "Gray",font=bold_font, command=self.multiply)
        self.btn3.place(x=170, y=200)

        self.btn4=Button(win, text='Divide')
        self.btn4 = Button(win, text='Divide', fg = "Yellow", bg = "Gray",font=bold_font, command=self.divide)
        self.btn4.place(x=240, y=200)

        self.btn5=Button(win, text='Clear')
        self.btn5 = Button(win, text='Clear', fg = "Brown", bg = "Gray",font=bold_font ,command=self.clear)
        self.btn5.place(x=300, y=200)

    # Methods
    def add(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 + num2
        self.t3.insert(END, str(result))

    def sub(self, event):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 - num2
        self.t3.insert(END, str(result))

    def multiply(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 * num2
        self.t3.insert(END, str(result))

    def divide(self):
        self.t3.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        result = num1 // num2
        self.t3.insert(END, str(result))

    def clear(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.t3.delete(0, 'end')

window = Tk()
mywin = MyWindow(window)
window.title('Hello Python')
window.geometry("400x300+10+10")
window.configure(bg= "#CD5C5C")
window.mainloop()
