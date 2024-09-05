# In our unit on variables, we wrote a program that assigns your first and your last name to 2 separate variables with suitable names and output your full name as well as your initials using one print statement.
# Modify the following code to allow the user to enter his/her first and last name.

fname = input("Enter first time: ")
lname = input("Enter last name: ")
nLetters = int(input("How many letters you want: "))

fullname = fname + " " + lname
initials = fname[:nLetters] + lname[:nLetters]

print(f"Hi {fullname}. Your initials are {initials}!")
