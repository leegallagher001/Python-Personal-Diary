# PERSONAL DIARY PROJECT - Prototype 1

# The first stage of my Diary project, the goals of this are to make a start on the most basic functions of the app - text input and text file generation

# (0) Imports

import os

# (1) Opening statement

print("TEXT DIARY ENTRY")
print("\n")
print("-- This function of the program generates a simple text diary entry --")
print("\n")

# (1B) Username & Password Entry

username = input("Please enter your username: ")
print("\n")
password = input("Please enter your password: ")

if username == "username" and password == "password":

    # (2) Header Inputs

    print("\n")
    title = input("Entry Title: ")
    title.upper()
    print("\n")
    date = input("Entry Date (dd/mm/yyyy): ")
    print("\n")
    time = input("Entry Time (XX:XX): ")
    print("\n")

    # (3) Main Body Input

    print("Write About Your Day - Type 'END' On A New Line To Finish: ")
    print("\n")
    paragraphs = []
    while True:
        paragraph = input()
        if paragraph == 'END':
            break
        paragraphs.append(paragraph)

    main = '\n'.join(paragraphs)

    # (4) Sample Output

    print("\n")
    print("-" * 50)
    print("\n")
    print(title)
    print("\n")
    print("-" * 50)
    print("\n")
    print(date)
    print("\n")
    print("-" * 50)
    print("\n")
    print(time)
    print("\n")
    print("-" * 50)
    print("\n")
    print(main)
    print("\n")

    # (5) Save Entry To Text File

    save = input("Would you like to save this diary entry? Y/N: ")

    if save == "Y":
        print("\n")
        file_input = input("Name File Entry: ")
        f = open(f"{file_input}.txt", "x")
        with open(f"{file_input}.txt", "a") as f:
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
            f.write(time)
            f.write("\n")
            f.write("-" * 50)
            f.write("\n")
            f.write(main)
            f.write("\n")
        input("Press 'ENTER' to exit the program")
    else:
        print("\n")
        print("File discarded. Have a nice day!")
        input("Press 'ENTER' to exit the program")

# (1C) Incorrect Login

else:
    print("Login Details Incorrect")
    input("Press 'ENTER' to exit the program")