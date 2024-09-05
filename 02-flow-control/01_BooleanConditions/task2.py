number = 5
print("I have thought of a number between 1 and 10")
guess = input("Can you guess what it is?\n")

print(f"You guessed the number {guess}. This answer is {guess == number}")


# What happens if you input the guess 2?
  # Answer
  #False

# What happens if you input the guess 6?
  # Answer
  #False

# What happens if you input the guess 5?
  # Answer
  #Error since it is a string

# Why might this behavior be unexpected? 
  # Answer