# Add comments to this code to explain how it works and predict what it will do.

answer = input("What is the capital of France?\n> ")

while answer != "Paris":
  print("Incorrect! Try again.")
  answer = input("What is the capital of France?\n> ")

print("Correct!")