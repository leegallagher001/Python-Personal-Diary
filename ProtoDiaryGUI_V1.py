# ProtoDiaryGUI-V1 - by Lee Gallagher

# This is a first prototype of what the UI/UX of my Python Diary application may look like.
# Initial goal is to simulate the "Main Menu" screen, however I will add more functionality where possible.

# (0.0) Imports

from ast import Lambda
import tkinter as tk
from tkinter import *
import json

diary_entries_file = "pdgui-v1-entries.json"

# (1.0) Window Configuration

window = tk.Tk()

home_page = tk.Frame(window, bg="lightgreen") # Page 1
new_entry_page = tk.Frame(window, bg="lightgreen") # Page 2
view_saved_entries_page = tk.Frame(window, bg="lightgreen") # Page 3
read_saved_entry_page = tk.Frame(window, bg="lightgreen") # Page 4

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

def access_current_entries_page(): # calls "read saved entries page" from home
    home_page.pack_forget()
    view_saved_entries_page.pack(fill='both', expand=True)
    view_saved_entries_page.tkraise()
    display_saved_entries()

# -- NEW ENTRY PAGE -- #

def home_button_from_new(): # calls "home page" from "new entry page"
    new_entry_page.pack_forget()
    home_page.pack(fill='both', expand=True)
    home_page.tkraise()

def text_entry_to_file(): # saves the entered text to a JSON file, then deletes the text entered into the text widgets
    
    diary_entry = {}

    diary_entry["title"] = enter_title_textbox.get("1.0",'end-1c')
    diary_entry["date"] = enter_date_textbox.get("1.0",'end-1c')
    diary_entry["main"] = enter_article_textbox.get("1.0",'end-1c')

    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

    diary_entries.append(diary_entry)

    with open (diary_entries_file, 'w') as f:
        json.dump(diary_entries, f, indent=4)

    enter_title_textbox.delete("1.0", "end")
    enter_date_textbox.delete("1.0", "end")
    enter_article_textbox.delete("1.0", "end")

# -- VIEW SAVED ENTRIES PAGE -- #

def home_button_from_saved(): # calls "home page" from "view saved entries page"
    view_saved_entries_page.pack_forget()
    home_page.pack(fill='both', expand=True)
    home_page.tkraise()

def read_article():
    view_saved_entries_page.pack_forget()
    read_saved_entry_page.pack(fill='both', expand=True)
    read_saved_entry_page.tkraise()
    load_article()

def display_saved_entries(): # displays buttons that allow user to select an entry by title
    with open (diary_entries_file, 'r') as f: # opens the JSON file and program reads it
        diary_entries = json.load(f)

    for i, diary_entry in enumerate(diary_entries, start=1): # generates a button for each diary entry
        tk.Button(entries_container, bg="black", fg="lightgreen", font=("Arial", 14), text=f"{i}. {diary_entry['title']} - {diary_entry['date']}", command=read_article).grid(row=i-1, columnspan=1, column=0, sticky=NSEW, padx=5, pady=5)

# -- READ SAVED ENTRY PAGE -- #

def load_article():
    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

    for diary_entry in diary_entries:
        if tk.Button(text = f"{i}. {diary_entry['title']}") == diary_entry['title']:
            entry_title.config(text = diary_entry['title'])
            entry_date.config(text = diary_entry['date'])
            entry_main.config(text = diary_entry['main'])

def home_button_from_read(): # calls "home page" from "reading entry" page
    read_saved_entry_page.pack_forget()
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

title_label = tk.Label(home_page, text="[ PYTHON TEXT DIARY ]", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

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

title_label = tk.Label(new_entry_page, text="[ PYTHON TEXT DIARY ]", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=10, sticky=NSEW, padx=5, pady=5)

entry_title_label = tk.Label(new_entry_page, text="Entry Title: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=1, columnspan=2, sticky=NSEW, padx=5, pady=5)

entry_date_label = tk.Label(new_entry_page, text="Entry Date: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=2, columnspan=2, sticky=NSEW, padx=5, pady=5)

entry_article_label = tk.Label(new_entry_page, text="Entry Article: ", bg="green", fg="black", font=("Arial", 14)).grid(column=0, row=3, columnspan=2, rowspan=5, sticky=NSEW, padx=5, pady=5)

# with the elements subject to the ".get()" method, grid needs to be declared seperately
# as otherwise the widget is assigned a class of "None" and is inaccessible via ".get()" method

enter_title_textbox = tk.Text(new_entry_page, fg="lightgreen", bg="black", font=("Arial", 14), width=45, height=1)
enter_title_textbox.grid(column=2, row=1, columnspan=8, sticky=NSEW, padx=5, pady=5)                          

enter_date_textbox = tk.Text(new_entry_page, fg="lightgreen", bg="black", font=("Arial", 14), width=45, height=1)
enter_date_textbox.grid(column=2, row=2, columnspan=8, sticky=NSEW, padx=5, pady=5)

enter_article_textbox = tk.Text(new_entry_page, fg="lightgreen", bg="black", font=("Arial", 14),width=45, height=10)
enter_article_textbox.grid(column=2, row=3, columnspan=8, rowspan=5, sticky=NSEW, padx=5, pady=5)

home_button = tk.Button(new_entry_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_new).grid(column=0, row=8, columnspan=5, sticky=NSEW, padx=5, pady=5)

submit_button = tk.Button(new_entry_page, text="SUBMIT", bg="black", fg="yellow", font=("Arial", 16), command=text_entry_to_file)
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

entries_container = tk.Frame(view_saved_entries_page, bg="green") # container that stores the buttons for the different saved entries
entries_container.grid(column=0, row=1, columnspan=10, rowspan=7, sticky=NSEW, padx=5, pady=5) # configured as it's own grid

containerRows = 10
containerColumns = 1

for i in range(containerRows):
    entries_container.grid_rowconfigure(i, weight=1)
for i in range(containerColumns):
    entries_container.grid_columnconfigure(i, weight=1)

home_button = tk.Button(view_saved_entries_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_saved).grid(column=0, row=8, columnspan=10, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(view_saved_entries_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=9, columnspan=10, sticky=NSEW, padx=5, pady=5)

# ---------- Page 4 - READ SAVED ENTRY PAGE ---------- #

pg4rows = 10
pg4columns = 10

# (1) Grid Configuration

for i in range(pg4rows):
    read_saved_entry_page.grid_rowconfigure(i, weight=1)
for i in range(pg4columns):
    read_saved_entry_page.grid_columnconfigure(i, weight=1)

# (2) Page Contents

title_label = tk.Label(read_saved_entry_page, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=10, sticky=NSEW, padx=5, pady=5)

diary_entry_container = tk.Frame(read_saved_entry_page, bg="black") # where the diary article is read from
diary_entry_container.grid(column=0, row=1, columnspan=10, rowspan=7, sticky=NSEW, padx=5, pady=5)

diaryRows = 10
diaryColumns = 1

for i in range(diaryRows):
    diary_entry_container.grid_rowconfigure(i, weight=1)
for i in range(diaryColumns):
    diary_entry_container.grid_columnconfigure(i, weight=1)

entry_title = tk.Label(diary_entry_container, fg="lightgreen", bg="black", font=("Arial", 14))
entry_title.grid(column=0, row=0, columnspan=1, sticky=NSEW, padx=5, pady=5)

entry_date = tk.Label(diary_entry_container, fg="lightgreen", bg="black", font=("Arial", 14))
entry_date.grid(column=0, row=1, columnspan=1, sticky=NSEW, padx=5, pady=5)

entry_main = tk.Label(diary_entry_container, fg="lightgreen", bg="black", font=("Arial", 14))
entry_main.grid(column=0, row=2, columnspan=1, rowspan=8, sticky=NSEW, padx=5, pady=5)

home_button = tk.Button(read_saved_entry_page, text="HOME", bg="black", fg="lightgreen", font=("Arial", 16), command=home_button_from_read).grid(column=0, row=8, columnspan=10, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(read_saved_entry_page, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=9, columnspan=10, sticky=NSEW, padx=5, pady=5)
    
# (4.0) Mainloop

window.mainloop()


