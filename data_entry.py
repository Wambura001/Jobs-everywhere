import tkinter as tk
from tkcalendar import DateEntry
import sqlite3

def apply():
    # Get values from entries
    first_name = entry_firstname.get()
    sir_name = entry_sirname.get()
    date_of_birth = entry_date_of_birth.get()
    phone_number = entry_phone_number.get()
    country_val = country.get()
    gender_val = gender_var.get()

    # Insert data into SQLite database
    conn = sqlite3.connect("application_data.db")
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS applications "
                   "(id INTEGER PRIMARY KEY, first_name TEXT, sir_name TEXT, "
                   "date_of_birth TEXT, phone_number TEXT, country TEXT, gender TEXT)")
    cursor.execute("INSERT INTO applications (first_name, sir_name, date_of_birth, "
                   "phone_number, country, gender) VALUES (?, ?, ?, ?, ?, ?)",
                   (first_name, sir_name, date_of_birth, phone_number, country_val, gender_val))
    conn.commit()
    conn.close()

    # Clear the entries
    entry_firstname.delete(0, tk.END)
    entry_sirname.delete(0, tk.END)
    entry_date_of_birth.delete(0, tk.END)
    entry_phone_number.delete(0, tk.END)

def pick_date():
    # Open the calendar to pick a date
    cal.place(x=window.winfo_x() + entry_date_of_birth.winfo_x(),
              y=window.winfo_y() + entry_date_of_birth.winfo_y() + entry_date_of_birth.winfo_height())

def close_calendar():
    cal.place_forget()

def close():
    window.destroy()

# GUI
window = tk.Tk()
window.title("Data Entry")
window.geometry('400x400')
window.config(bg='#47719C')

# Create entries and labels
label_form = tk.Label(window, text='Fill the form below', font=('Helvetica', 14))
label_firstname = tk.Label(window, text="First name")
entry_firstname = tk.Entry(window)
label_sirname = tk.Label(window, text="Sirname")
entry_sirname = tk.Entry(window)
label_date_of_birth = tk.Label(window, text="Date of birth")
entry_date_of_birth = tk.Entry(window)  # Placeholder for selected date
label_phone_number = tk.Label(window, text="Phone number")
entry_phone_number = tk.Entry(window)
label_country = tk.Label(window, text="Country")
country_values = ['Country1', 'Country2', 'Country3']
country = tk.StringVar(window)
country.set(country_values[0])
dropdown_country = tk.OptionMenu(window, country, *country_values)
label_gender = tk.Label(window, text="Gender")
gender_var = tk.StringVar(window)
gender_var.set("Male")
radio_male = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
radio_female = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")

# Calendar widget
cal = DateEntry(window, width=12, background='darkblue', foreground='white', borderwidth=2)

# Buttons
button_pick_date = tk.Button(window, text='Pick Date', command=pick_date, bg='#1976D2', fg='white')
button_apply = tk.Button(window, text='Apply', command=apply, bg='#4CAF50', fg='white')
button_close = tk.Button(window, text='Close', command=close, bg='#e53935', fg='white')

# Position entries and labels
label_form.grid(row=0, column=0, columnspan=3, pady=10)
label_firstname.grid(row=1, column=0, sticky='e', padx=10, pady=5)
entry_firstname.grid(row=1, column=1, columnspan=2, padx=10, pady=5)
label_sirname.grid(row=2, column=0, sticky='e', padx=10, pady=5)
entry_sirname.grid(row=2, column=1, columnspan=2, padx=10, pady=5)
label_date_of_birth.grid(row=3, column=0, sticky='e', padx=10, pady=5)
entry_date_of_birth.grid(row=3, column=1, padx=10, pady=5)
button_pick_date.grid(row=3, column=2, padx=10, pady=5)
label_phone_number.grid(row=4, column=0, sticky='e', padx=10, pady=5)
entry_phone_number.grid(row=4, column=1, columnspan=2, padx=10, pady=5)
label_country.grid(row=5, column=0, sticky='e', padx=10, pady=5)
dropdown_country.grid(row=5, column=1, columnspan=2, padx=10, pady=5)
label_gender.grid(row=6, column=0, sticky='e', padx=10, pady=5)
radio_male.grid(row=6, column=1, pady=5)
radio_female.grid(row=6, column=2, pady=5)
button_apply.grid(row=7, column=0, pady=10)
button_close.grid(row=7, column=1, pady=10)

# Event handling for closing calendar
cal.bind("<FocusOut>", lambda event: close_calendar())

window.mainloop()