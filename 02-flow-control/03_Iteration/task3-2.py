# Adapt the code to calculate the average of all values in the list

sum = 0
count = 0
for value in [3, 15, 2, 7, 4, 10]:
  sum = sum + value
  count += 1

if count > 0: #Only here if the list is empty, then it still outputs something
  average = sum / count
  print(f"The sum of all values in the list is: {sum}\nThe average of all values in the list is: {average}")
else:
  print("Error")
  

