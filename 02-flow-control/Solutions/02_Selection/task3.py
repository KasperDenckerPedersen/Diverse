# Adapt the code:
#  - Add a line of code asking the user to enter a third number
#  - Add if/elif/else statements to confirm whether the third number is bigger/smaller/the same as the first number and whether it is bigger/smaller/the same as the second number


n1 = int(input("Please enter a number:\n>"))
n2 = int(input("Please enter another number\n>"))
n3 = int(input("Please enter another number\n>"))

if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print("n1 > n2 > n3")
        elif n2 < n3:
            print("n1 > n3 > n2")
        else:
            print("n1 > n2 = n3")
    elif n1 < n3:
        print("n3 > n1 > n2")
    else:
        print("n1 = n3 > n2")
elif n2 > n1:
    if n1 > n3:
        print("n2 > n1 > n3")
    elif n1 < n3:
        if n3 > n2:
            print("n3 > n2 > n1")
        elif n2 > n3:
            print("n2 > n3 > n1")
        else:
            print("n2 = n3 > n1")
    else:
        print("n2 > n1 = n3")   
else:
    if n1 > n3:
        print("n1 = n2 > n3")
    elif n1 < n3:
        print("n3 > n1 = n2")
    else:
        print("n2 = n1 = n3")
