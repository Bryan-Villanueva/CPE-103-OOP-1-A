import tkinter as tk
import math

def seven(event=0): entry.insert(tk.END, "7")
def eight(event=0): entry.insert(tk.END, "8")
def nine(event=0): entry.insert(tk.END, "9")
def four(event=0): entry.insert(tk.END, "4")
def five(event=0): entry.insert(tk.END, "5")
def six(event=0): entry.insert(tk.END, "6")
def one(event=0): entry.insert(tk.END, "1")
def two(event=0): entry.insert(tk.END, "2")
def three(event=0): entry.insert(tk.END, "3")
def zero(event=0): entry.insert(tk.END, "0")
def decimal(event=0): entry.insert(tk.END, ".")
def addition(event=0): entry.insert(tk.END, "+")
def subtraction(event=0): entry.insert(tk.END, "-")
def multiply(event=0): entry.insert(tk.END, "*")
def division(event=0): entry.insert(tk.END, "/")
def parent1(event=0): entry.insert(tk.END, "(")
def parent2(event=0): entry.insert(tk.END, ")")
def delete(event=0):
    current_text = entry.get()
    if len(current_text) > 0:
        entry.delete(len(current_text)-1, tk.END)
def clear(event=0): entry.delete(0, tk.END)
def equal(event=0):
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def sin_function():
    try:
        result = math.sin(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def cos_function():
    try:
        result = math.cos(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def tan_function():
    try:
        result = math.tan(math.radians(float(entry.get())))
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")
def exponent(event=0): entry.insert(tk.END, "**")

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("360x500")
root.config(bg="#f4f4f4")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), borderwidth=3, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4, ipady=10, pady=10, sticky="nsew")

def create_button(text, row, col, command, bg="#f0f0f0", fg="black"):
    button = tk.Button(
        root, text=text, font=("Arial", 16),
        bg=bg, fg=fg, relief="groove", activebackground="#ddd",
        command=command, width=5, height=2
    )
    button.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")
    return button

create_button("sin", 1, 0, sin_function, bg="#ffcccb")
create_button("cos", 1, 1, cos_function, bg="#ffcccb")
create_button("tan", 1, 2, tan_function, bg="#ffcccb")
create_button("^", 1, 3, exponent, bg="#ffcccb")

create_button("7", 2, 0, seven)
create_button("8", 2, 1, eight)
create_button("9", 2, 2, nine)
create_button("/", 2, 3, division, bg="#d9d9d9")

create_button("4", 3, 0, four)
create_button("5", 3, 1, five)
create_button("6", 3, 2, six)
create_button("*", 3, 3, multiply, bg="#d9d9d9")

create_button("1", 4, 0, one)
create_button("2", 4, 1, two)
create_button("3", 4, 2, three)
create_button("-", 4, 3, subtraction, bg="#d9d9d9")

create_button("C", 5, 0, clear, bg="#ff6666", fg="white")
create_button("0", 5, 1, zero)
create_button(".", 5, 2, decimal)
create_button("=", 5, 3, equal, bg="#66b2ff", fg="white")

root.bind("1", one)
root.bind("2", two)
root.bind("3", three)
root.bind("4", four)
root.bind("5", five)
root.bind("6", six)
root.bind("7", seven)
root.bind("8", eight)
root.bind("9", nine)
root.bind("0", zero)
root.bind("+", addition)
root.bind("-", subtraction)
root.bind("*", multiply)
root.bind("/", division)
root.bind("<BackSpace>", delete)
root.bind("<Return>", equal)
root.bind("<Delete>", clear)
root.bind(")", parent1)
root.bind("(", parent2)
root.bind(".", decimal)
root.bind("^", exponent)

root.mainloop()