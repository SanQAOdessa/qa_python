from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, PrimaryKeyConstraint, update
from sqlalchemy.orm import sessionmaker, relationship, declarative_base


class MyUniversityDB:
    def __init__(self):
        engine = create_engine(self.DATABASE_URL)
        Session = sessionmaker(bind=engine)
        self.session = Session()
        self.Base.metadata.create_all(engine)

    DATABASE_URL = "postgresql+psycopg2://oleksandr:12345@localhost/university"
    Base = declarative_base()

    class Courses(Base):
        __tablename__ = "courses"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(200), nullable=False)
        # students = relationship('Student', back_populates='courses')
        students_courses = relationship('StudentsCourses', back_populates='courses')


    class Students(Base):
        __tablename__ = "students"
        id = Column(Integer, primary_key=True, autoincrement=True)
        name = Column(String(200))
        age = Column(Integer)
        students_courses = relationship('StudentsCourses', back_populates='students')
        def __repr__(self):
            return f"Student(name={self.name}, age={self.age})"

    class StudentsCourses(Base):
        __tablename__ = "students_courses"
        __table_args__ = (
            PrimaryKeyConstraint('student_id', 'course_id'),
        )
        student_id = Column(Integer, ForeignKey("students.id", ondelete='SET NULL'))
        course_id = Column(Integer, ForeignKey("courses.id", ondelete='SET NULL'))
        students = relationship('Students', back_populates='students_courses')
        courses = relationship('Courses', back_populates='students_courses')

    def create_student(self, name: str, age: int)->bool | int:
        is_student_exists = self.get_student_by_name_and_age(name, age)
        if is_student_exists:
            return is_student_exists

        new_student = self.Students(name=name, age=age)
        self.session.add(new_student)
        self.session.commit()
        result = self.get_student_by_name_and_age(name, age)
        return result if result else False

    def create_course(self, name: str):
        new_course = self.Courses(name=name)
        self.session.add(new_course)
        self.session.commit()
        return new_course.id

    def get_course_by_name(self,name: str) -> int:
        result = self.session.query(self.Courses.id).filter(self.Courses.name == name).first()
        return result[0] if result else False

    def get_student_by_name_and_age(self,name: str, age: int) -> int:
        result = (self.session
                  .query(self.Students.id)
                  .filter(self.Students.name == name, self.Students.age == age)
                  .first()
                  )
        return result[0] if result else False

    def set_student_to_course(self, student_name: str, student_age: int, course_name: str):
        # check course and student exists, and create it if not exists
        course_id = self.get_course_by_name(course_name)
        if not course_id:
            course_id = self.create_course(course_name)
        student_id = self.get_student_by_name_and_age(student_name, student_age)
        if not student_id:
            student_id = self.create_student(student_name, student_age)

        new_students_course = self.StudentsCourses(course_id=course_id, student_id=student_id)
        self.session.add(new_students_course)
        self.session.commit()

    def clear_database(self):
        self.session.query(self.StudentsCourses).delete()
        self.session.commit()
        self.session.query(self.Students).delete()
        self.session.commit()
        self.session.query(self.Courses).delete()
        self.session.commit()


    def get_empty_courses(self):
        result = (self.session
                  .query(self.Courses.name, self.StudentsCourses)
                  .outerjoin(self.StudentsCourses)
                  .all()
                  )

        # looks like kostil, but in query I can`t realise that by filter or where
        result = [res.name for res in result if res[1] is None]
        return result[0] if result else False

    def get_students_by_course(self, course_name: str):
        result = (self.session
                  .query(self.Students)
                  .join(self.StudentsCourses)
                  .join(self.Courses)
                  .filter(self.Courses.name == course_name)
                  .all()
                  )
        return result

    def update_student(self, name, age, new_name=None, new_age=None):
        upd_values = {}
        if new_name:
            upd_values['name'] = new_name
        if new_age:
            upd_values['age'] = new_age
        if upd_values:
            student_id = self.get_student_by_name_and_age(name, age)
            assert student_id, f'student with name {name} and age {age} does not exist'
            update_stmt = (update(self.Students).where(self.Students.id == student_id).values(upd_values))
            self.session.execute(update_stmt)

    def delete_student_from_course(self, name, age, course):
        course_id = self.get_course_by_name(course)
        student_id = self.get_student_by_name_and_age(name, age)
        # TODO: add asserts for id-s and check is row exists
        (self.session.query(self.StudentsCourses)
                        .filter(
                    self.StudentsCourses.student_id==student_id,
                            self.StudentsCourses.course_id==course_id)
                        .delete()
            )
        self.session.commit()
