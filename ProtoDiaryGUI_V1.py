# ProtoDiaryGUI-V1 - by Lee Gallagher

# This is a first prototype of what the UI/UX of my Python Diary application may look like.
# Initial goal is to simulate the "Main Menu" screen, however I will add more functionality where possible.

# (0.0) Imports

from ast import Lambda
import tkinter as tk
from tkinter import *
import json

diary_entries = "pdgui-v1-entries.json"

# (1.0) Window Configuration

window = tk.Tk()

home_page = tk.Frame(window, bg="lightgreen")
new_entry_page = tk.Frame(window, bg="lightgreen")
view_saved_entries_page = tk.Frame(window, bg="lightgreen")

home_page.tkraise() # loads home page when program is opened

home_page.pack(fill='both', expand=True)

window.geometry("900x600")
window.configure(bg="lightgreen")
window.title("Python Diary Application GUI Prototype V1")

# (2.0) Button Functions

# -- HOME PAGE -- #

def add_new_entry_page(): # calls "new entry page" from home
    home_page.pack_forget()
    new_entry_page.pack(fill='both', expand=True)
    new_entry_page.tkraise()

def access_current_entries_page():
    home_page.pack_forget()
    view_saved_entries_page.pack(fill='both', expand=True)
    view_saved_entries_page.tkraise()

# -- NEW ENTRY PAGE -- #

def home_button_from_new(): # calls "home page" from "new entry page"
    new_entry_page.pack_forget()
    home_page.pack(fill='both', expand=True)
    home_page.tkraise()

def text_entry_to_txt():
    title = enter_title_textbox.get("1.0",'end-1c')
    date = enter_date_textbox.get("1.0",'end-1c')
    main = enter_article_textbox.get("1.0",'end-1c')

    with open(f"{title}.txt", "w") as f:
        f.write("-" * 50)
        f.write("\n")
        f.write(title)
        f.write("\n")
        f.write("-" * 50)
        f.write("\n")
        f.write(date)
        f.write("\n")
        f.write("-" * 50)
        f.write("\n")
        f.write(main)
        f.write("\n")

    enter_title_textbox.delete("1.0", "end")
    enter_date_textbox.delete("1.0", "end")
    enter_article_textbox.delete("1.0", "end")

# -- VIEW SAVED ENTRIES PAGE

def home_button_from_saved(): # calls "home page" from "view saved entries page"
    view_saved_entries_page.pack_forget()
    home_page.pack(fill='both', expand=True)
    home_page.tkraise()

# (3.0) Page Layouts

# ---------- Page 1 - HOME PAGE ---------- #

# (1) Grid Configuration

pg1rows = 6
pg1columns = 2

for i in range(pg1rows):
    home_page.grid_rowconfigure(i, weight=1)
for i in range(pg1columns):
    home_page.grid_columnconfigure(i, weight=1)

# (2) Page Contents (Main Menu)

title_label = tk.Label(home_page, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

button_new = tk.Button(home_page, text="Add New Entry", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20), command=add_new_entry_page).grid(column=0, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_view = tk.Button(home_page, text="View Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20), command=access_current_entries_page).grid(column=1, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_delete = tk.Button(home_page, text="Delete Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=0, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_help = tk.Button(home_page, text="Help & Readme Text", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=1, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(home_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=5, columnspan=2, sticky=NSEW, padx=5, pady=5)

# ---------- Page 2 - NEW ENTRY PAGE ---------- #

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

# with the elements subject to the ".get()" method, grid needs to be declared seperately
# as otherwise the widget is assigned a class of "None" and is inaccessible via ".get()" method

enter_title_textbox = tk.Text(new_entry_page, fg="green", bg="black", font=("Arial", 14), width=45, height=1)
enter_title_textbox.grid(column=2, row=1, columnspan=8, sticky=NSEW, padx=5, pady=5)                          

enter_date_textbox = tk.Text(new_entry_page, fg="green", bg="black", font=("Arial", 14), width=45, height=1)
enter_date_textbox.grid(column=2, row=2, columnspan=8, sticky=NSEW, padx=5, pady=5)

enter_article_textbox = tk.Text(new_entry_page, fg="green", bg="black", font=("Arial", 14),width=45, height=10)
enter_article_textbox.grid(column=2, row=3, columnspan=8, rowspan=5, sticky=NSEW, padx=5, pady=5)

home_button = tk.Button(new_entry_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_new).grid(column=0, row=8, columnspan=5, sticky=NSEW, padx=5, pady=5)

submit_button = tk.Button(new_entry_page, text="SUBMIT", bg="black", fg="yellow", font=("Arial", 16), command=text_entry_to_txt)
submit_button.grid(column=5, row=8, columnspan=5, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(new_entry_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=9, columnspan=10, sticky=NSEW, padx=5, pady=5)

# ---------- Page 3 - VIEW SAVED ENTRIES PAGE ---------- #

# (1) Grid Configuration

pg3rows = 10
pg3columns = 10

for i in range(pg3rows):
    view_saved_entries_page.grid_rowconfigure(i, weight=1)
for i in range(pg3columns):
    view_saved_entries_page.grid_columnconfigure(i, weight=1)

# (2) Page Contents

title_label = tk.Label(view_saved_entries_page, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=10, sticky=NSEW, padx=5, pady=5)

entries_container = tk.Frame(view_saved_entries_page, bg="green").grid(column=0, row=1, columnspan=10, rowspan=7, sticky=NSEW, padx=5, pady=5)

home_button = tk.Button(view_saved_entries_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_saved).grid(column=0, row=8, columnspan=10, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(view_saved_entries_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=9, columnspan=10, sticky=NSEW, padx=5, pady=5)

# (4.0) Mainloop

window.mainloop()

