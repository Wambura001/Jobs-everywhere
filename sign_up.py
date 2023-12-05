from tkinter import *
import sqlite3
import hashlib

def register_user():
    username = entry_username.get()
    password = entry_password.get()

    # Check if username or password is empty
    if not username or not password:
        label_result.config(text='Please enter both username and password')
        return

    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Initialize the database and register user
    try:
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS users(Id integer PRIMARY KEY AUTOINCREMENT,
                                                             Username TEXT NOT  NULL,
                                                             Password TEXT NOT NULL)''')
        cursor.execute('INSERT INTO users (username, password) VALUES (?,?)', (username, hashed_password))
        conn.commit()
        conn.close()
        label_result.config(text='Registration successful!')
    except Exception as e:
        label_result.config(text=f'Registration failed: {e}')

def on_close():
    window.destroy()

window = Tk()
window.title("Sign Up")
window.geometry('400x350')
window.config(bg='#9C9247')

# create labels and entries
label_username = Label(window, text="Username:", font=("Helvetica", 12))
entry_username = Entry(window)
label_password = Label(window, text="Password:", font=("Helvetica", 12))
entry_password = Entry(window, show='*')
button_submit = Button(window, text="Sign in", bg='blue', fg='white', command=register_user, width=15)
button_close = Button(window, text="Close", bg='red', fg='white', command=on_close, width=15)
label_result = Label(window, text='', fg='red')

# place the widgets in a grid format
label_username.grid(row=0, column=0, padx=10, pady=10, sticky='e')
entry_username.grid(row=0, column=1, padx=10, pady=10)
label_password.grid(row=1, column=0, padx=10, pady=10, sticky='e')
entry_password.grid(row=1, column=1, padx=10, pady=10)
button_submit.grid(row=2, column=0, padx=10, pady=10, columnspan=2)
button_close.grid(row=3, column=0, padx=10, pady=10, columnspan=2)
label_result.grid(row=4, column=0, columnspan=2)

window.mainloop()
