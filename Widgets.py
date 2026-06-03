from tkinter import*
from datetime import date
root=Tk()
root.title("Widgets")   
root.geometry("400x300")
lbl=Label(root,text="Hello",fg="white",bg="#072F5F",height=1,width=300)
name_lbl=Label(root,text="Full Name",bg="#3695D3",)
name_entry=Entry()
def display():
    name=name_entry.get()
    global message
    message="Welcome to the Application \nToday's date is "
    greet="Hello"+name+"\n"
    text_box.insert(END,greet)
    text_box.insert(END,message)
    text_box.insert(END,date.today())
text_box=Text(root,height=3)
btn=Button(root,text="Begin",command=display,height=1,bg="#072F5F",fg="white")
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()
root.mainloop()
