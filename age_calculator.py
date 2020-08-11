"""
Created by : R.Lokesh

Project : 1

Name : Age Calculator

"""

# Importing Tkinter module

from tkinter import *

import datetime

# Setting gui main window

root = Tk()

# Adding Caption

root.title("Age Calculator")

# Setting window size 

root.geometry("400x350")

# Adding widgets

label_title = Label(root,text =" AGE CALCULATOR  ",font=('arial',20,"bold"),bg="skyblue",fg="white",width=22)
label_title.grid(row=0,column=0,padx=10,pady=5,columnspan=2)


label_name = Label(root,text ="NAME :",font=('arial',12,"bold"),bg="skyblue",fg="white",width=15)
label_name.grid(row=1,column=0,padx=10,pady=20)

label_year = Label(root,text ="YEAR :",font=('arial',12,"bold"),bg="skyblue",fg="white",width=15)
label_year.grid(row=2,column=0,padx=10,pady=20)

entry_name = Entry(root,width=30)
entry_name.grid(row=1,column=1)

entry_year = Entry(root,width=30)
entry_year.grid(row=2,column=1)

label_age = Label(root,text ="AGE  :",font=('arial',12,"bold"),bg="skyblue",fg="white",width=15)
label_age.grid(row=3,column=0,padx=10,pady=20)

entry_age = Entry(root,width=30,state=DISABLED
                  )
entry_age.grid(row=3,column=1)

# Functions

def clear():
    entry_name.delete(0,END)
    entry_year.delete(0,END)
    entry_age.delete(0,END)
    
    entry_age.config(state=DISABLED)

def calculate():
    entry_age.config(state=NORMAL)
    year_birth = int(entry_year.get())
    year_now = int(datetime.datetime.now().year)
    age = year_now - year_birth
    entry_age.insert(0,age)

button_calculate = Button(root,text ="CALCULATE",font=('arial',12,"bold"),bg="skyblue",fg="white",width=15,relief=GROOVE,command=calculate)
button_calculate.grid(row=4,column=0,pady=40)

button_clear = Button(root,text ="CLEAR",font=('arial',12,"bold"),bg="skyblue",fg="white",width=15,relief=GROOVE,command=clear)
button_clear.grid(row=4,column=1,pady=10)

# Creating Mainloop

root.mainloop()
