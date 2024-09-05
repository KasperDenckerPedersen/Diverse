'''
In this make task we will write a program that simulates an encounter with a zombie in an RPG. 
To this end, you should first create a list of possible weapons. 
Second you should create a variable zombieWeakness that is randomly assigned to one of the weapons in you list. 
Output a message telling the user that they have encountered a zombie and should prepare to fight. 
Output the list of weapons to the user.  Ask if they want to type 1 to use a random weapon from the list or 2 to pick their own weapon. 
If the weapon picked matches the zombieWeakness, output a message telling the user that they have won the fight.  
Otherwise output a message saying that they have lost.
'''

import random
import time

def spawn_zombie(weapons):
    weakness = random.choice(weapons)
    return weakness

def select_weapon(weapons):
    print('1. Select a random weapon')
    print('2. Select weapon manually')
    choice = int(input('>'))
    if choice == 1:
        weapon = random.choice(weapons)
    else:
        print('Select one of following weapons (by index)')
        for i in range(len(weapons)):
            print(f'{i}: {weapons[i]}')
        weaponIndex = int(input('>'))
        weapon = weapons[weaponIndex]

    return weapon

def get_winner(zombie, player):
    print("\U0001F94A\U0001F94A\U0001F94A Let's get ready to rumble \U0001F94A\U0001F94A\U0001F94A")
    for i in range(5, -1, -1):
        print(i)
        time.sleep(1)
    if zombie == player:
        winner = 'player'
    else:
        winner = 'zombie'
    return winner

def playGame(weapons):
    zombieWeaknesses = spawn_zombie(weapons)
    print('You encountered a zombie. Get ready to fight!!!')
    playerWeapon = select_weapon(weapons)
    winner = get_winner(zombieWeaknesses, playerWeapon)
    if winner == 'player':
        print(f'You destroyed the zombie with your {playerWeapon}')
    else:
        print(f"Your {playerWeapon} had no chance against that zombie's {zombieWeaknesses} weakness")



availableWeapons = ['\U0001F52B Gun \U0001F52B', '\U0001F52A Knife \U0001F52A', '\U0001FA93 Axe \U0001FA93', '\U0001F525 Flamethrower \U0001F525']
playGame(availableWeapons)