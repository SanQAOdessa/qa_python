from faker import Faker
import pytest
import random

from lesson_22.my_university_db import MyUniversityDB

def test_my_university():
    my_db = MyUniversityDB()
    # clear data
    my_db.clear_database()

    #generate test data
    fake = Faker()
    students = []
    for _ in range(20):
        name = fake.first_name()
        age = random.randrange(18, 100)
        my_db.create_student(name, age)
        students.append({"name": name, "age": age})
    # fake = Faker()
    courses = []
    for _ in range(5):
        name = fake.street_name()
        my_db.create_course(name)
        courses.append({"name":name})
    # course without students
    with_out_student_course = fake.street_name()
    my_db.create_course(with_out_student_course)

    # add student to random courses
    for student in students:
        course_for_choice = courses.copy()
        for _ in range(3):
            course = random.choice(course_for_choice)
            course_for_choice.remove(course)
            my_db.set_student_to_course(student["name"], student["age"], course['name'])

    # check course name without students
    assert with_out_student_course in my_db.get_empty_courses()

    # print students in selected course
    print(f"\n ----- Students in course {courses[0]['name']}:")
    students_count = 0
    for student in my_db.get_students_by_course(courses[0]['name']):
        print(f"Name: {student.name}, age: {student.age}")
        my_db.update_student(student.name, student.age, student.name+'--', student.age+10)

        students_count += 1
    print(f'total students in course is: {students_count}')

    # print edited students names and ages
    print(f"\n ----- Students in course {courses[0]['name']}:")
    students_count = 0
    for student in my_db.get_students_by_course(courses[0]['name']):
        print(f"Name: {student.name}, age: {student.age}")
        if random.choice([0, 0, 1]): # delete random students from course
            my_db.delete_student_from_course(student.name, student.age, courses[0]['name'])
        students_count += 1
    print(f'total students in course is: {students_count}')

    # print students names and ages without deleted from course
    print(f"\n ----- Students in course {courses[0]['name']}:")
    students_count = 0
    for student in my_db.get_students_by_course(courses[0]['name']):
        print(f"Name: {student.name}, age: {student.age}")

        students_count += 1
    print(f'total students in course is: {students_count}')

    # validate students in empty course
    assert not my_db.get_students_by_course(with_out_student_course), \
        f'Unexpected student in course {with_out_student_course}'