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

Prototype 3 - ProtoDiaryGUI-V1 "Fallout"

GUI-V1 was my first attempt at building the features of the previous prototypes into an application that utilises a UI. The data handling of the diary entries is almost identical to that of PD2, with only a few minor differences to account for the fact that it is a UI application rather than a console one.

The GUI was built using Python’s Tkinter module, which allows a user to build user interfaces using a range of widgets and grid functionality. GUI-V1 has a home page with a main menu, which has four buttons that each lead to another page (or more precisely, a different “frame”) of the application (add new entry, view current entries, delete entry and help/readme). The theme I went for was that of black and a moderate green tone, to emulate something similar to the terminals in the Fallout games or The Matrix.

The “Add New Entry” page allows the user to enter a title, date and main body of text and then hit a “submit” button which submits the entry to the JSON file. The “View Saved Entries” page lists each of the entries as label widgets in a central frame container, and has an entry field allowing the user to enter the name of an entry and hit a “submit” button, which then opens a new frame that allows the user to read the selected entry. The “Delete Entry” page is aesthetically similar to the “View Saved Entries” page, expect that when the user enters a name and hits “submit”, instead of taking the user to the article, the entry is deleted from the JSON file. The “Help/Readme” page features some simple information pertaining to the use of the program.

Prototype 4 - ProtoDiaryGUI-V2 "Aero"

The second of the GUI prototypes, for "GUI-V2, or "Aero" I decided to go with a completely fresh, clean-sheet codebase, making use of the experience of building GUI-V1 but not directly copying and pasting anything over. The theme I went for with this one was that of "Frutiger Aero" - vibrant blues and greens harkening back to an early-2000's, nostalgic Windows XP-esque aesthetic.

For this one, the code is much cleaner and more functional than that of GUI-V1. All of the "pages" (technically "frames") are wrapped in functions this time, and a lot more care was taken to make sure that the code was more maintainable and efficient than GUI-V1 - everything refreshes as it should now. I managed to implement a few things that I wished to implement from the beginning - viewing entries is now managed by simply clicking the entry as a button rather than having to type the title in and hit a "submit" button. The delete functionality remains the same, but I am going to change this in the next prototype, but one big improvement to this is that the deleted entry disappears from the list of entries immediately after being deleted. The big text sections are also now in a "word wrap" which means that words aren't splitting when it gets to the end of the box and onto a new line.

Overall, "Aero" is a marked improvement on GUI-V1.

Prototype 5 - ProtoDiaryGUI-V3 "Honeycomb"

The third GUI prototype, for GUI-V3 I decided to go for a "Honeycomb" theme of oranges, yellows, reds and blacks, at least for the most part. Perhaps this was due to it being around the time just after Halloween when I made it, but I think it's an interesting theme.

Unlike the leap from GUI-V1 to GUI-V2, I was able to copy my work for GUI-V2 directly for this one, since it was very tidy compared to GUI-V1. However, I've been able to make major improvements with V3. 

The delete functionality is now also simply a button press, although the button is much smaller than that of the "view entries" buttons, but nonetheless it's made the process of deleting entries significantly less clunky. I've also added "Exit" buttons to every page of the program, allowing the user to seamlessly exit the program from any page.

I've also started to incorporate other forms of multimedia with this version, with an "Audio Entries" page where .mp3 files stored in an "Audio Entries" folder can be played in an audio interface built using Tkinter and Pygame, which includes the ability to load an audio entry by pressing the button of the entry you wish to play, which is then placed in an audio interface including play, stop, pause and unpause buttons as well as volume buttons. There is also a page dedicated to adding audio entries, allowing the user to either open the Audio Entries folder and drag and drop a pre-made .mp3 audio file in, or to record an entry using an in-built recording system in the app. As of V3, this is still yet to be refined somewhat.

I would say that overall "Honeycomb" is a little less of a leap than what was made from V1 to V2, but nonetheless the inclusion of audio entries as well as refinements to the text entry pages make it a good improvment nonetheless.

Prototype 6 - ProtoDiaryGUI-V4 "Mystery"

The fourth GUI prototype (well, essentially version at this point) will set the goal of bringing image and video entries to the Python Personal Diary app. The theme is "Mystery" - red/maroon, black and grey tones set the mood of a retro adventure horror.

# --- This prototype is currently under construction --- #
