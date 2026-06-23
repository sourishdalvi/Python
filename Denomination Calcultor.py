from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("Denomination Calculator")
root.geometry("400x400")
def calculate():
    top=Toplevel(root)
    top.title("Denomination Calculator")
    top.geometry("300x250")
    Label(top,text="Enter the amount:").pack()
    amount_entry=Entry(top)
    amount_entry.pack()
    e1, e2, e3 = Entry(top), Entry(top), Entry(top)
    def count():
        a=int(amount_entry.get())
        notes_2000=a//2000
        a=a%2000
        notes_500=a//500
        a=a%500
        notes_100=a//100
        a=a%100
        e1.delete(0, END)
        e2.delete(0, END)
        e3.delete(0, END)
        e1.insert(0, str(notes_2000))
        e2.insert(0, str(notes_500))
        e3.insert(0, str(notes_100))
    Button(top, text="Calculate", command=count).pack()
    Label(top, text="2000 Notes:").pack()
    e1.pack()
    Label(top, text="500 Notes:").pack()
    e2.pack()
    Label(top, text="100 Notes:").pack()
    e3.pack()
Button(
            root,
            text="start",
            command=lambda:(
                messagebox.showinfo("Alert", "Calculate count"),
                calculate()
            )
).pack(pady=100)
root.mainloop()
        
        

