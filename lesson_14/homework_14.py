
class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.average_score = 0

    def set_average_score(self, value):
        self.average_score = value


new_student = Student("Jon", "Travolta", 55)
print(f"New student with name {new_student.name} created - average score is {new_student.average_score}")
print("Changing average score to 100...")
new_student.set_average_score(100)
print(f"Student with name {new_student.name} has new average score: {new_student.average_score}")

