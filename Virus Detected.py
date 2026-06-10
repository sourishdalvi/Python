from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("200x200")
def msg():
    messagebox.showwarning("Virus Detected", "Your Computer is Infected with a Virus")
button=Button(root, text="Scan for virus", command=msg)
button.place(x=50, y=50)
root.mainloop()