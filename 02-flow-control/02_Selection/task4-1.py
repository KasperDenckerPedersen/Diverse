'''
In this make task, we will create a program called "Task Grader". The program should allow the user to enter a test mark between 1 and 100. 
If the number entered is too high or too low, a message should be displayed informing the user of this. 
Create a variable called fail and assign the value "Y" to it if the test result is less than 40 and "N" otherwise. 
Check the value of fail and informs the user if a retake is required. 
Upgrade your program to also print out the grades as follows: under 40: "U", 40-59: "C", 60-79: "B", 80 or more: "A"
'''

Test_Mark = int(input("Enter your test mark: "))
grade = "No Data"

if Test_Mark < 1:
    print("The test mark entered is too low")
elif Test_Mark > 100:
    print("The test mark is too high")
else:
    if Test_Mark < 40:
        grade = "U"
    elif Test_Mark < 60:
        grade = "C"
    elif Test_Mark < 80:
        grade = "B"
    else:
        grade = "A"
    print(f"Your test mark of {Test_Mark}, gives you the grade of {grade}")