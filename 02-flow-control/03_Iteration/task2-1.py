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
  # Answer

# What does '!=' mean?
  # Answer

# How can you tell which lines of code are inside the loop?
  # Answer

# How many times will the loop repeat?
  # Answer

# What has to happen to make the program run the last line of code?
  # Answer
