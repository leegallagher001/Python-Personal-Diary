# ProtoDiaryGUI-V3 - by Lee Gallagher

# A continuation building upon the work done in GUI-V2, the idea for V3 will be to experiment with the next ideas, making
# the "delete entry" functions more buttons-based (similar to the "read entry" function) as well as some experiments with
# adding other types of media such as audio excerpts

# (0) Imports

import sys
from datetime import date
import os
import tkinter as tk # for UI
from tkinter import *
from tkinter import filedialog # used on "Add Audio Entry" page
from tkinter.filedialog import askdirectory, askopenfilename # used on "Add Audio Entry" page
import json # used for text entry storage
from turtle import title
import pathlib
from pathlib import Path
import pygame 
from pygame import mixer # used to play audio entries
import sounddevice as sd # used to record audio
from scipy.io.wavfile import write # used to write audio data to a file
import wavio as wv # used to create a .wav file for audio
from pydub import AudioSegment # used to convert .wav to .mp3 - also need to pip install "ffmpeg" for this to work

diary_entries_file = "pdgui-v3-entries.json"

audio_entries_folder_directory = r"C:\Users\User\Desktop\Personal Diary Project (Python)\ProtoDiaryGUI-V3\Audio Entries" # path to the "audio entries" folder - 'r' at beginning treats the path like a raw string

window = tk.Tk()
window.geometry("1000x600")

# ---------- PAGES ---------- #

def new_entry(): # Page 2 - Add New Entry Page

    window.title("Honeycomb Text Diary - Add New Entry")

    # Grid Configuration

    new_entry_page = tk.Frame(window, bg="black")

    pg2rows = 10
    pg2columns = 10

    for i in range(pg2rows):
        new_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg2columns):
        new_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(new_entry_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    new_title_label = tk.Label(new_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter title: ") # title section
    new_title_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_title = tk.Text(new_entry_page, bg="orange", font="Helvitica 18", width=45, height=1)
    new_entry_title.grid(row=1, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_date_label = tk.Label(new_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter date: ") # date section
    new_date_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_date = tk.Text(new_entry_page, bg="orange", font="Helvitica 18", width=45, height=1)
    new_entry_date.grid(row=2, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    new_main_label = tk.Label(new_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter article: ") # main article section
    new_main_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    new_entry_main = tk.Text(new_entry_page, bg="orange", font="Helvitica 18", width=45, height=10, wrap="word") # word wrap stops words from splitting when typing multiple lines
    new_entry_main.grid(row=3, rowspan=5, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(new_entry_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(new_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=3, padx=5, pady=5, sticky="nsew")

    submit_button = tk.Button(new_entry_page, bg="black", fg="orange", font="Helvitica 18", relief=tk.RAISED, bd=5, text="submit entry", command=lambda: save_new_entry(new_entry_title, new_entry_date, new_entry_main)) # submit button
    submit_button.grid(row=8, column=3, columnspan=4, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(new_entry_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(new_entry_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack New Entry Page

    new_entry_page.pack(fill='both', expand=True)

def view_entries(): # Page 3 - View Saved Entries Page

    window.title("Honeycomb Text Diary - View Saved Entries")

    # Grid Configuration

    global view_entries_page
    view_entries_page = tk.Frame(window, bg="black")

    pg3rows = 10
    pg3columns = 10

    for i in range(pg3rows):
        view_entries_page.grid_rowconfigure(i, weight=1)
    for i in range(pg3columns):
        view_entries_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(view_entries_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    saved_entries = tk.Frame(view_entries_page, bg="orange") # this frame contains the saved entries that will be loaded from the JSON file
    saved_entries.grid(row=1, rowspan=7, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    entries_rows = 10
    entries_columns = 1

    for i in range(entries_rows):
        saved_entries.grid_rowconfigure(i, weight=1)
    for i in range(entries_columns):
        saved_entries.grid_columnconfigure(i, weight=1)

    home_button = tk.Button(view_entries_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(view_entries_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(view_entries_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(view_entries_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack View Saved Entries Page

    display_entries_to_view(saved_entries)
    view_entries_page.pack(fill="both", expand=True)

def delete_entry_page_function(): # Page 4 - Delete Entry Page

    window.title("Honeycomb Text Diary - Delete Entry")

    # Grid Configuration

    delete_entry_page = tk.Frame(window, bg="black")

    pg4rows = 10
    pg4columns = 10

    for i in range(pg4rows):
        delete_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg4columns):
        delete_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(delete_entry_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    saved_entries = tk.Frame(delete_entry_page, bg="orange") # this frame contains the saved entries that will be loaded from the JSON file
    saved_entries.grid(row=1, rowspan=7, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    entries_rows = 10
    entries_columns = 10

    for i in range(entries_rows):
        saved_entries.grid_rowconfigure(i, weight=1)
    for i in range(entries_columns):
        saved_entries.grid_columnconfigure(i, weight=1)

    # Saved Entries Header Section

    saved_number = tk.Label(saved_entries, bg="black", fg="orange", font="Helvitica 14", text="No.")
    saved_number.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    saved_title = tk.Label(saved_entries, bg="black", fg="orange", font="Helvitica 14", text="Title")
    saved_title.grid(row=0, column=1, columnspan=4, sticky="nsew", padx=5, pady=5)

    saved_date = tk.Label(saved_entries, bg="black", fg="orange", font="Helvitica 14", text="Date")
    saved_date.grid(row=0, column=5, columnspan=4, sticky="nsew", padx=5, pady=5)

    saved_button = tk.Label(saved_entries, bg="black", fg="orange", font="Helvitica 14", text="Delete?")
    saved_button.grid(row=0, column=9, sticky="nsew", padx=5, pady=5)

    # Home Button

    home_button = tk.Button(delete_entry_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(delete_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(delete_entry_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(delete_entry_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Delete Entry Page

    display_entries_to_delete(saved_entries, delete_entry_page)
    delete_entry_page.pack(fill='both', expand=True)

def help_readme():

    window.title("Honeycomb Text Diary - Help & Readme")

    # Grid Configuration

    help_readme_page = tk.Frame(window, bg="black")

    pg5rows = 10
    pg5columns = 10

    for i in range(pg5rows):
        help_readme_page.grid_rowconfigure(i, weight=1)
    for i in range(pg5columns):
        help_readme_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(help_readme_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    read_me = "HELP & README\n\nWelcome to the Python Text Diary Program!.\n\nThis program is designed to let users store their favourite memories in a text diary format - holidays, days away, funny stories, anything you like really - but to do that it is important to have an idea of how the program works of course.\n\nAs you will have seen, the home page consists of the main menu. Here you have four options:\n\nNew Entry\n\nOption 1 - The 'New Entry' page allows the user to enter new text diary entries. Simply fill in the fields and hit 'Submit'. The entry will be saved and can be read later on.\n\nOption 2 - View Saved Entries\n\nThis page allows the user to select and read a saved entry. A list of current entries will be displayed on the screen as buttons. Simply click on the entry you wish to view. A new page will then appear with the entry available to read there.\n\nOption 3 - Delete Entry\n\nSometimes you might find that you want to delete an entry, whether to save space or simply because it may not be fond to you anymore. On this page, the titles of each entry will once again be displayed. Simply type in the name of the entry to delete, and hit 'Submit'. A message will appear to let you know that the entry has been deleted. Leave the page, and when you come back it should be gone.\n\nOption 4 - Audio Entries\n\nPage Under Construction."

    help_readme_text = tk.Text(help_readme_page, bg="orange", font="Helvitica 18", width=52, height=12, wrap="word") # help/readme displayed here
    help_readme_text.grid(row=1, rowspan=7, column=0, columnspan=10, padx=5, pady=5, sticky="nsew")

    help_readme_text.insert("1.0", read_me)

    help_readme_text.config(state=tk.DISABLED) # makes the text box read-only

    home_button = tk.Button(help_readme_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(help_readme_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(help_readme_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")
    
    # Footer

    footer = tk.Label(help_readme_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Help & Readme Page

    help_readme_page.pack(fill='both', expand=True)

def read_entry(): # Page 6 - Read Saved Entry Page

    window.title("Honeycomb Text Diary - Read Entry")

    # Grid Configuration

    read_entry_page = tk.Frame(window, bg="black")

    pg6rows = 10
    pg6columns = 10

    for i in range(pg6rows):
        read_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg6columns):
        read_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(read_entry_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    title_label = tk.Label(read_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter title: ") # title section
    title_label.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_title
    entry_title = tk.Text(read_entry_page, bg="orange", font="Helvitica 18", width=45, height=1, wrap="word") # wrap = "word" makes the text display properly, stopping words from splitting
    entry_title.grid(row=1, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    date_label = tk.Label(read_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter date: ") # date section
    date_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_date
    entry_date = tk.Text(read_entry_page, bg="orange", font="Helvitica 18", width=45, height=1, wrap="word")
    entry_date.grid(row=2, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    main_label = tk.Label(read_entry_page, bg="orange", fg="black", font="Helvitica 18", text="enter article: ") # main article section
    main_label.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky="nsew")
    global entry_main
    entry_main = tk.Text(read_entry_page, bg="orange", font="Helvitica 18", width=45, height=10, wrap="word")
    entry_main.grid(row=3, rowspan=5, column=2, columnspan=8, padx=5, pady=5, sticky="nsew")

    home_button = tk.Button(read_entry_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(read_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(read_entry_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(read_entry_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Read Entry Page

    view_entries_page.destroy()
    read_entry_page.pack(fill='both', expand=True)
    
def audio_entries(): # Page 7 - Audio Entries Page

    window.title("Honeycomb Text Diary - Audio Entries")

    # Grid Configuration

    audio_entries_page = tk.Frame(window, bg="black")

    pg7rows = 10
    pg7columns = 10

    for i in range(pg7rows):
        audio_entries_page.grid_rowconfigure(i, weight=1)
    for i in range(pg7columns):
        audio_entries_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(audio_entries_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    audio_interface_frame = tk.Frame(audio_entries_page, bg="orange") # this frame will contain the interface through which audio is played (buttons etc.)
    audio_interface_frame.grid(row=1, rowspan=7, column=0, columnspan=5, padx=5, pady=5, sticky="nsew")

    interface_rows = 3
    interface_columns = 4

    for i in range(interface_rows):
        audio_interface_frame.grid_rowconfigure(i, weight=1)
    for i in range(interface_columns):
        audio_interface_frame.grid_columnconfigure(i, weight=1)

    audio_entry_selected = tk.Entry(audio_interface_frame, bg="black", fg="orange", font="Helvitica 18", justify="center") # this entry will contain the loaded audio entry to be played
    audio_entry_selected.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky="nsew")

    play_btn = tk.Button(audio_interface_frame, bg="orange", font="Helvitica 20", text="PLAY", command=lambda: play_audio_entry(audio_entry_selected, volume_display)) # play the audio entry
    play_btn.grid(row=1, column=0, padx=5, pady=5, sticky="nsew")

    pause_btn = tk.Button(audio_interface_frame, bg="yellow", fg="black", font="Helvitica 20", text="PAUSE", command=lambda: pause_entry()) # pauses the audio entry
    pause_btn.grid(row=1, column=1, padx=5, pady=5, sticky="nsew")

    unpause_btn = tk.Button(audio_interface_frame, bg="yellow", fg="black", font="Helvitica 20", text="UNPAUSE", command=lambda: unpause_entry()) # unpauses the audio entry
    unpause_btn.grid(row=1, column=2, padx=5, pady=5, sticky="nsew")

    stop_btn = tk.Button(audio_interface_frame, bg="red", fg="black", font="Helvitica 20", text="STOP", command=lambda: stop_audio_entry()) # stop the audio entry
    stop_btn.grid(row=1, column=3, padx=5, pady=5, sticky="nsew")

    volume_down_btn = tk.Button(audio_interface_frame, bg="yellow", fg="black", font="Helvitica 20", text="<", command=lambda: volume_decrease(volume_display)) # volume down button
    volume_down_btn.grid(row=2, column=0, padx=5, pady=5, sticky="nsew")

    volume_display = tk.Label(audio_interface_frame, bg="black", fg="orange", font="Helvitica 14", text="0.5") # displays the current volume
    volume_display.grid(row=2, column=1, columnspan=2, padx=5, pady=5, sticky="nsew") # uses a label, so not sure how well this will work when I try to add actual functionality

    volume_up_btn = tk.Button(audio_interface_frame, bg="yellow", fg="black", font="Helvitica 20", text=">", command=lambda: volume_increase(volume_display)) # volume up button
    volume_up_btn.grid(row=2, column=3, padx=5, pady=5, sticky="nsew")

    audio_saved_entries = tk.Frame(audio_entries_page, bg="orange") # this frame contains the saved audio entries
    audio_saved_entries.grid(row=1, rowspan=7, column=5, columnspan=5, padx=5, pady=5, sticky="nsew")

    entries_rows = 10
    entries_columns = 1

    for i in range(entries_rows):
        audio_saved_entries.grid_rowconfigure(i, weight=1)
    for i in range(entries_columns):
        audio_saved_entries.grid_columnconfigure(i, weight=1)

    home_button = tk.Button(audio_entries_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(audio_entries_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(audio_entries_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(audio_entries_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Audio Entries Page

    display_audio_entries(audio_saved_entries, audio_entry_selected)
    audio_entries_page.pack(fill='both', expand=True)

def add_audio_entry(): # Page 8 - Add Audio Entry Page

    window.title("Honeycomb Text Diary - Add Audio Entry")

    # Grid Configuration

    add_audio_entry_page = tk.Frame(window, bg="black")

    pg8rows = 10
    pg8columns = 10

    for i in range(pg8rows):
        add_audio_entry_page.grid_rowconfigure(i, weight=1)
    for i in range(pg8columns):
        add_audio_entry_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(add_audio_entry_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary")
    header.grid(row=0, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Content

    mp3_instruct_text = "This section allows you to add an audio recording you have already made into the diary program's storage system so it can be played later on.\n\nClick the button, drag or paste your .mp3 file into the folder, and close the window - simple!\n\nYou should have your file copied and ready to be pasted into the file or otherwise accessible to be dragged into the folder."
    record_instruct_text = "This section allows you to record an audio entry on the program itself. You will have to enter how long you wish to record for before recording.\n\nEnter a time (in seconds) then click the button below to get started with recording a new audio entry."

    add_mp3_instructions = tk.Text(add_audio_entry_page, bg="yellow", fg="black", font="Helvitica 20", wrap="word", height=8, width=30)
    add_mp3_instructions.grid(row=1, rowspan=5, column=0, columnspan=5, padx=10, pady=10, sticky="nsew")
    add_mp3_instructions.insert("1.0", mp3_instruct_text)
    add_mp3_instructions.config(state = tk.DISABLED)

    add_mp3_btn = tk.Button(add_audio_entry_page, bg="#245DDA", fg="white", font="Helvitica 20", text="Add MP3 Entry", command=lambda:filedialog.askopenfilename(initialdir=audio_entries_folder_directory, filetypes=[("Audio Files", "*.mp3")]))
    add_mp3_btn.grid(row=6, rowspan=2, column=0, columnspan=5, padx=10, pady=5, sticky="nsew")

    record_entry_instructions = tk.Text(add_audio_entry_page, bg="yellow", fg="black", font="Helvitica 20", wrap="word", height=8, width=30)
    record_entry_instructions.grid(row=1, rowspan=3, column=5, columnspan=5, padx=10, pady=10, sticky="nsew")
    record_entry_instructions.insert("1.0", record_instruct_text)
    record_entry_instructions.config(state = tk.DISABLED)

    enter_filename_label = tk.Label(add_audio_entry_page, bg="orange", fg="black", font="Helvitica 16", text="Entry Name") # Allows user to enter a file name for their recording
    enter_filename_label.grid(row=4, column=5, columnspan=3, padx=10, pady=5, sticky="nsew")

    enter_filename_entry = tk.Entry(add_audio_entry_page, bg="yellow", fg="black", font="Helvitica 16", justify="center", width=8)
    enter_filename_entry.grid(row=4, column=8, columnspan=2, padx=10, pady=5, sticky="nsew")

    enter_time_label = tk.Label(add_audio_entry_page, bg="orange", fg="black", font="Helvitica 16", text="Enter Recording Time (Seconds)") # Allows user to set duration of recording - only way to do it in Python it seems
    enter_time_label.grid(row=5, column=5, columnspan=4, padx=10, pady=5, sticky="nsew")

    enter_time_entry = tk.Entry(add_audio_entry_page, bg="yellow", fg="black", font="Helvitica 16", justify="center", width=8)
    enter_time_entry.grid(row=5, column=9, padx=10, pady=5, sticky="nsew")

    record_btn = tk.Button(add_audio_entry_page, bg="#81C033", fg="white", font="Helvitica 20", text="Record New Entry", command=lambda: record_audio_entry(enter_filename_entry, enter_time_entry))
    record_btn.grid(row=6, rowspan=2, column=5, columnspan=5, padx=10, pady=5, sticky="nsew")

    home_button = tk.Button(add_audio_entry_page, bg="orange", fg="black", font="Helvitica 18", relief=tk.RAISED, bd=5, text="home", command=lambda: home(add_audio_entry_page)) # home button
    home_button.grid(row=8, column=0, columnspan=7, padx=5, pady=5, sticky="nsew")

    exit_app = tk.Button(add_audio_entry_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=8, column=7, columnspan=3, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(add_audio_entry_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=9, column=0, columnspan=10, padx=10, pady=5, sticky="nsew")

    # Pack Audio Entries Page

    add_audio_entry_page.pack(fill='both', expand=True)

# ---------- HOME PAGE BUTTON FUNCTION (TO VISIT OTHER PAGE) ---------- #

def visit_page(home_page, y):

    home_page.destroy()
    y()

# ---------- HOME BUTTONS FUNCTION ---------- #

def home(x):

    x.destroy()
    main()

# ---------- EXIT BUTTON ---------- #

def exit_button():

    sys.exit()

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
        entry_button = tk.Button(saved_entries, bg="black", fg="orange", font="Helvitica 14", text=f"{i} - TITLE: {diary_entry["title"]} - DATE: {diary_entry["date"]}", command=lambda e=diary_entry["title"]: load_entry(e)) # the lambda function that tripped me up!
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

            entry_title.config(state=tk.DISABLED) # makes the text field read_only
            entry_date.config(state=tk.DISABLED) # makes the text field read_only
            entry_main.config(state=tk.DISABLED) # makes the text field read_only

# The above was for sure the most frustrating part of the program to build, but very happy with the result - and helped when it came to the delete page as well

def display_entries_to_delete(saved_entries, delete_entry_page):

    with open (diary_entries_file, 'r') as f: # accesses the JSON file holding the diary entries
        diary_entries = json.load(f)

    for i, diary_entry in enumerate(diary_entries, start=1): # generates a columned list of current entries - looks quite a bit better than GUI-V2 I think

        delete_entry_number = tk.Label(saved_entries, bg="darkorange", fg="black", font="Helvitica 14", text=f"{i}")
        delete_entry_number.grid(row=i, column=0, sticky="nsew", padx=5, pady=5)

        delete_entry_label = tk.Label(saved_entries, bg="darkorange", fg="black", font="Helvitica 14", text=f"{diary_entry["title"]}")
        delete_entry_label.grid(row=i, columnspan=4, column=1, sticky="nsew", padx=5, pady=5)

        delete_entry_label_date = tk.Label(saved_entries, bg="darkorange", fg="black", font="Helvitica 14", text=f"{diary_entry["date"]}")
        delete_entry_label_date.grid(row=i, columnspan=4, column=5, sticky="nsew", padx=5, pady=5)

        delete_entry_button = tk.Button(saved_entries, bg="red", fg="black", font="Helvitica 14", text="X", command=lambda y=diary_entry["title"]: delete_entry(delete_entry_page, y))
        delete_entry_button.grid(row=i, column=9, sticky="nsew", padx=5, pady=5) # button to delete entries instead of a textbox and submit button - will be subject to further development

def delete_entry(delete_entry_page, y): # deletes a saved entry once a title is written in the textbox and the submit button is pressed, then should refresh the entries

    new_data = []

    with open (diary_entries_file, 'r') as f:
        diary_entries = json.load(f)

        for diary_entry in diary_entries:
            if diary_entry['title'] == y: # if an entry is found matching the title of entry the user wishes to delete
                pass # allows the for loop to continue without doing anything
            else:
                new_data.append(diary_entry) # adds the diary entries that we want to keep back onto the JSON file

    with open (diary_entries_file, 'w') as f:
        json.dump(new_data, f, indent=4)

    delete_entry_page.destroy() # destroys the current instance of the page to allow it to be loaded again (refreshed)
    delete_entry_page_function() # brings the page up again, sans the deleted entry

# ---------- AUDIO ENTRIES FOLDER & PAGE FUNCTIONS ---------- #

def display_audio_entries(audio_saved_entries, audio_entry_selected): # displays the audio entries as buttons in the "audio saved entries" frame

    for i, audio_entry in enumerate(os.listdir(audio_entries_folder_directory), start=1):
        audio_entry_button = tk.Button(audio_saved_entries, bg="black", fg="orange", font="Helvitica 14", text=f"{i}. {audio_entry}", command=lambda e = audio_entry: load_audio_entry(audio_entry_selected, e)) # similar lambda function as the saved text entries page
        audio_entry_button.grid(row=i-1, columnspan=1, column=0, sticky="nsew", padx=5, pady=5)

def load_audio_entry(audio_entry_selected, e): # loads the title of the audio entry into the entry box, allowing us to then call that specific entry using the play_audio_entry() function

    audio_entry_selected.delete(0, tk.END) # deletes the current entry in the box
    audio_entry_selected.insert(0, e) # loads the entry for the button pressed

def play_audio_entry(audio_entry_selected, volume_display): # uses the OS and Pygame modules to create a path to the audio entry in the folder and play it

    audio_entry_to_play = audio_entry_selected.get() # retrieves the title of the file from the "selected entry" text box above
    audio_volume = float(volume_display["text"])

    for audio_entry in os.listdir(audio_entries_folder_directory): # loops through "audio entries" folder
        if audio_entry_to_play == audio_entry: # finds the matching entry
            audio_entry_path = os.path.join("Audio Entries", f"{audio_entry}") # creates a path for the program to find the entry to play
            mixer.init() # initialises Pygame's "mixer" function
            mixer.music.load(f"{audio_entry_path}") # loads the audio entry into the "mixer"
            mixer.music.set_volume(audio_volume) # sets the volume of the playback
            mixer.music.play() # plays the audio

def stop_audio_entry(): # stops the entry from playing

    mixer.music.stop() # stops playback of the entry

# Getting these volume button functions below to work properly - both with and without audio currently playing - was a surprisingly difficult thing to pull off

def volume_increase(volume_display): # increases the audio volume in 0.1 increments when pressed

    if float(volume_display["text"]) >= 0 and float(volume_display["text"]) < 1: # checks that the volume is between 0.0 and 0.9
        audio_volume = float(volume_display["text"]) + 0.1
        audio_volume_rounded = round(audio_volume, 1) # rounds to nearest 1 decimal place, as was getting very slight variations in numbers for some reason
        volume_display["text"] = audio_volume_rounded
        if pygame.mixer.get_init(): # checks to see if mixer is initiated
            mixer.music.set_volume(audio_volume) # updates the audio volume if it is
        else: # passes the update step if not
            pass
    else:
        pass

def volume_decrease(volume_display): # decreases the audio volume in 0.1 increments when pressed
    
    if float(volume_display["text"]) > 0 and float(volume_display["text"]) <= 1: # checks that the volume is between 0.1 and 1.0
        audio_volume = float(volume_display["text"]) - 0.1
        audio_volume_rounded = round(audio_volume, 1) # rounds to nearest 1 decimal place, as was getting very slight variations in numbers for some reason
        volume_display["text"] = audio_volume_rounded
        if pygame.mixer.get_init(): # checks to see if mixer is initiated
            mixer.music.set_volume(audio_volume) # updates the audio volume if it is
        else: # passes the update step if not
            pass
    else:
        pass

# Having seperate buttons for pausing and unpausing is an extremely clunky solution to this problem. Will need to take a good look at this soon.

def pause_entry(): # pauses the entry if playing

    if pygame.mixer.get_init():
        pygame.mixer.music.pause()
    else:
        pass

def unpause_entry(): # unpauses the entry if paused

    if pygame.mixer.get_init():
        pygame.mixer.music.unpause()
    else:
        pass

# ---------- ADD AUDIO ENTRIES PAGE (RECORD ENTRY) FUNCTION ---------- #

def record_audio_entry(enter_filename_entry, enter_time_entry): # allows the user to record a new entry

    filename = enter_filename_entry.get() # takes name from entry name input

    record_time = int(enter_time_entry.get()) # takes time from time entry input

    freq = 44100

    duration = record_time

    recording = sd.rec(int(duration * freq), samplerate=freq, channels=2) # starts recording

    sd.wait() # records audio for given number of seconds

    wv.write(f"{filename}.wav", recording, freq, sampwidth=2)

    # INVESTIGATION REQUIRED - it's going to take a significant amount of digging to figure out exactly how I managed to get the next two lines to work
    # as for the longest time it didn't and then after trying about 20 different things it just...did. Also, theres still an error message in the console
    # that pops up upon program start

    AudioSegment.converter = r"C:\ffmpeg-8.0.1-full_build\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

    new_audio_entry = AudioSegment.from_wav(f"{filename}.wav").export(f"Audio Entries/{filename}.mp3", format="mp3")
        
# ---------- PROGRAM START ---------- #

def main(): # Page 1 - Home Page

    window.title("Honeycomb Text Diary - Home")

    # Grid Configuration

    home_page = tk.Frame(window, bg="black") # "Honeycomb" theme - because why not!

    pg1rows = 12
    pg1columns = 12

    for i in range(pg1rows):
        home_page.grid_rowconfigure(i, weight=1)
    for i in range(pg1columns):
        home_page.grid_columnconfigure(i, weight=1)

    # Header

    header = tk.Label(home_page, bg="orange", fg="black", font="Helvitica 40", text="honeycomb text diary") # Windows XP-style blue
    header.grid(row=0, column=0, columnspan=12, padx=10, pady=5, sticky="nsew")

    # Buttons

    new_entry_page = tk.Button(home_page, bg="orange", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="add new entry", command=lambda: visit_page(home_page, new_entry))
    new_entry_page.grid(row=1, rowspan=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    view_entries_page = tk.Button(home_page, bg="orange", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="view current entries", command=lambda: visit_page(home_page, view_entries))
    view_entries_page.grid(row=1, rowspan=4, column=4, columnspan=4, padx=10, pady=10, sticky="nsew")

    delete_entry_page = tk.Button(home_page, bg="orange", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="delete saved entry", command=lambda: visit_page(home_page, delete_entry_page_function))
    delete_entry_page.grid(row=1, rowspan=4, column=8, columnspan=4, padx=10, pady=10, sticky="nsew")

    add_audio_entry_page = tk.Button(home_page, bg="orange", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="add audio entry", command=lambda: visit_page(home_page, add_audio_entry))
    add_audio_entry_page.grid(row=5, rowspan=4, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    audio_entries_page = tk.Button(home_page, bg="orange", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="current audio entries", command=lambda: visit_page(home_page, audio_entries))
    audio_entries_page.grid(row=5, rowspan=4, column=4, columnspan=4, padx=10, pady=10, sticky="nsew") # the audio entries page is the big experiment of this version

    exit_app = tk.Button(home_page, bg="red", fg="white", font="Helvitica 16", relief=tk.RAISED, bd=5, text="EXIT", command=exit_button)
    exit_app.grid(row=5, rowspan=4, column=8, columnspan=4, padx=10, pady=10, sticky="nsew")

    help_readme_page = tk.Button(home_page, bg="yellow", fg="black", font="Helvitica 16", relief=tk.RAISED, bd=5, text="help & readme", command=lambda: visit_page(home_page, help_readme))
    help_readme_page.grid(row=9, rowspan=2, column=0, columnspan=12, padx=10, pady=10, sticky="nsew")

    # Footer

    footer = tk.Label(home_page, bg="orange", fg="black", font="Helvitica 24", text="created by lee gallagher 2025")
    footer.grid(row=11, column=0, columnspan=12, padx=10, pady=5, sticky="nsew")

    # Pack Home Page

    home_page.pack(fill='both', expand=True)

main()

window.mainloop()
