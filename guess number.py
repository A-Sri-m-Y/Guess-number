from tkinter import*
from tkinter import messagebox
import random

def number():
    global x
    global attempts
    number = int(e1.get())
    l3.config(text = attempts)

    if (number < x):

        messagebox.showinfo("message", "Too small try again !")
        attempts = attempts + 1

    elif (number > x):
        messagebox.showinfo ("message" , "To big try again !")
        attempts = attempts + 1

    else:
        messagebox.showinfo("message","Congratulations you won !")
        

root = Tk()
root.title("Welcome to Guess the Number")
root.config(bg="plum")
root.geometry("600x400+200+100")
global x
global attempts
attempts = 0
x = random.randrange(1, 100)
    
l0 = Label(root, text="Guess game", font=("Arial", 16), width="18", bg="black", fg="white")
l0.place(x=270, y=10)
 
l1 = Label(root, text="Guess the number", font=("Arial", 16), width="18", bg="red", fg="white")
l1.place(x=150, y=220)

l2=Label(root,text="No Of Attempts Are:",font=("areal",16),width="18",bg="teal",fg="black")
l2.place(x=150,y=140)

l3 = Label(root, text="", width="8", font=("Arial", 12),bg="purple",fg="white")
l3.place(x=425, y=140)

e1 =Entry(root, text="", width="8", font=("Arial", 12))
e1.place(x=420, y=225)

b1 = Button(root, text="Check", font=("Arial", 18), width="7", bg="indigo", fg="white", command=number)
b1.place(x=320, y=340)


root.mainloop()






