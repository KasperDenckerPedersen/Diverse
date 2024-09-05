'''
Write a program that asks the user for their name and which subject they are studying. 
The program should output a message telling the student by name which room to go to for that class (make up the room numbers if you need to). 
You should include at least 3 subjects and have a message such as "I don't know which room that class is in" for any you don't include.
Example - an input of "Ben" and "Computing" might get an output of "Hi Ben, go to room 401 for Computing"
'''

name = input("What is your name? ")
Study = input("What do you study? ").lower() # Or use .capatalize for first letter to always be capital.

if Study == "Economic":
    print(f"Hello {name}\n Go to room 1")
elif Study == "science":
    print(f"Hello {name}\nGo to room 2")
elif Study == "art":
    print(f"Hello {name}\nGo find a real study instead")
elif Study == "business":
    print(f"Hello {name}\nGo to room 3")
else:
    print(f"Hello {name}\nNo room for this study")