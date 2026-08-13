student ={
    "name": "RYAN",
    "age": 20,
    "grades": {"MATH": 85, "SCIENCE": 90, "ENGLISH": 78, "HISTORY": 92, "ART": 88}
}
# def Average(student):
#     grades = student["grades"]
#     total = sum(grades.values())
#     average = total / len(grades)
#     return average
# average_grade = Average(student)
# print(f"The average grade for {student['name']} is: {average_grade}")
def average_grade(student):
    grades = student["grades"]   # assume grades is a list: [85, 90, 78, 92]
    total = 0
    for grade in grades.values():
        total += grade
    return total / len(grades)
average = average_grade(student)
print(f"The average grade for {student['name']} is: {average}")