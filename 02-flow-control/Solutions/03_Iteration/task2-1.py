# Add comments to this code to explain how it works and predict what it will do.

password = 'Secure Password'
guess = input("Please enter your password:\n>")

while guess != password: 
  print("Your password is wrong!")
  again = input("Do you want to try it again?\n>")
  if again == "yes":
    guess = input("Please enter your password:\n>")
  else:
    print("Better luck next time!")
    break

if guess == password:
  print("Your login was successful")

# Give the line number where iteration starts.
  # 6

# What does '!=' mean?
  # unequal to

# How can you tell which lines of code are inside the loop?
  # They are indented

# How many times will the loop repeat?
  # Unknown - it is an indefinite loop and will iterate until the user guesses the correct password or tells it not to try again

# What has to happen to make the program run the last line of code?
  # The user has to guess the right password
