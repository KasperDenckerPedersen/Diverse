import random

randomNumber = random.randint(1, 50)
guess = int(input("I selected a secret number between 1 and 50. Try to guess it:\n>"))

while guess != randomNumber:
  if guess < randomNumber:
    guess = int(input("Wrong - your number is to small! Guess again.\n>"))
  if guess > randomNumber:
    guess = int(input("Wrong - your number is to big! Guess again.\n>"))

print(f"Good job! You guessed {randomNumber} correctly")

# What will be the outputs of the program?
  # It will query the user to guess a number until the right number is guessed

# Which functions did we use in our program?
  # We used the Python functions int, input and print. Additionally, we import and use the function randint from the random library

# How often are the functions called?
  # randint and print once. The others unknown as the number of iterations in the loop is unknown before the program is run
