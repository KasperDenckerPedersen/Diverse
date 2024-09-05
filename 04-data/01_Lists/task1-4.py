# Add comments to this code to explain how it works and predict what it will do.

creditCardLimit = 5000
transactions = []

while True:
  price = int(input('How much do you want to pay?\n'))
  if creditCardLimit >= sum(transactions) + price:
    print("Thanks for shopping with us!")
    transactions.append(price)
  else:
    print('Sorry, your card got rejected!')
    break

print(f'You spend a total of {sum(transactions)} this month.')