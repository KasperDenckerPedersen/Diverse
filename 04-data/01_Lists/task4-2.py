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

def generate_random_list():
    random_list = []
    while True:
        print("Choose an option:")
        print("1: Print the list")
        print("2: Add random numbers to the list")
        print("3: Remove duplicates from the list")
        print("4: Output the number of elements and average value")
        print("5: Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            print("List:", random_list)
        
        elif choice == '2':
            n = int(input("Enter the number of random numbers to add: "))
            new_numbers = [random.randint(0, 20) for _ in range(n)]
            random_list.extend(new_numbers)
            print(f"Added {n} random numbers to the list.")
        
        elif choice == '3':
            random_list = list(set(random_list))
            print("Duplicates removed.")
        
        elif choice == '4':
            count = len(random_list)
            average = sum(random_list) / count if count > 0 else 0
            print(f"Number of elements: {count}")
            print(f"Average value: {average:.2f}")
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice, please try again.")

generate_random_list()
