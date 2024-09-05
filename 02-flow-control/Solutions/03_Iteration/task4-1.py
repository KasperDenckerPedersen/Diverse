'''
In this make task, we will write a program that hacks the 4 digit pin of your phone. 
You query the user for his/her pin and store it in a variable. 
Subsequently, your program should start iterating over all possible 4 digit passwords until it guessed your pin correctly. 
The program should print the correct password as well as the number of iterations it took for it to guess it.
Bonus: How much longer would it take to guess a 6 digit pin?
'''

pin = 9674

counter = 1
guess = 0
while guess != pin:
    guess += 1
    counter += 1
print(f'Your pin is {guess}')
print(f"Total tries: {counter}")

# Variante 2
# counter = 0
# for guess in range(0, 10000):
#     counter += 1
#     if guess == pin:
#         print(f'Your pin is {guess}')
#         break

# print(f"Total tries: {counter}")