number = 5
print("I have thought of a number between 1 and 10")
guess = input("Can you guess what it is?\n")

print(f"You guessed the number {guess}. This answer is {guess == number}")


# What happens if you input the guess 2?
  # False

# What happens if you input the guess 6?
  # False

# What happens if you input the guess 5?
  # False

# Why might this behavior be unexpected? 
  # We might expect the last question to return True. However it returns False as we compare the integer 5 with the string 5