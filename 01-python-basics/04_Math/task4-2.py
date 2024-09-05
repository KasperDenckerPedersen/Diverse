'''
Create a program that allows the user to enter the price of a meal at a restaurant as well as the percentage that you want to tip. 
The program calculates the amount of the tip to be paid. The price, the tip and the total price are then displayed separately.
'''

Price = float(input("Enter the price of the meal: "))
Tip_Perc = float(input("Enter tip percentage in a integer number: "))

Tip_Perc = Tip_Perc/100

Total_Tip = Tip_Perc*Price

Total_Price = Total_Tip + Price

print(f'The tip for the meal is {Total_Tip} which gives a total price of {Total_Price:.2f}') #The :.2f indicates we want to digits on the total price