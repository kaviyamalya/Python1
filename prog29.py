##Programs with list and tuples

students = [("kaviya", [90, 85, 95]),
            ("malya", [80, 75, 70]),
            ("siva", [95, 90, 92])]


print("List of students and their grades:")
for student in students:
    print(student[0] + ":", student[1])


averages = []
for student in students:
    grades = student[1]
    average = sum(grades) / len(grades)
    averages.append((student[0], average))


print("\nList of students and their average grades:")
for average in averages:
    print(average[0] + ":", average[1])
