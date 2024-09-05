'''
In this make task, we will code our own simple calculator. 
You program should have 4 functions that add, subtract, multiply or divide two integer number arguments. 
The user is asked to input two numbers. These numbers will be passed as arguments into one of the subroutines. 
The user is asked to input 1 to add, 2 to subtract, 3 to multiply and 4 to divide. Output the returned result as part of a sentence.
'''

num1 = int(input("Number 1: "))
num2 = int(input("Number 2: "))
num3 = int(input("1 for add, 2 for subtract, 3 for multiply and 4 for divide: "))

def add(num1, num2):
    return num1 + num2

def minus(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

if num3 == 1:
    print(f" {num1} plus {num2} is {add(num1, num2)}")
elif num3 == 2:
    print(f" {num1} minus {num2} is {minus(num1, num2)}")
elif num3 == 3:
    print(f" {num1} multiplied by {num2} is {multiply(num1, num2)}")
elif num3 == 4:
    print(f" {num1} divided by {num2} is {divide(num1, num2)}")
else:
    print("Please try again!")