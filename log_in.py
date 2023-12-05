# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 00:24:22 2023

@author: sirin
"""
from tkinter import *
from tkinter import messagebox
import hashlib
import sqlite3
from index import MainPage  # Make sure you have index.py with MainPage class

def authenticate_user():
    entered_username = entry_username.get()
    entered_password = entry_password.get()
    hashed_password = hashlib.sha256(entered_password.encode()).hexdigest()

    # Connect to database
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Check if username and password match
    cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (entered_username, hashed_password))
    user_data = cursor.fetchone()

    conn.close()

    if user_data:
        label_result.config(text="Login successful")
        window.destroy()
        index = MainPage(username=entered_username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")
        label_result.config(text="Login failed. Please check your username and password.")

def toggle_password_visibility():
    # Toggle password visibility
    current_state = password_visibility.get()
    entry_password.config(show='' if current_state.get() else '*')
    
def on_close():
    window.destroy()

# Tkinter
window = Tk()
window.title("Log in")
window.geometry('400x350')
window.config(bg='#479C80')

# Create labels and entries
label_username = Label(window, text="Username:", font=("Helvetica", 12))
entry_username = Entry(window)
label_password = Label(window, text="Password:", font=("Helvetica", 12))
entry_password = Entry(window, show='*')
password_visibility = IntVar()
check_show_password = Checkbutton(window, text="Show Password", variable=password_visibility, command=toggle_password_visibility)
button_log_in = Button(window, text="Log in", bg='blue', fg='white', command=authenticate_user)
button_close = Button(window, text="Close", bg='red', fg='white', command=on_close)
label_result = Label(window, text='', fg='green')

# Place the widgets in a grid format
label_username.grid(row=0, column=0, pady=10, sticky='e')
entry_username.grid(row=0, column=1, pady=10)
label_password.grid(row=1, column=0, pady=10, sticky='e')
entry_password.grid(row=1, column=1, pady=10)
check_show_password.grid(row=2, columnspan=2, pady=5)
button_log_in.grid(row=3, column=0, pady=10)
button_close.grid(row=3, column=1, pady=10)
label_result.grid(row=4, column=0, columnspan=2, pady=10)

window.mainloop()