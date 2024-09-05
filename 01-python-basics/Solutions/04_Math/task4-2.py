'''
Create a program that allows the user to enter the price of a meal at a restaurant as well as the percentage that you want to tip. 
The program calculates the amount of the tip to be paid. The price, the tip and the total price are then displayed separately.
'''

price = float(input("Price: "))
tip = float(input("Tip (in %): "))

totalTip = price * tip/100

total = price + totalTip

print()
print(f'Price: {price:.2f}')
print(f'Tip: {totalTip:.2f}')
print(10*'-')
print(f'Total: {total:.2f}')

print()
print(f'Price: {price:.2f}\nTip: {totalTip:.2f}\n{10*"-"}\nTotal: {total:.2f}')