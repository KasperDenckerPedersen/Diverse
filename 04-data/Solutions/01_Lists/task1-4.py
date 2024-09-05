# Add comments to this code to explain how it works and predict what it will do.

creditCardLimit = 5000 # Define the credit card limit
transactions = [] # Create an empty list to store the transactions

while True: # Keep the program running
  price = int(input('How much do you want to pay?\n')) # Ask the user for the amount to pay
  if creditCardLimit >= sum(transactions) + price: # Check if the sum of the previous transaction and the price are lower or equal to the credit card limit
    print("Thanks for shopping with us!") # Thank the user
    transactions.append(price) # Append the new price to the dictionary
  else: # If the sum of transactions + the price would exceed the limit
    print('Sorry, your card got rejected!') # Tell the user that the card got rejected
    break # Stop the program

print(f'You spend a total of {sum(transactions)} this month.') # Tell the user the total of all transaction