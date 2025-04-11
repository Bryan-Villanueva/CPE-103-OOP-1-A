import tkinter as tk
import math
from tkinter import font


# Calculator functions
def calculate(operation):
    try:
        if operation == "add":
            res = float(entry1.get()) + float(entry2.get())
            history.append(f"{entry1.get()} + {entry2.get()} = {res}")
        elif operation == "subtract":
            res = float(entry1.get()) - float(entry2.get())
            history.append(f"{entry1.get()} - {entry2.get()} = {res}")
        elif operation == "multiply":
            res = float(entry1.get()) * float(entry2.get())
            history.append(f"{entry1.get()} × {entry2.get()} = {res}")
        elif operation == "divide":
            res = float(entry1.get()) / float(entry2.get())
            history.append(f"{entry1.get()} ÷ {entry2.get()} = {res}")
        elif operation == "sqrt":
            num = float(entry3.get())
            res = math.sqrt(num) if num >= 0 else "Invalid Input"
            history.append(f"√{num} = {res}")
        elif operation == "power":
            res = float(entry4.get()) ** float(entry5.get())
            history.append(f"{entry4.get()}^{entry5.get()} = {res}")
        elif operation in ["sin", "cos", "tan"]:
            num = float(entry6.get())
            res = getattr(math, operation)(num)
            history.append(f"{operation}({num}) = {res}")
        elif operation in ["asin", "acos", "atan"]:
            num = float(entry6.get())
            if operation in ["asin", "acos"] and not -1 <= num <= 1:
                res = "Must be between -1 and 1"
            else:
                res = math.degrees(getattr(math, operation)(num))
                res = f"{res}°"
            history.append(f"{operation}({num}) = {res}")

        result.set(f"{res:.6f}".rstrip('0').rstrip('.') if isinstance(res, float) else res)
        update_history()
    except ValueError:
        result.set("Invalid Input")
        history.append("Invalid Input")
        update_history()
    except ZeroDivisionError:
        result.set("Cannot divide by zero")
        history.append("Cannot divide by zero")
        update_history()


def clear_all():
    for entry in [entry1, entry2, entry3, entry4, entry5, entry6]:
        entry.delete(0, 'end')
    result.set("")


def update_history():
    history_listbox.delete(0, "end")
    for item in history:
        history_listbox.insert("end", item)


def clear_history():
    history.clear()
    update_history()


# Main window setup
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("680x600")
root.configure(bg="#2E3440")
root.resizable(False, False)

history = []
result = tk.StringVar()

# Fonts
title_font = font.Font(size=14, weight="bold")
label_font = font.Font(size=11)
button_font = font.Font(size=10)

# Main layout
main_frame = tk.Frame(root, bg="#2E3440")
main_frame.pack(pady=10)

tk.Label(main_frame, text="Scientific Calculator", bg="#2E3440", fg="#88C0D0",
         font=title_font).grid(row=0, column=0, columnspan=2, pady=10)

# Basic operations
basic_frame = tk.LabelFrame(main_frame, text="Basic Operations", bg="#2E3440", fg="#E5E9F0")
basic_frame.grid(row=1, column=0, padx=10, pady=5)

tk.Label(basic_frame, text="Number 1:", bg="#2E3440", fg="#E5E9F0").grid(row=0, column=0)
entry1 = tk.Entry(basic_frame, bg="#3B4252", fg="#E5E9F0")
entry1.grid(row=0, column=1)

tk.Label(basic_frame, text="Number 2:", bg="#2E3440", fg="#E5E9F0").grid(row=1, column=0)
entry2 = tk.Entry(basic_frame, bg="#3B4252", fg="#E5E9F0")
entry2.grid(row=1, column=1)

buttons_frame = tk.Frame(basic_frame, bg="#2E3440")
buttons_frame.grid(row=2, columnspan=2, pady=5)

for i, (text, op) in enumerate([("+", "add"), ("-", "subtract"), ("×", "multiply"), ("÷", "divide")]):
    tk.Button(buttons_frame, text=text, command=lambda o=op: calculate(o),
              bg="#3B4252", fg="#E5E9F0").grid(row=0, column=i, padx=2)

# Advanced operations
advanced_frame = tk.LabelFrame(main_frame, text="Advanced Operations", bg="#2E3440", fg="#E5E9F0")
advanced_frame.grid(row=2, column=0, padx=10, pady=5)

tk.Label(advanced_frame, text="Square root:", bg="#2E3440", fg="#E5E9F0").grid(row=0, column=0)
entry3 = tk.Entry(advanced_frame, bg="#3B4252", fg="#E5E9F0", width=15)
entry3.grid(row=0, column=1)
tk.Button(advanced_frame, text="√", command=lambda: calculate("sqrt"), bg="#3B4252", fg="#E5E9F0").grid(row=0, column=2)

tk.Label(advanced_frame, text="Power:", bg="#2E3440", fg="#E5E9F0").grid(row=1, column=0)
power_frame = tk.Frame(advanced_frame, bg="#2E3440")
power_frame.grid(row=1, column=1, columnspan=2)

tk.Label(power_frame, text="Base:", bg="#2E3440", fg="#E5E9F0").pack(side="left")
entry4 = tk.Entry(power_frame, bg="#3B4252", fg="#E5E9F0", width=8)
entry4.pack(side="left")

tk.Label(power_frame, text="Exp:", bg="#2E3440", fg="#E5E9F0").pack(side="left")
entry5 = tk.Entry(power_frame, bg="#3B4252", fg="#E5E9F0", width=8)
entry5.pack(side="left")
tk.Button(advanced_frame, text="x^y", command=lambda: calculate("power"), bg="#3B4252", fg="#E5E9F0").grid(row=1,
                                                                                                           column=3)

tk.Label(advanced_frame, text="Trigonometry:", bg="#2E3440", fg="#E5E9F0").grid(row=2, column=0)
entry6 = tk.Entry(advanced_frame, bg="#3B4252", fg="#E5E9F0", width=15)
entry6.grid(row=2, column=1)

trig_buttons = tk.Frame(advanced_frame, bg="#2E3440")
trig_buttons.grid(row=3, columnspan=4)

for i, (text, op) in enumerate([("sin", "sin"), ("cos", "cos"), ("tan", "tan"),
                                ("sin⁻¹", "asin"), ("cos⁻¹", "acos"), ("tan⁻¹", "atan")]):
    tk.Button(trig_buttons, text=text, command=lambda o=op: calculate(o),
              bg="#3B4252", fg="#E5E9F0", width=6).grid(row=0, column=i, padx=2)

result_frame = tk.Frame(basic_frame, bg="#2E3440")
result_frame.grid(row=3, columnspan=2)
tk.Label(result_frame, text="Result:", bg="#2E3440", fg="#E5E9F0").pack(side="left")
tk.Label(result_frame, textvariable=result, bg="#2E3440", fg="#88C0D0").pack(side="left")

history_frame = tk.LabelFrame(main_frame, text="History", bg="#2E3440", fg="#E5E9F0")
history_frame.grid(row=1, column=1, rowspan=2, padx=10)

history_listbox = tk.Listbox(history_frame, height=15, width=35, bg="#434C5E", fg="#E5E9F0")
history_listbox.pack(pady=5)

history_buttons = tk.Frame(history_frame, bg="#2E3440")
history_buttons.pack()
tk.Button(history_buttons, text="Clear History", command=clear_history, bg="#3B4252", fg="#E5E9F0").pack()

tk.Button(main_frame, text="Clear All", command=clear_all, bg="#3B4252", fg="#E5E9F0").grid(row=3, column=0, pady=10)

root.mainloop()