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
  # Answer

# Which functions did we use in our program?
  # Answer

# How often are the functions called?
  # Answer
