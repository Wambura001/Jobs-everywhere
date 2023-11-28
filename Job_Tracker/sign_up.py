from tkinter import *
# from PIL import Image,ImageTk


window = Tk()
window.title("Sign Up")
window.geometry('400x350')
window.config(bg='#9C9247 ')

#functions
def on_close():
    window.terminate()
# def submit():


#create labels and entries
label_username = Label(window,text="Username:",font=("Helvetica",12))
entry_username = Entry(window)
label_password = Label(window,text="Password:",font=("Helvetica",12))
entry_password = Entry(window,show='*')
button_submit = Button(window, text="Submit", font=("Helvetica", 14), bg=('blue'),fg=('white'))
button_close = Button(window, text="Close", font=("Helvetica", 14), bg=('red'), fg=('white'), command=on_close)

#place the widgets in a grid format
label_username.grid(row=0,column=0)
entry_username.grid(row=0, column=1)
label_password.grid(row=1,column=0)
entry_password.grid(row=1,column=1)
button_submit.grid(row=2,column=0)
button_close.grid(row=2,column=1)



window.mainloop()