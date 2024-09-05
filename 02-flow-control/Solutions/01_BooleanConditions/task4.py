# Write a program that queries the user to input a number x as well a number y. Print a message that tells the user if x is a multiple of y or not.

x = int(input('x:>'))
y = int(input('y:>'))

condition = x % y == 0

print(f'x is a multiple of y: {condition}')