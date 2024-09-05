# Add comments to this code to explain how it works and predict what it will do.

grades = { 
    'Mike': {
        'Finance': 12,
        'Marketing': 3,
        'Math': 0,
        'Economics': 10
    },
    'Sara': {
        'Finance': 10,
        'Programming': 12,
        'Econometrics': 3
    },
    'Julia': {
        'Marketing': 12,
        'Accounting': -3,
        'Programming': 10,
        'Finance': 7
    },
    'John': {
        'Project Management': 7,
        'Math': 12,
        'Economics': 3,
        'Econometrics': 10
    }
} # Create a nested dictionary. The outer dictionary has the names as keys and dictionaries as values. The inner dictionaries have the subjects as keys and the grades as values

for student in grades: # Iterate over the keys of the dictionary
    result = sum(grades[student].values()) / len(grades[student].values()) # Calculate the average grade for each student 
    print(f'{student}: {result:.2f}') # Print the name and the average grade for each student