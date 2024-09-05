number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?\n"))

if guess == number:
  print("Correct!")
if guess < number:
  print("Too Low!")
if guess > number:
  print("Too High!")