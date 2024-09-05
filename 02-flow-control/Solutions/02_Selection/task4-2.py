'''
Write a program that asks the user for their name and which subject they are studying. 
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to). 
You should include at least 3 subjects and have a message such as "I don't know which room that class is in" for any you don't include.
Example - an input of "Ben" and "Computing" might get an output of "Hi Ben, go to room 401 for Computing"
'''

name = input("Please enter your name:\n>")
subject = input("Please enter your subject:\n>")

if subject == "Programmieren für Wirtschaftswissenschaftler":
    print(f'Hi {name}! Go to room CIP2 for {subject}')
elif subject == "Datenmanagment und Analyse":
    print(f'Hi {name}! Go to room 414 for {subject}')
elif subject == "Data Science":
    print(f'Hi {name}! Go to room 210 for {subject}')
else:
    print(f"Hi {name}! I don't know which room that class is in")