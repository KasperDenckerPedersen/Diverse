# Add comments to this code to explain how it works and predict what it will do.

def tip_calculator(price, percentage):
    tip = price * percentage
    total = price + tip
    print(f"You should tip €{tip} and pay a total of €{total}!")
    return tip, total

tipNew, totalNew = tip_calculator(25, 0.1)
