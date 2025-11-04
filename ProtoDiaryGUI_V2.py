# ProtoDiaryGUI-V2 - by Lee Gallagher

# A second prototype of a Python Text Diary incorporating a Tkinter GUI, the goal for this will be to incorporate some of the features
# that I planned for the first one but in a much cleaner and more thoughtful way (the code for GUI-V1 was messy and I have a greater
# understanding of how to structure a Tkinter program now). This prototype will also incorporate a clean-sheet design with more vibrant
# colours that matches a nostalgic, early 2000's Window XP-esque or "Frutiger Aero" theme.

# (0) Imports

import tkinter as tk
from tkinter import *
import json

diary_entries = "pdgui-v2-entries.json"

window = tk.Tk()
window.geometry("900x600")

# ---------- PAGES ---------- #

def new_entry(): # Page 2 - Add New Entry Page

    window.title("aero Text Diary - Add New Entry")

    # Grid Configuration

    new_entry_page = tk.Frame(window, bg="#81C046")

    pg2rows = 10
    pg2columns = 10

    for i in range(pg2rows):
        new_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg2columns):
        new_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    new_title_label = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter title: ") # title section
    new_title_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_title = tk.Entry(new_entry_page, bg="lightblue", font="Helvitica 18")
    new_entry_title.grid(row=1, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_date_label = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter date: ") # date section
    new_date_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_date = tk.Entry(new_entry_page, bg="lightblue", font="Helvitica 18")
    new_entry_date.grid(row=2, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_main_label = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter article: ") # main article section
    new_main_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_main = tk.Text(new_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=10)
    new_entry_main.grid(row=3, rowspan=5, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(new_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    submit_button = tk.Button(new_entry_page, bg="#81C046", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="submit entry") # submit button
    submit_button.grid(row=8, column=5, columnspan=5, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack New Entry Page

    new_entry_page.pack(fill='both', expand=True)

def view_entries(): # Page 3 - View Saved Entries Page

    window.title("aero Text Diary - View Saved Entries")

    # Grid Configuration

    view_entries_page = tk.Frame(window, bg="#81C046")

    pg3rows = 10
    pg3columns = 10

    for i in range(pg3rows):
        view_entries_page.grid_rowconfigure(i, weight=1)
    for i in range(pg3columns):
        view_entries_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(view_entries_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    saved_entries = tk.Frame(view_entries_page, bg="#81C046") # this frame contains the saved entries that will be loaded from the JSON file
    saved_entries.grid(row=1, rowspan=7, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(view_entries_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(view_entries_page)) # home button
    home_button.grid(row=8, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(view_entries_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack View Saved Entries Page

    view_entries_page.pack(fill="both", expand=True)

def delete_entry():

    window.title("aero Text Diary - Delete Entry")

    # Grid Configuration

    delete_entry_page = tk.Frame(window, bg="#81C046")

    pg4rows = 10
    pg4columns = 10

    for i in range(pg4rows):
        delete_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg4columns):
        delete_entry_page.grid_columnconfigure(i, weight=1)

# ---------- HOME PAGE BUTTON FUNCTIONS ---------- #

def visit_new_entry(home_page):

    home_page.destroy()
    new_entry()

def visit_saved_entries(home_page):

    home_page.destroy()
    view_entries()

# ---------- HOME BUTTON(S) ---------- #

def home(x):

    x.destroy()
    main()

# ---------- PROGRAM START ---------- #

def main(): # Page 1 - Home Page

    window.title("aero Text Diary - Home")

    # Grid Configuration

    home_page = tk.Frame(window, bg="#81C046") # Windows XP-style green

    pg1rows = 10
    pg1columns = 10

    for i in range(pg1rows):
        home_page.grid_rowconfigure(i, weight=1)
    for i in range(pg1columns):
        home_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(home_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Buttons

    new_entry_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="add new entry", command=lambda: visit_new_entry(home_page))
    new_entry_page.grid(row=1, rowspan=4, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    view_entries_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="view current entries", command=lambda: visit_saved_entries(home_page))
    view_entries_page.grid(row=1, rowspan=4, column=5, columnspan=5, padx=10, pady=10, sticky="nsew")

    delete_entry_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="delete saved entry")
    delete_entry_page.grid(row=5, rowspan=4, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    help_readme_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="aero text diary")
    help_readme_page.grid(row=5, rowspan=4, column=5, columnspan=5, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(home_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Home Page

    home_page.pack(fill='both', expand=True)

main()

window.mainloop()
