number = 5
print("I have thought of a number between 1 and 10")
guess = int(input("Can you guess what it is?\n"))

if guess == number: # Check if the user guessed the number 5 and output "Correct!" if True
  print("Correct!")
if guess < number: # Check if the user guessed a number smaller than 5 and output "Too Low!" if True
  print("Too Low!")
if guess > number: # Check if the user guessed a number bigger than 5 and output "Too High!" if True
  print("Too High!")

  
  