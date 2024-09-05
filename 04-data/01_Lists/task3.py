'''
Modify the code to build a program that allows a user to chose between different options. 
Option 1 should show all the available video games in the list. 
Option 2 should allow the user to enter the name of a video game and add it to the list if it is not already there. 
Option 3 should allow the user to enter the index of a game and delete it
'''
def get_choice():
    print("")
    print("Enter a number for your choice.")
    print("1. Show all")
    print("2. Add new name")
    print("3. Delete a name")
    print("4. Exit")
    print("")
    choice = int(input())
    return choice

videoGames = ["Mario", "Sonic", "Joust", "Zelda"]


while True:
    choice = get_choice()
    if choice == 1:
        print(videoGames)
        continue
    elif choice == 2:
        newGame = input("Enter the name:\n>")
        if newGame in videoGames:
            print("Sorry! This game is already on the list.")
            continue
        videoGames.append(newGame)
        print(f"The new list is now:\n{videoGames}")
        continue

    elif choice == 3:
        print("Enter the index of the name you want to delete")
        index = int(input())
        if index in videoGames:
            del videoGames[index]
            print(f"The new list is now:\n{videoGames}")
            continue
        else:
            print(f"The index {index} is not on the list")
            continue
    elif choice == 4:
        print("Goodbye")
        break
    else:
        print("PLease provide one of the following numbers!")
        continue