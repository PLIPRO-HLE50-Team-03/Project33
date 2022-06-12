from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os



root = Tk()
root.title("Tennis Ladder")
root.geometry('1024x768')
root.resizable(0,0)
bg = Image.open('background.png')
bg.thumbnail((1024, 768))
width, height = bg.size
bg = ImageTk.PhotoImage(bg)
root.iconbitmap('icon.ico')

def new():
    if user_entry.get() == "":
        messagebox.showinfo("Tennis Ladder", "Παρακαλώ δώστε όνομα χρήστη")
    elif password_entry.get() == "":
        messagebox.showinfo("Tennis Ladder", "Παρακαλώ δώστε κώδικο")
    elif user_entry.get() == "" and password_entry.get() == "":
        messagebox.showinfo("Tennis Ladder", "Παρακαλώ δώστε όνομα χρήστη και κώδικο")
    elif user_entry.get() == "admin" and password_entry.get() == "123":
        root.withdraw()
        paswd.set("")
        os.system('python Ladder.py')
        def home_page():
            new_window.withdraw()
            root.deiconify()
    else:
        messagebox.showinfo("Tennis Ladder", "Λάθος στοιχεία εισόδου")
        paswd.set("")


canvas = Canvas(root, width=width, height=height, bd=0, highlightthickness=5)
canvas.pack(fill=BOTH, expand=True)
canvas.create_image(0, 0, image=bg, anchor='nw')
canvas.create_text(400, 70, text="Welcome to Tennis Ladder", font=('Tahoma 30 bold'), fill='#922B21')
canvas.create_text(220, 145, text="Χρήστης", font=('Tahoma 18 bold'), fill='#922B21')
canvas.create_text(220, 215, text="Κωδικός", font=('Tahoma 18 bold'), fill='#922B21')
user_entry = Entry(root, font=("Tahoma 18 bold"))
user_entry.focus()
canvas.create_window(290, 130, anchor="nw", window=user_entry)
paswd = StringVar()
password_entry = Entry(root, textvar=paswd, font=("Ariel 18 bold"), show="*")
canvas.create_window(290, 200, anchor="nw", window=password_entry)
login = Button(root, text="Έισοδος", font=("Tahoma 22 bold"),
            width=8, bg="grey", fg='#922B21', relief=RAISED, cursor="hand2", command=new,borderwidth=2).place(x=290, y=250)
canvas.create_window(290, 290, anchor="nw", window=login)
root.mainloop()