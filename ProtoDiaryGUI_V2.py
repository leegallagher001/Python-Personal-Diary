# ProtoDiaryGUI-V2 - by Lee Gallagher

# A second prototype of a Python Text Diary incorporating a Tkinter GUI, the goal for this will be to incorporate some of the features
# that I planned for the first one but in a much cleaner and more thoughtful way (the code for GUI-V1 was messy and I have a greater
# understanding of how to structure a Tkinter program now). This prototype will also incorporate a clean-sheet design with more vibrant
# colours that matches a nostalgic, early 2000's Window XP-esque or "Frutiger Aero" theme.

# (0) Imports

from datetime import date
import tkinter as tk
from tkinter import *
import json
from turtle import title

diary_entries_file = "pdgui-v2-entries.json"

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
    new_entry_title = tk.Text(new_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=1)
    new_entry_title.grid(row=1, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_date_label = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter date: ") # date section
    new_date_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_date = tk.Text(new_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=1)
    new_entry_date.grid(row=2, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_main_label = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter article: ") # main article section
    new_main_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_main = tk.Text(new_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=10)
    new_entry_main.grid(row=3, rowspan=5, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(new_entry_page, bg="#81C046", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(new_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    submit_button = tk.Button(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="submit entry", command=lambda: save_new_entry(new_entry_title, new_entry_date, new_entry_main)) # submit button
    submit_button.grid(row=8, column=5, columnspan=5, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(new_entry_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack New Entry Page

    new_entry_page.pack(fill='both', expand=True)

def view_entries(): # Page 3 - View Saved Entries Page

    window.title("aero Text Diary - View Saved Entries")

    # Grid Configuration

    global view_entries_page
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

    entries_rows = 10
    entries_columns = 1

    for i in range(entries_rows):
        saved_entries.grid_rowconfigure(i, weight=1)
    for i in range(entries_columns):
        saved_entries.grid_columnconfigure(i, weight=1)

    home_button = tk.Button(view_entries_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(view_entries_page)) # home button
    home_button.grid(row=8, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(view_entries_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack View Saved Entries Page

    display_entries_to_view(saved_entries)
    view_entries_page.pack(fill="both", expand=True)

def delete_entry_page_function(): # Page 4 - Delete Entry Page

    window.title("aero Text Diary - Delete Entry")

    # Grid Configuration

    delete_entry_page = tk.Frame(window, bg="#81C046")

    pg4rows = 10
    pg4columns = 10

    for i in range(pg4rows):
        delete_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg4columns):
        delete_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(delete_entry_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    saved_entries = tk.Frame(delete_entry_page, bg="#81C046") # this frame contains the saved entries that will be loaded from the JSON file
    saved_entries.grid(row=1, rowspan=6, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    entries_rows = 10
    entries_columns = 5

    for i in range(entries_rows):
        saved_entries.grid_rowconfigure(i, weight=1)
    for i in range(entries_columns):
        saved_entries.grid_columnconfigure(i, weight=1)

    delete_label = tk.Label(delete_entry_page, bd=5, bg="yellow", fg="black", font="Helvitica 18", text="enter title to delete") # label instructions for delete textbox
    delete_label.grid(row=7, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    delete_textbox = tk.Entry(delete_entry_page, bg="lightblue", font="Helvitica 18")
    delete_textbox.grid(row=7, column=5, columnspan=5, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(delete_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(delete_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    submit_button = tk.Button(delete_entry_page, bg="red", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="delete entry", command=lambda: delete_entry(delete_textbox, delete_entry_page)) # submit button
    submit_button.grid(row=8, column=5, columnspan=5, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(delete_entry_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Delete Entry Page

    display_entries_to_delete(saved_entries)
    delete_entry_page.pack(fill='both', expand=True)

def help_readme():

    window.title("aero Text Diary - Help & Readme")

    # Grid Configuration

    help_readme_page = tk.Frame(window, bg="#81C046")

    pg5rows = 10
    pg5columns = 10

    for i in range(pg5rows):
        help_readme_page.grid_rowconfigure(i, weight=1)
    for i in range(pg5columns):
        help_readme_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(help_readme_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    read_me = "HELP & README\n\nWelcome to the Python Text Diary Program!.\n\nThis program is designed to let users store their favourite memories in a text diary format - holidays, days away, funny stories, anything you like really - but to do that it is important to have an idea of how the program works of course.\n\nAs you will have seen, the home page consists of the main menu. Here you have four options:\n\nNew Entry\n\nOption 1 - The 'New Entry' page allows the user to enter new text diary entries. Simply fill in the fields and hit 'Submit'. The entry will be saved and can be read later on.\n\nOption 2 - View Saved Entries\n\nThis page allows the user to select and read a saved entry. A list of current entries will be displayed on the screen as buttons. Simply click on the entry you wish to view. A new page will then appear with the entry available to read there.\n\nOption 3 - Delete Entry\n\nSometimes you might find that you want to delete an entry, whether to save space or simply because it may not be fond to you anymore. On this page, the titles of each entry will once again be displayed. Simply type in the name of the entry to delete, and hit 'Submit'. A message will appear to let you know that the entry has been deleted. Leave the page, and when you come back it should be gone."

    help_readme_text = tk.Text(help_readme_page, bg="lightblue", font="Helvitica 18", width=52, height=12) # help/readme displayed here
    help_readme_text.grid(row=1, rowspan=7, column=0, columnspan=8, padx=5, pady=5, sticky="nsew")

    help_readme_text.insert("1.0", read_me)

    home_button = tk.Button(help_readme_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(help_readme_page)) # home button
    home_button.grid(row=8, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")
    
    # Footer

    footer = tk.Label(help_readme_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Help & Readme Page

    help_readme_page.pack(fill='both', expand=True)

def read_entry(): # Page 6 - Read Saved Entry Page

    window.title("aero Text Diary - Read Entry")

    # Grid Configuration

    read_entry_page = tk.Frame(window, bg="#81C046")

    pg6rows = 10
    pg6columns = 10

    for i in range(pg6rows):
        read_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg6columns):
        read_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    title_label = tk.Label(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter title: ") # title section
    title_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_title
    entry_title = tk.Text(read_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=1)
    entry_title.grid(row=1, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    date_label = tk.Label(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter date: ") # date section
    date_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_date
    entry_date = tk.Text(read_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=1)
    entry_date.grid(row=2, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    main_label = tk.Label(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", text="enter article: ") # main article section
    main_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_main
    entry_main = tk.Text(read_entry_page, bg="lightblue", font="Helvitica 18", width=45, height=10)
    entry_main.grid(row=3, rowspan=5, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(read_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    # Footer

    footer = tk.Label(read_entry_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Read Entry Page

    view_entries_page.destroy()
    read_entry_page.pack(fill='both', expand=True)
    


# ---------- HOME PAGE BUTTON FUNCTIONS ---------- #

def visit_new_entry(home_page):

    home_page.destroy()
    new_entry()

def visit_saved_entries(home_page):

    home_page.destroy()
    view_entries()

def visit_delete_entry(home_page):

    home_page.destroy()
    delete_entry_page_function()

def visit_help_readme(home_page):

    home_page.destroy()
    help_readme()

# ---------- HOME BUTTONS FUNCTION ---------- #

def home(x):

    x.destroy()
    main()

# ---------- DIARY ENTRY (JSON READ/WRITE) FUNCTIONS ---------- #

def save_new_entry(new_entry_title, new_entry_date, new_entry_main):

    diary_entry = {}

    diary_entry["title"] = new_entry_title.get("1.0", 'end-1c')
    diary_entry["date"] = new_entry_date.get("1.0", 'end-1c')
    diary_entry["main"] = new_entry_main.get("1.0", 'end-1c')

    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

    diary_entries.append(diary_entry)

    with open (diary_entries_file, 'w') as f:
        json.dump(diary_entries, f, indent=4)

    new_entry_title.delete(1.0, tk.END)
    new_entry_date.delete(1.0, tk.END)
    new_entry_main.delete(1.0, tk.END)

# These two functions form the most difficult part of the program for me, as I struggled to figure out how to make each of the buttons generated in the loop uniquely
# identifiable to the "load_entry()" function. It turns out that what I was needing was to pass the "diary_entry["title"]" as an argument alongside the "lambda" function and THEN
# assign that expression to the function itself.

def display_entries_to_view(saved_entries): # displays a button for each entry to allow the user to open a diary entry

    with open (diary_entries_file, 'r') as f: # accesses the JSON file holding the diary entries
        diary_entries = json.load(f)

    for i, diary_entry in enumerate(diary_entries, start=1):
        entry_button = tk.Button(saved_entries, bg="#245DDA", fg="white", font="Helvitica 14", text=f"{i} - TITLE: {diary_entry["title"]} - DATE: {diary_entry["date"]}", command=lambda e=diary_entry["title"]: load_entry(e)) # the lambda function that tripped me up!
        entry_button.grid(row=i-1, columnspan=1, column=0, sticky="nsew", padx=5, pady=5)

def load_entry(entry_selection): # loads the chosen entry onto the "read entry" page

    read_entry()

    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

    for diary_entry in diary_entries:
        if entry_selection == diary_entry["title"]:
            entry_title.insert("1.0", diary_entry["title"])
            entry_date.insert("1.0", diary_entry["date"])
            entry_main.insert("1.0", diary_entry["main"])

# The above was for sure the most frustrating part of the program to build, but very happy with the result - and helped when it came to the delete page as well

def display_entries_to_delete(saved_entries):

    with open (diary_entries_file, 'r') as f: # accesses the JSON file holding the diary entries
        diary_entries = json.load(f)

    for i, diary_entry in enumerate(diary_entries, start=1):

        delete_entry_label = tk.Label(saved_entries, bg="#245DDA", fg="white", font="Helvitica 14", text=f"{i} - TITLE: {diary_entry["title"]} - DATE: {diary_entry["date"]}")
        delete_entry_label.grid(row=i-1, columnspan=5, column=0, sticky="nsew", padx=5, pady=5)

def delete_entry(delete_textbox, delete_entry_page): # deletes a saved entry once a title is written in the textbox and the submit button is pressed, then should refresh the entries

    new_data = []

    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

        delete_selection = delete_textbox.get()

        for diary_entry in diary_entries:
            if diary_entry['title'] == delete_selection: # if an entry is found matching the title of entry the user wishes to delete
                pass # allows the for loop to continue without doing anything
            else:
                new_data.append(diary_entry) # adds the diary entries that we want to keep back onto the JSON file

    with open (diary_entries_file, 'w') as f:
        json.dump(new_data, f, indent=4)

    delete_entry_page.destroy() # destroys the current instance of the page to allow it to be loaded again (refreshed)
    delete_entry_page_function() # brings the page up again, sans the deleted entry

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

    header = tk.Label(home_page, bg="#245DDA", fg="white", font="Helvitica 40", text="aero text diary") # Windows XP-style blue
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Buttons

    new_entry_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="add new entry", command=lambda: visit_new_entry(home_page))
    new_entry_page.grid(row=1, rowspan=4, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    view_entries_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="view current entries", command=lambda: visit_saved_entries(home_page))
    view_entries_page.grid(row=1, rowspan=4, column=5, columnspan=5, padx=10, pady=10, sticky="nsew")

    delete_entry_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="delete saved entry", command=lambda: visit_delete_entry(home_page))
    delete_entry_page.grid(row=5, rowspan=4, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")

    help_readme_page = tk.Button(home_page, bg="#245DDA", fg="white", font="Helvitica 14", relief=tk.RAISED, bd=5, text="help & readme", command=lambda: visit_help_readme(home_page))
    help_readme_page.grid(row=5, rowspan=4, column=5, columnspan=5, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(home_page, bg="#245DDA", fg="white", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Home Page

    home_page.pack(fill='both', expand=True)

main()

window.mainloop()
