'''
In this make task, you should write a simple note taking program. It should wait for user input and do the following depending on it: 
1. All saved notes are loaded to a list noteBooks from the file notebook.txt
2. The user can enter a short message that is appended to the list noteBooks.
3. Show all notes
4: The notebook is stored in a file called notebook.txt and the program is terminated
'''

def print_menu():
    print("What do you want to do?: ")
    print("1. To load notes from file.")
    print("2. Add note")
    print("3. To show all notes.")
    print("4. Store notes in a file and terminate")
    choice = int(input("> "))
    return choice

def load_notes(notes):
    fileHandler = open("03_Files/notebooks.txt", "r")
    for note in fileHandler:
        notes.append(note[:-1])

    return notes

def add_notes(notes):
    note = input("Enter a note: ")
    notes.append(note)
    return notes

def show_notes(notes):
    for note in notes:
        print(note)
    return

def write_notebook(notes):
    fileHandler = open("03_Files/notebooks.txt", "w")
    for note in notes:
        fileHandler.write(note + "\n")
        fileHandler.close()

    return

noteBooks = []

while True:
    choice = print_menu()
    if choice == 1:
        noteBooks = load_notes(noteBooks)
        continue
    elif choice == 2:
        noteBooks = add_notes(noteBooks)
        continue
    elif choice == 3:
        show_notes(noteBooks)
        continue
    elif choice == 4:
        write_notebook(noteBooks)
        break
    else: 
        print("Not a valid input, try again.")
        continue
