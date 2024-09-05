# Write a program that queries the user to input a number x as well a number y. Print a message that tells the user if x is a multiple of y or not.
x = int(input("Enter the x number: "))
y = int(input("Enter the y number: "))

check = x % y == 1
print(f"Is {x} multiple of {y}, the answer is {check}")
