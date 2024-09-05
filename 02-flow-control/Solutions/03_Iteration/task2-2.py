largestNumber = -999

for number in [15, 1, 27, 38, 50, 179, 3]:
  if number > largestNumber:
    largestNumber = number
    print(f"{number} is the new largest number!")
print(f'The largest number in the list is: {largestNumber}')

# What is the objective of our code?
  # To find the largest number in the list

# For how many iterations will the code run?
  # 7 (it is a definite loop that will run once for every element in the list)

# What happens if we iterate over the list [15, 1, 27, 'Hello, world!']
  # We will receive an error as we cannot compare numbers (value in variable largestNumber) with strings ("Hello, world!")