# Add comments to this code to explain how it works and predict what it will do.

answer = input("What is the capital of France?\n> ") # Ask the user for an input

while answer != "Paris": # Check if answer is paris -> if True jump to line 9 -> if False stay in the loop and ask for new input
  print("Incorrect! Try again.")
  answer = input("What is the capital of France?\n> ")

print("Correct!")