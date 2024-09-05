'''
Adapt the code to create a guessing game. Your game should ask the user for a username and greet him/her personally. 
Additionally, it should report a score (the number of guesses needed to guess the number correctly) at the end of the round. 
When the round is finished, your game should ask the user if he/she wants to play again.
'''
def play_game():
    import random
    count = 1
    randomNumber = random.randint(1, 50)
    guess = int(
        input("I selected a secret number between 1 and 50. Try to guess it:\n>"))

    while guess != randomNumber:
        if guess < randomNumber:
            guess = int(input("Wrong - your number is to small! Guess again.\n>"))
            count += 1
        if guess > randomNumber:
            guess = int(input("Wrong - your number is to big! Guess again.\n>"))
            count +=1

    print(f"Good job! You guessed {randomNumber} correctly\nYour number of guesses were {count}")

name = input("Hello!\nWhat is your name? ")
print(f"Nice too meet you {name}")

play_game()

for i in [1,2,3,4,5,6,7,8,9]:
    play_again = input("That was a great game!\nDo you wanna play again? ")
    if play_again == "Yes":
        play_game()
    else:
        break
print("Have a good day!\nHope to play again soon.")
