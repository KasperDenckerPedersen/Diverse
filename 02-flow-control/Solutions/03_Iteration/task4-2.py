'''
In this make task, we will write a program that calculates the Fibonacci sequence up to the n-th term. 
A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8.... The first two terms are 0 and 1. 
All other terms are obtained by adding the preceding two terms. This means to say the nth term is the sum of (n-1)th and (n-2)th term.
Your program should ask a user how many terms he/she wants to calculate and output the respective Fibonacci sequence.
''' 

nFib = int(input("Length: "))

if nFib < 1:
    print('Error')
elif nFib == 1:
    print(0)
elif nFib == 2:
    print(0)
    print(1)
else:
    n1 = 0
    n2 = 1
    print(n1)
    print(n2)
    for i in range(2, nFib):
        n3 = n1 + n2
        print(n3)
        n1 = n2
        n2 = n3