# Add comments to this code to explain how it works and predict what it will do.

grades = {'Mike': -3, 'Sandra': 12, 'Josh': 10, 'Anna': 7}
#print(grades.items())

for key, value in grades.items():
    print(f'{key}: {value}')

print(sum(grades.values()) / len(grades.values()))
