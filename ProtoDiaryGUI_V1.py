# ProtoDiaryGUI-V1 - by Lee Gallagher

# This is a first prototype of what the UI/UX of my Python Diary application may look like.
# Initial goal is to simulate the "Main Menu" screen, however I will add more functionality where possible.

# (0) Imports

import tkinter as tk
from tkinter import *

# (1) Window Configuration

window = tk.Tk()

home_page = tk.Frame(window, bg="lightgreen")
new_entry_page = tk.Frame(window, bg="lightgreen")

home_page.tkraise() # loads home page when program is opened

home_page.pack(fill='both', expand=True)

window.geometry("900x600")
window.configure(bg="lightgreen")
window.title("Python Diary Application GUI Prototype V1")

# (2) Button Functions

def add_new_entry_page(): # calls "new entry page" from home
    home_page.pack_forget()
    new_entry_page.pack(fill='both', expand=True)
    new_entry_page.tkraise()

def home_button_from_new(): # calls "home page" from "new entry page"
    new_entry_page.pack_forget()
    home_page.pack(fill='both', expand=True)
    home_page.tkraise()

# ---------- HOME PAGE ---------- #

# (1) Grid Configuration

pg1rows = 6
pg1columns = 2

for i in range(pg1rows):
    home_page.grid_rowconfigure(i, weight=1)
for i in range(pg1columns):
    home_page.grid_columnconfigure(i, weight=1)

# (2) Main Menu

title_label = tk.Label(home_page, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

button_new = tk.Button(home_page, text="Add New Entry", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20), command=add_new_entry_page).grid(column=0, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_view = tk.Button(home_page, text="View Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=1, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_delete = tk.Button(home_page, text="Delete Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=0, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_help = tk.Button(home_page, text="Help & Readme Text", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=1, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(home_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=5, columnspan=2, sticky=NSEW, padx=5, pady=5)

# ---------- NEW ENTRY PAGE ---------- #

# (1) Grid Configuration

pg2rows = 10
pg2columns = 10

for i in range(pg2rows):
    new_entry_page.grid_rowconfigure(i, weight=1)
for i in range(pg2columns):
    new_entry_page.grid_columnconfigure(i, weight=1)

# (2) Page Contents

title_label = tk.Label(new_entry_page, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=10, sticky=NSEW, padx=5, pady=5)

entry_title_label = tk.Label(new_entry_page, text="Entry Title: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=1, columnspan=2, sticky=NSEW, padx=5, pady=5)

entry_date_label = tk.Label(new_entry_page, text="Entry Date: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=2, columnspan=2, sticky=NSEW, padx=5, pady=5)

entry_article_label = tk.Label(new_entry_page, text="Entry Article: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=3, columnspan=2, rowspan=5, sticky=NSEW, padx=5, pady=5)

enter_title_textbox = tk.Entry(new_entry_page, fg="green", bg="black", font=("Arial", 14)).grid(column=2, row=1, columnspan=8, sticky=NSEW, padx=5, pady=5)

enter_date_textbox = tk.Entry(new_entry_page, fg="green", bg="black", font=("Arial", 14)).grid(column=2, row=2, columnspan=8, sticky=NSEW, padx=5, pady=5)

enter_article_textbox = tk.Entry(new_entry_page, fg="green", bg="black", font=("Arial", 14)).grid(column=2, row=3, columnspan=8, rowspan=5, sticky=NSEW, padx=5, pady=5)

home_button = tk.Button(new_entry_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_new).grid(column=0, row=8, columnspan=10, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(new_entry_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=9, columnspan=10, sticky=NSEW, padx=5, pady=5)

window.mainloop()

