# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:24:22 2023

@author: sirin
"""
from tkinter import *
# from PIL import Image,ImageTk


window = Tk()
window.title("Log in")
window.geometry('400x350')
window.config(bg='#479C80')


#create labels and entries
label_username = Label(window,text="Username:",font=("Helvetica",12))
entry_username = Entry(window)
label_password = Label(window,text="Password:",font=("Helvetica",12))
entry_password = Entry(window,show='*')
button_submit = Button(window, text="Submit", font=("Helvetica", 14), bg=('blue'),fg=('white'))
button_close = Button(window, text="Close", font=("Helvetica", 14), bg=('red'), fg=('white'))

#place the widgets in a grid format
label_username.grid(row=0,column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1,column=0)
entry_password.grid(row=1,column=1)
button_submit.grid(row=2,column=0)
button_close.grid(row=2,column=1)



window.mainloop()