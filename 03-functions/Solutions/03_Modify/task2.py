'''
Adapt the code to create a guessing game. Your game should ask the user for a username and greet him/her personally. 
Additionally, it should report a score (the number of guesses needed to guess the number correctly) at the end of the round. 
When the round is finished, your game should ask the user if he/she wants to play again.
'''

import random

def play_game(maxNumber):
    score = 1
    randomNumber = random.randint(1, maxNumber)
    guess = int(input(f"\U0001F92B\U0001F92B\U0001F92BI selected a secret number between 1 and {maxNumber}. Try to guess it \U0001F9D0\U0001F9D0:\n>"))

    while guess != randomNumber:
        score += 1
        if guess < randomNumber:
            guess = int(input("Wrong - your number is to small! Guess again.\n>"))
        elif guess > randomNumber:
            guess = int(input("Wrong - your number is to big! Guess again.\n>"))

    print(f"\U0001F973\U0001F973Good job! You guessed {randomNumber} correctly. It took your {score} tries.\U0001F973\U0001F973")


def set_difficulty():
    print('Please select the difficulty level.')
    print('1. Easy (1-10)')
    print('2. Medium (1-100)')
    print('3. Hard (1-1000)')
    print('4. Expert (1-100000)')
    choice = int(input('>'))
    if choice == 1:
        maxNumber = 10
    elif choice == 2:
        maxNumber = 100
    elif choice ==3 :
        maxNumber = 1000
    elif choice == 4:
        maxNumber = 100000
    else:
        print('Invalid choice - using default (100)')
        maxNumber = 100
    return maxNumber


def play_again(name):
    print(f'Hi {name}. Good luck in the game!')
    while True:
        maxNumber = set_difficulty()
        play_game(maxNumber)
        playAgain = input('Play again (y/n): ')
        if playAgain == 'n':
            break

# MAIN CODE
userName = input('Username: ')
play_again(userName)
