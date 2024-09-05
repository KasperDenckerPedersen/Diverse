'''
In this make task we will write our own phonebook. First, your should create an empty dictionary called phoneBook. 
Subsequently, you should ask the user to press: 
1. to add an entry to the phonebook (name, phone number, email) and store it in the dictionary (you might want to nest multiple dictionaries). 
If the users presses 2, the program should show all available contacts. 
If the user presses 3, the program should ask the user for a contact name and show all the information for this contact. 
If the user presses 4, the program should be terminated
'''

phonebook = {}

while True:
    print("--------Opening phonebook--------")
    print("\nWhat do you want to do?:\n")
    choice = int(input("Add new contact: 1\nShow all contacts: 2\nSearch by name: 3\nExit: 4\n>"))
    if choice == 1:
        name = input("Type the name: ")
        phonenumber = float(input("Type the phone number: "))
        email = input("Type the email: ")
        phonebook[name] = phonenumber, email
        continue
    elif choice == 2:
        print(phonebook)
        continue
    elif choice == 3:
        searchName = input("What name should be searched for?: ")
        if searchName in phonebook.keys():
            print(f"This is found by {searchName}:\n{phonebook[name]}\n")
        else:
            print("This name does not exist in the phonebook.")
            while True:
                choice2 = input("Want to search for a new name? Y or N")
                if choice2 == "Y":
                    continue
                else: 
                    break
            continue
    elif choice == 4:
        print("--------Closing phonebook--------")
        break
    else:
        print("Please try again")
        continue
