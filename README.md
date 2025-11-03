---- PYTHON PERSONAL DIARY - by Lee Gallagher ----

-- INTRODUCTION --

The Python Personal Diary is an ongoing project that I have embarked upon both out of a wish to have a personal diary that covers multiple forms of media - including text, audio entires, images and videos - as well as building something that serves as a portfolio piece and demonstrates some aptitude with the Python programming language and it’s libraries.

The repository and the development of the project as a whole is structured around a multi-stage, iterative approach, with multiple prototypes that each serve to inform the development of a particular function of what I hope becomes the overall final product - a functional, user-friendly and aesthetically appealing Personal Diary Application.

Before moving on to discussing each of the prototypes in the repository in more detail, I should apologise if anything in the repository is particularly out-of-place or unusual. When I set up the repository for this project I didn’t have a great understanding of how to use Git or GitHub - truthfully, I still don’t, although I have slightly more experience with it now.

-- PROTOTYPES --

Prototype 1 - ProtoDiary1

ProtoDiary1 was my first step into my efforts to make a Python personal diary a reality. This program is a simple console application that takes in text information - a title, date and main article of text - assigns variables to them, and then uses a file method to print the content that the user has input onto a clean, easily-readable plain text (.txt) file.

This program taught me the basics of using file methods to create a file and then write information to that file. I was able to set the file method up in such a way that each file created would be named after the diary entry title that the user had provided.

Prototype 2 - ProtoDiary2

ProtoDiary2 was a logical step further from PD1. The focus of this prototype remains text-based, as I seen it best to master that before moving on to other forms of media.

This prototype has somewhat more features than PD1. It remains a console application, however it also incorporates a menu system, allowing the user to add diary entries, view saved diary entries and select an entry to read, and delete diary entries. When creating a new entry, the date of entry is generated automatically by the datetime module.

Instead of creating a text file, new entries are stored onto a JSON file, which has the advantages of being modifiable (allowing the addition and deletion of entries) as well as allowing the user to read a diary entry from the console application itself, rather than from an external text file. This isn’t a perfect program and there are plenty of things that could be improved upon, but overall it proved an informative exercise for my next stage of development.

Prototype 3 - ProtoDiaryGUI-V1

GUI-V1 was my first attempt at building the features of the previous prototypes into an application that utilises a UI. The data handling of the diary entries is almost identical to that of PD2, with only a few minor differences to account for the fact that it is a UI application rather than a console one.

The GUI was built using Python’s Tkinter module, which allows a user to build user interfaces using a range of widgets and grid functionality. GUI-V1 has a home page with a main menu, which has four buttons that each lead to another page (or more precisely, a different “frame”) of the application (add new entry, view current entries, delete entry and help/readme).

The “Add New Entry” page allows the user to enter a title, date and main body of text and then hit a “submit” button which submits the entry to the JSON file. The “View Saved Entries” page lists each of the entries as label widgets in a central frame container, and has an entry field allowing the user to enter the name of an entry and hit a “submit” button, which then opens a new frame that allows the user to read the selected entry. The “Delete Entry” page is aesthetically similar to the “View Saved Entries” page, expect that when the user enters a name and hits “submit”, instead of taking the user to the article, the entry is deleted from the JSON file. The “Help/Readme” page features some simple information pertaining to the use of the program.
