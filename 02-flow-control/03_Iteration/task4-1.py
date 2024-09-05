'''
In this make task, we will write a program that hacks the 4 digit pin of your phone. 
You query the user for his/her pin and store it in a variable. 
Subsequently, your program should start iterating over all possible 4 digit passwords until it guessed your pin correctly. 
The program should print the correct password as well as the number of iterations it took for it to guess it.
Bonus: How much longer would it take to guess a 6 digit pin?
'''

Code = int('0003') #This is for the code to look nice when considering numbers with 0 in the first digit.
count = 0

for i in range(0, 10000):
    count += 1
    if i == Code:
        check = i
        break
print(f"You hacked the code, it is {check:04}. It took {count} iterations.")

pin = "5312"
tries = 0
for i in range(0,4):
    digit = int(pin[i])
    for guess in range(0,10):
        tries += 1
        if guess == digit:
            print(guess)
            break
print(f'It took{tries} tries to get it')


