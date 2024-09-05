'''
In this make task, we will write a program that calculates the Fibonacci sequence up to the n-th term. 
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 0 and 1. 
All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.
Your program should ask a user how many terms he/she wants to calculate and output the respective Fibonacci sequence.
''' 
terms = int(input("How many terms of the Fibonacci sequence?: "))
n = 2
sequence = [0, 1]
a, b = 0, 1

if terms == 1:
    print(a)
elif terms == 2:
    print(a, b)
else:
    while n < terms:
        n += 1
        temp = a + b
        a = b
        b = temp
        sequence.append(temp)
    print(f"At term {terms}, the number in the fibonacci sequence is {temp}.\nThe sequence is: {sequence}")