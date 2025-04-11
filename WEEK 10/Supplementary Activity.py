import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror

window = tk.Tk()
window.title('Birth Date Selector')
window.geometry("600x250")
window.configure(bg='#2d2d2d')

ttk.Label(window, text="CHOOSE YOUR BIRTH DATE",
          background='#6a0dad', foreground="white",
          font=("Poppins", 15)).place(x=175, y=20)

ttk.Label(window, text="Select Month:",
          font=("Poppins", 12), background='#2d2d2d', foreground="white").place(x=10, y=135)
ttk.Label(window, text="Select the day:",
          font=("Poppins", 12), background='#2d2d2d', foreground="white").place(x=10, y=65)
ttk.Label(window, text="Year:",
          font=("Poppins", 12), background='#2d2d2d', foreground="white").place(x=10, y=100)

m = tk.StringVar()
day = ttk.Combobox(window, width=30, textvariable=m)
day['values'] = tuple(str(i) for i in range(1, 32))
day.place(x=250, y=67)
day.configure(background='#3d3d3d', foreground='white')
day.current()

n = tk.StringVar()
year = ttk.Combobox(window, width=30, textvariable=n)
year['values'] = tuple(str(i) for i in range(2025, 1899, -1))
year.place(x=250, y=100)
year.configure(background='#3d3d3d', foreground='white')
year.current()

o = tk.StringVar()
month = ttk.Combobox(window, width=30, textvariable=o)
month['values'] = ('January', 'February', 'March', 'April', 'May', 'June',
                   'July', 'August', 'September', 'October', 'November', 'December')
month.place(x=250, y=135)
month.configure(background='#3d3d3d', foreground='white')
month.current()

def validate_and_submit():
    if not all([m.get(), n.get(), o.get()]):
        showerror("Error", "Please fill in all fields!")
        return
    showinfo(
        title="Selection",
        message=f'You Selected: {o.get()} {m.get()}, {n.get()}')

ttk.Button(window, text="Submit", command=validate_and_submit,
           style='Accent.TButton').place(x=250, y=200)

style = ttk.Style()
style.configure('Accent.TButton', background='#6a0dad', foreground='white', font=('Poppins', 10))

window.mainloop()