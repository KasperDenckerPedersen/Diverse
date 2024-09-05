'''
In this make task we will write a program that simulates an encounter with a zombie in an RPG. 
To this end, you should first create a list of possible weapons. 
Second you should create a variable zombieWeakness that is randomly assigned to one of the weapons in you list. 
Output a message telling the user that they have encountered a zombie and should prepare to fight. 
Output the list of weapons to the user.  Ask if they want to type 1 to use a random weapon from the list or 2 to pick their own weapon. 
If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
Otherwise output a message saying that they have lost.
'''

weapons = ["Sword", "Bow", "Spear", "Dagger"]
import random
Won_Games = 0

while True:
    zombieWeakness = random.randint(0, 3)
    print("You have encountered a zombie, prepare to fight!")
    choose_or_random = int(input("1. To choose your own, 2. to get one assigned: "))
    if choose_or_random == 1:
        print("0. for sword")
        print("1. for bow")
        print("2. for spear")
        print("3. for dagger")
        Choose_weapon = int(input("Choose your weapon:"))
        print(f"You have chosen the {weapons[Choose_weapon]}\n")
        if zombieWeakness == Choose_weapon:
            Won_Games += 1
            print(f"Contratz. The {weapons[Choose_weapon]} was the zombies weakness!\nYou have won the encounter\n")
            keep_going = input("Do you want to keep walking? Yes or No: ")
            if keep_going == "Yes":
                continue
            else:
                break     
        else: 
            print("The zombie was too strong!\nGame Over!")
            print("")
            Try_Again = input("Do you wanna try again? Yes or No: ")
            if Try_Again == "Yes":
                continue
            else:
                break

    elif choose_or_random == 2:
        random_weapon_assigned = random.randint(0, 3)
        print(f"You got the {weapons[random_weapon_assigned]}\n")
        if zombieWeakness == random_weapon_assigned:
            Won_Games += 1
            print(f"Contratz. The {weapons[random_weapon_assigned]} was the zombies weakness!\nYou have won the encounter\n")
            keep_going = input("Do you want to keep walking? Yes or No: ")
            if keep_going == "Yes":
                continue
            else:
                break     
        else: 
            print("The zombie was too strong!\nGame Over!")
            print("")
            Try_Again = input("Do you wanna try again? Yes or No: ")
            if Try_Again == "Yes":
                continue
            else:
                break

print(f"The amount of won games is {Won_Games}")


