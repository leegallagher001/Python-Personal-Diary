# ProtoDiaryGUI-V1 - by Lee Gallagher

# This is a first prototype of what the UI/UX of my Python Diary application may look like.
# Initial goal is to simulate the "Main Menu" screen, however I will add more functionality where possible.

# (0) Imports

import tkinter as tk
from tkinter import *

# (1) Window Configuration

window = tk.Tk()
window.geometry("900x600")
window.configure(bg="lightgreen")
window.title("Python Diary Application GUI Prototype V1")

# (2) Grid Configuration

pg1rows = 6
pg1columns = 2

for i in range(pg1rows):
    window.grid_rowconfigure(i, weight=1)
for i in range(pg1columns):
    window.grid_columnconfigure(i, weight=1)

# (3) Main Menu

title_label = tk.Label(window, text="-- PYTHON TEXT DIARY --", bg="green", fg="black", font=("Arial", 24)).grid(column=0, row=0, columnspan=2, sticky=NSEW, padx=5, pady=5)

button_new = tk.Button(window, text="Add New Entry", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=0, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_view = tk.Button(window, text="View Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=1, row=1, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_delete = tk.Button(window, text="Delete Saved Entries", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=0, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

button_help = tk.Button(window, text="Help & Readme Text", borderwidth=2, relief="raised", fg="lightgreen", bg="black", font=("Arial", 20)).grid(column=1, row=3, rowspan=2, sticky=NSEW, padx=5, pady=5)

footer_label = tk.Label(window, text="Created by Lee Gallagher 2025", bg="green", fg="black", font=("Arial", 20)).grid(column=0, row=5, columnspan=2, sticky=NSEW, padx=5, pady=5)

window.mainloop()
