##Implement dictionary

students = {"kaviya": 90,
            "malya": 80,
            "siva": 95}


print("Dictionary of students and their grades:", students)


alice_grade = students["kaviya"]
print("kaviya's grade:", alice_grade)

students["SKM"] = 85
print("Dictionary of students and their grades:", students)


students["malya"] = 85
print("Dictionary of students and their grades:", students)


del students["siva"]
print("Dictionary of students and their grades:", students)
