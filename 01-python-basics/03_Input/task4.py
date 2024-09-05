'''
Lots of websites use chatbots to interact with their customers.  These chatbots are often very sophisticated and use AI to learn and adapt to the user. 
Our chat bot is going to be a bit simpler. We will write a simple chatbot that helps users to generate an add to sell their used car.
'''

# The chatbot should work like this:
# - Ask the user for the make and model of the car
print("What is the model of the car?")
model = input()
# - Ask the user for the mileage of the car
print("What is the mileage of the car?")
mileage = input()
# - Ask the user for the price of the car
print("What is the price of the car?")
price = input()
# - Ask the user for the power of the car
print("What is the horsepower of the car?")
power = input()
# - Ask the user for the contact information (name, email address)
print("What is your information: name and email")
ContactInformation = input()
# - Output the add for the car'
print(f'{model} for sale, only {price} for a car that has only run {mileage} miles, the car has {power} horsepower. Please contact {ContactInformation} for more info!')

# Write your code here
