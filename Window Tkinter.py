from cProfile import label
from tkinter import *
root=Tk()
root.geometry("400x300")
root.title("Main")
def topwin():
    top=Toplevel()
    top.geometry("180x100")
    top.title("Top Window")
    Label(top,text="This is a Top Window").pack()
    top.mainloop()
l=Label(root,text="This is Main Window")
btn=Button(root,text="Open Top Window",command=topwin)
l.pack()
btn.pack()
root.mainloop()

