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
}

for student in grades:
    result = sum(grades[student].values()) / len(grades[student].values())
    print(f'{student}: {result:.2f}')
