'''
In this make task, you should write a simple note taking program. It should wait for user input and do the following depending on it: 
1. All saved notes are loaded to a list noteBooks from the file notebook.txt/csv
2. The user can enter a short message that is appended to the list noteBooks.
3. Show all notes
4: The notebook is stored in a file called notebook.txt and the program is terminated
'''

def print_menu():
    print('1. Load notes from file')
    print('2. Add note')
    print('3. Show notes')
    print('4. Save and quit')
    choice = int(input('> '))
    return choice

def add_notes(notes):
    note = input('Enter note: ')
    notes.append(note)
    return notes

def show_notes(notes):
    for note in notes:
        print(note)


def write_notebook(notes):
    fileHandler = open('03_Files/notebooks.txt', 'w')
    for note in notes:
        fileHandler.write(note + '\n')
    fileHandler.close()

def load_notes(notes):
    fileHandler = open('03_Files/notebooks.txt', 'r')
    for note in fileHandler:
        notes.append(note[:-1])
    return notes


noteBooks = []

while True:
    choice = print_menu()
    if choice == 1:
        noteBooks = load_notes(noteBooks)
    elif choice == 2:
        noteBooks = add_notes(noteBooks)
    elif choice == 3:
        show_notes(noteBooks)
    elif choice == 4:
        write_notebook(noteBooks)
        break
    else:
        print('Invalid choice')

