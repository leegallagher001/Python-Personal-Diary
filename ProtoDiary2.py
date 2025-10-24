# Proto Diary 2 - by Lee Gallagher

# The second prototype in my journey to build a full-scale multimedia Python Diary Entry app

# Similarly to the first iteration, ProtoDiary2 will focus on text diary entries, but will be using JSON to store the entries
# with the hopes of being able to build a local storage and menu system that will allow the user to actually retrieve and read
# saved articles from within the Python program itself.

# Ultimately, the goal is to make a program that allows the user to create, read and delete text diary entries, all from within
# the Python program itself, powered by local JSON storage.

# (0) Imports

import json
import datetime
import os

pd2_entries_file = "pd2_entries.json"

# (1) Functions & Initial Global Variables

def newEntry(): # Main Menu - Option 1

    print("\n")
    title = input("Entry Title: ")
    print("\n")
    time = datetime.date.today()
    date = "Entry Date: " + str(time)
    print(date)
    print("\n")
    paragraphs = []
    while True:
        paragraph = input("Write About Your Day. Type 'END' On A New Line To Finish: ""\n") # main article
        print("\n")
        if paragraph == 'END':
            break
        paragraphs.append(paragraph)

    main = "\n\n".join(paragraphs)

    # Staged Test (Review Article To Be Saved)

    print("\n")
    print("Entry Title: ", title)
    print("\n")
    print("Entry Date: ", date)
    print("\n")
    print(main)

    # JSON Save

    print("\n")
    save = input("Would you like to save this entry? (Y/N): ")
    save.upper()
    if save == "Y":

        with open (pd2_entries_file, 'r') as f:
            diary_entries = json.load(f)

            diary_entry = {
                "title": title,
                "date": date,
                "main": main
            }

        diary_entries.append(diary_entry)

        with open (pd2_entries_file, 'w') as f:
            json.dump(diary_entries, f, indent=4)

    else:
        print("Okay, maybe next time!")

def accessEntry():  # Main Menu - Option 2

    with open (pd2_entries_file, 'r') as f:
        diary_entries = json.load(f)

    if not diary_entries:
        print("No Entries Saved")
    else:
        print("Your Diary Entries: ")
        print("\n")
        for i, diary_entry in enumerate(diary_entries, start=1):
            print(f"{i}. {diary_entry['title']}")

    print("\n")
    entry_selection = input("Enter Name Of Entry To Be Viewed: ")
    print("\n")

    for diary_entry in diary_entries:
        if entry_selection == diary_entry["title"]:
            print("-" * 50)
            print("ENTRY TITLE: ", diary_entry['title'])
            print("-" * 50)
            print("ENTRY DATE: : ", diary_entry['date'])
            print("-" * 50)
            print(diary_entry['main'])
            print("-" * 50)
            break
        else:
            print("Invalid Selection.")

# (2) Opening Statements

print("Proto Diary 2 - Lee Gallagher")
print("\n")
print("Hello, and welcome to the second prototype of my personal diary project!")
print("\n")
print("This program allows you to write, store, read and delete text diary entries, all from within the Python program this time - no .txt files in the middle!")
print("\n")

# (3) Main Menu

print("1. Write Diary Entry")
print("2. Read Diary Entries")
print("3. Delete Diary Entry")
print("4. Exit Program")
print("\n")

menuChoice = int(input("Enter Your Choice: "))

while menuChoice != 4:

    if menuChoice == 1:
        newEntry()
        print("\n")
        menuChoice = int(input("Would You Like Something Else - Choose Another Option: "))
    elif menuChoice == 2:
        accessEntry()
        print("\n")
        menuChoice = int(input("Would You Like Something Else - Choose Another Option: "))
    elif menuChoice == 3:
        print("Under Construction")
        print("\n")
        menuChoice = int(input("Would You Like Something Else - Choose Another Option: "))
    else:
        print("Invalid Input. Please Try Again.")
        print("\n")
        menuChoice = int(input("Would You Like Something Else - Choose Another Option: "))

print("Thanks for visiting the Proto Diary 2 program!")
print("\n")
input("Press 'ENTER' to exit the program.")
exit()
