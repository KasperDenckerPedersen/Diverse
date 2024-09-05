'''
In this make task, you should write a program that generates a list of random numbers between 0 and 20. 
To this end, your program should first create an empty list. 
Subsequently, wait for user input. If the user presses 1, the program should print the list. 
If the user presses 2, the program should ask for a number n and add n random numbers to the list. 
If the user presses 3, the program should remove all duplicated values from the list. 
If the user presses 4, the program should output the number of elements in the list as well as the average value of all numbers in the list. 
If the user presses 5, you program should stop.
'''
import random

def print_menu():
    print('1. Print the list')
    print('2. Add numbers')
    print('3. Remove duplicates')
    print('4. Summary')
    print('5. Quit')
    choice = int(input())
    return choice

def show_list(numbers):
    for number in numbers:
        print(number)

def add_numbers(numbers):
    n = int(input('How many numbers you want do add: '))
    for i in range(n):
        randomNumber = random.randint(0, 20)
        numbers.append(randomNumber)
    return numbers


def remove_duplicates(numbers):
    numbers2 = []
    for number in numbers:
        if number not in numbers2:
            numbers2.append(number)
    return numbers2


def summary(numbers):
    length = len(numbers)
    average = sum(numbers)/length
    print(f'Number of elements: {length}, Average value: {average}')


numbers = []

while True:
    choice = print_menu()
    if choice == 1:
        show_list(numbers)
    elif choice == 2:
        numbers = add_numbers(numbers)
    elif choice == 3:
        numbers = remove_duplicates(numbers)
    elif choice == 4:
        summary(numbers)
    elif choice == 5:
        break