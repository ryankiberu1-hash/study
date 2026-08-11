class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"
    def average_grade(self):    
        try:
            return sum(self.grade.values()) / len(self.grade)
        except ZeroDivisionError:
            return 0    
    def is_passing(self,threshold=60):
        return self.average_grade() >= threshold
        
ryan = student("Ryan", 20, {"MATH": 90, "SCIENCE": 85, "ENGLISH": 88})
print(ryan)
print("Average Grade:", ryan.average_grade())
print("Is Passing:", ryan.is_passing())
with open("students.txt", "w") as f:
    f.write(f"Name: {ryan.name}, Age: {ryan.age}, Grade: {ryan.grade}\n")
empty_student = student("Empty", 0, {})
print(empty_student)