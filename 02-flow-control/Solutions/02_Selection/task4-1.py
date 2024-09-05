'''
In this make task, we will create a program called "Task Grader". The program should allow the user to enter a test mark betwenn 1 and 100. 
If the number entered is too high or too low, a message should be displayed informing the user of this. 
Create a variable called fail and assign the value "Y" to it if the test result is less than 40 and "N" otherwise. 
Check the value of fail and informs the user if a retake is required. 
Upgrade your program to also print out the grades as follows: under 40: "U", 40-59: "C", 60-79: "B", 80 or more: "A"
'''

points = int(input("Points:>"))

if points > 100:
    print('Points to high - enter a number between 1 and 100')
elif points < 1:
    print('Points to low - enter a number between 1 and 100')
else:
    if points >= 80:
        grade = 'A'
    elif points >= 60:
        grade = 'B'
    elif points >= 40:
        grade = 'C'
    else:
        grade = 'U'
    print(f'Final grade: {grade}')
