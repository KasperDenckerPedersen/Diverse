# Lots of websites use chatbots to interact with their customers.  These chatbots are often very sophisticated and use AI to learn and adapt to the user. Our chat bot is going to be a bit simpler. We will write a simple chatbot that helps users to generate an add to sell their used car.

# The chatbot should work like this:
# - Ask the user for the make and model of the car
# - Ask the user for the mileage of the car
# - Ask the user for the price of the car
# - Ask the user for the power of the car
# - Ask the user for the contact information (name, email address)
# - Output the add for the car

print('Willkommen zum Anzeigenkonfigurator!')
make = input('Marke: ')
model = input('Model: ')
mileage = input('Laufleistung: ')
price = input('Preis: ')

print(2*'\n')
print(4*'\U0001F911' + ' SUPER ANGEBOT ' + 4*'\U0001F911')
print(f'Marke: {make}')
print(f'Modell: {model}')
print(f'Laufleistung: {mileage}km')
print(f'Preis: {price}€')
print(15*'\U0001F911')
