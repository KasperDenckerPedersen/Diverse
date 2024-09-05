'''
In this make task, we will code our own simple calculator. 
You program should have 4 functions that add, subtract, multiply or divide two integer number arguments. 
The user is asked to input two numbers. These numbers will be passed as arguments into one of the subroutines. 
The user is asked to input 1 to add, 2 to subtract, 3 to multiply and 4 to divide. Output the returned result as part of a sentence.
'''

def add(x, y):
    return f'{x} + {y} = {x+y}'

def subtract(x,y):
    return f'{x} - {y} = {x-y}'

def multiply(x,y):
    return f'{x} * {y} = {x*y}'

def divide(x,y):
    return f'{x} / {y} = {x/y}'

def print_menu():
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiply')
    print('4. Divide')
    print('5. Shutdown')
    choice = int(input())
    return choice

while True:
    choice = print_menu()
    num1 = float(input('Number 1: '))
    num2 = float(input('Number 2: '))

    if choice == 1:
        result = add(num1, num2)
    elif choice == 2:
        result = subtract(num1, num2)
    elif choice == 3:
        result = multiply(num1, num2)
    elif choice == 4:
        result = divide(num1, num2)
    elif choice == 5:
        break
    else:
        result = 'Invalid choice'

    print(result)