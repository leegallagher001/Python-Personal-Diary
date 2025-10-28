# ProtoDiaryGUI-V1 - by Lee Gallagher

# This is a first prototype of what the UI/UX of my Python Diary application may look like.
# Initial goal is to simulate the "Main Menu" screen, however I will add more functionality where possible.

# (0) Imports

import tkinter as tk
from tkinter import *

# (1) Window Configuration

window = tk.Tk()
window.geometry("900x600")
window.configure(bg="#352f36")
window.title("Python Diary Application GUI Prototype V1")

# (2) Title Frame & Label

label_frame = tk.Frame(window, bg="lightgreen")
label_frame.pack(fill='both', expand=True)

label = tk.Label(label_frame, text="Python Diary Application", font=("Arial", 24), relief="solid", borderwidth=2, bg="black", fg="lightgreen", padx=100, pady=10)
label.pack(fill='both', expand=True, padx=5, pady=5)

# (3) Main Menu & Buttons

main_menu_frame = tk.Frame(window, bg="lightgreen")
main_menu_frame.pack(fill='both', expand=True, pady=5)

button_text = tk.Button(main_menu_frame, text="Text Diary ", font=("Arial", 16), width=70, height="2", bg="#084B13", fg="lightgreen", relief="raised", borderwidth=2)
button_text.pack(fill='both', expand=True, padx=5, pady=5)

button_images = tk.Button(main_menu_frame, text="Image Diary", font=("Arial", 16), width=70, height="2", bg="#084B13", fg="lightgreen", relief="raised", borderwidth=2)
button_images.pack(fill='both', expand=True, padx=5, pady=5)

button_audio = tk.Button(main_menu_frame, text="Audio Diary", font=("Arial", 16), width=70, height="2", bg="#084B13", fg="lightgreen", relief="raised", borderwidth=2)
button_audio.pack(fill='both', expand=True, padx=5, pady=5)

button_video = tk.Button(main_menu_frame, text="Video Diary", font=("Arial", 16), width=70, height="2", bg="#084B13", fg="lightgreen", relief="raised", borderwidth=2)
button_video.pack(fill='both', expand=True, padx=5, pady=5)

button_readme = tk.Button(main_menu_frame, text="Readme/Help", font=("Arial", 16), width=70, height="2", bg="#084B13", fg="lightgreen", relief="raised", borderwidth=2)
button_readme.pack(fill='both', expand=True, padx=5, pady=5)

window.mainloop()
