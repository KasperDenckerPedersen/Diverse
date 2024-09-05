# Adapt the code to calculate the average of all values in the list

sum = 0
count = 0
for value in [3, 15, 2, 7, 4, 10]:
    sum += value #sum = sum + 1
    count += 1 #count = count + 1

average = sum/count

print(f"The sum of all values in the list is: {sum}")
print(f'The average is {average:.2f}')

