# Modify the code to build a program that calculates the average grade for each class instead of each student

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

# class_grades = {}

# for student, studies in grades.items():
#     for studies, grade in studies.items():
#         if studies not in class_grades:
#             class_grades[studies] = []
#         class_grades[studies].append(grade)

# for studies, grades in class_grades.items():
#     average_grade = sum(grades) / len(grades)
#     print(f'{studies}: {average_grade:.2f}')

gradesCount = {}
gradesTotal = {}
for student in grades.keys():
    for course in grades[student].keys():
        gradesCount[course] = gradesCount.get(course, 0) + 1
        gradesTotal[course] = gradesTotal.get(course, 0) + grades[student][course]

for course in gradesCount.keys():
    gradesAverage = gradesTotal[course] / gradesCount[course]
    print(f"{course}: {gradesAverage:.2f}")