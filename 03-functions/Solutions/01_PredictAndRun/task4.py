# Add comments to this code to explain how it works and predict what it will do.

def tip_calculator(price, percentage): # Define function with 2 arguments
    tip = price * percentage
    total = price + tip
    print(f"You should tip €{tip} and pay a total of €{total}!")
    return tip, total

tipNew, totalNew = tip_calculator(25, 0.1) # Call function using 25 as argument for price and 0.1 as argument for percentage. Assign the returned values to the two variables
