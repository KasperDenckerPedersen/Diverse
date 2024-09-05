'''
Modify the code to tell the user to input a country. Store it in a variable. Call the function with the variable as the argument. 
Additionally, give the function a sensible name.
'''

def print_country(country):
    print("I am from " + country)

userCountry = input("Where are you from?\n>")

print_country(userCountry)