# Adapt the code:
#  - Add a line of code asking the user to enter a third number
#  - Add if/elif/else statements to confirm whether the third number is bigger/smaller/the same as the first number and whether it is bigger/smaller/the same as the second number

number1 = int(input("Please enter a number"))
number2 = int(input("Please enter another number"))
number3 = int(input("Please enter a third number"))

if number1 > number2:
  print("Number 1 is bigger than number 2")
elif number2 > number1: 
  print("Number 2 is bigger than number 1")
elif number3 > number1:
  print("Number 3 is larger than number 1")
elif number3 > number2:
  print("Number3 is larger than number 2")
else:
  print("All numbers are the same")