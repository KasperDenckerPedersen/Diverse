'''
In this make task we will write our own phonebook. First, your should create an empty dictionary called phoneBook. 
Subsequently, you should ask the user to press: 
1. to add an entry to the phonebook (name, phone number, email) and store it in the dictionary (you might want to nest multiple dictionaries). 
If the users presses 2, the program should show all available contacts. 
If the user presses 3, the program should ask the user for a contact name and show all the information for this contact. 
If the user presses 4, the program should be terminated
'''


def printMenu():
    '''
    Print the menu and return the choice of the user
    '''
    print('\n')
    print(10*'-')
    print('1. Add entry')
    print('2. Show contacts')
    print('3. Search contacts')
    print('4. Exit')
    print(10*'-')
    choice = int(input())
    return choice

def addEntry(phoneBook):
    '''
    Add a new entry and return the updated dictionary phoneBook
    '''
    name = input('Name: ')
    number = input('Number: ')
    mail = input('Mail: ')
    if name in phoneBook.keys():
        print(10*'-')
        print('This name is already in your contacts')
        print(10*'-')
    else:
        phoneBook[name] = {'number': number, 'mail': mail}
    return phoneBook

def showContacts(phoneBook):
    '''
    Show all contacts
    '''
    print(10*'-')
    print('Contacts:')
    print(10*'-')
    for name in phoneBook.keys():
        print(name)
    print(10*'-')

def searchContact(phoneBook):
    '''
    Search for a contact by name and show details
    '''
    name = input('Name: ')
    if name in phoneBook.keys():
        print(10*'-')
        print(f'Name: {name}')
        print(f'Number: {phoneBook[name]["number"]}')
        print(f'Mail: {phoneBook[name]["mail"]}')
        print(10*'-')
    else:
        print(10*'-')
        print(f'{name} is not in your contacts')
        print(10*'-')

phoneBook = {}

while True:
    choice = printMenu()
    if choice == 1:
        phoneBook = addEntry(phoneBook)
    elif choice == 2:
        showContacts(phoneBook)
    elif choice == 3:
        searchContact(phoneBook)
    elif choice == 4:
        break
    else:
        print('Invalid choice. Try again')