import pytest

from math import pi
from abc import ABC, abstractmethod

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = department


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, salary)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(Shape):
    "square"
    def __init__(self, side_length):
        self.__side_length = side_length

    def area(self):
        return self.__side_length ** 2

    def perimeter(self):
        return self.__side_length * 4

class Circle(Shape):
    "circle"
    def __init__(self, radius):
        self.__radius = radius

    def area(self):
        return round(pi * self.__radius ** 2, 2)

    def perimeter(self):
        return round(pi * self.__radius * 2, 2)

class Rectangle(Shape):
    "rectangle"
    def __init__(self, side_a_length, side_b_length):
        self.__side_a_length = side_a_length
        self.__side_b_length = side_b_length

    def area(self):
        return self.__side_a_length * self.__side_b_length

    def perimeter(self):
        return (self.__side_a_length + self.__side_b_length) * 2

@pytest.fixture()
def team_lead():
    return TeamLead("Job", 100, "r&d", "php")

def get_public_attributes_from_class(my_class):
    return {item for item in dir(my_class) if not item.startswith("_")}

def test_teamlead_contains_manager_attributes(team_lead):
    manager = Manager("test", 10, "dep")
    manager_attributes = get_public_attributes_from_class(manager)
    team_lead_attributes = get_public_attributes_from_class(team_lead)
    assert manager_attributes.issubset(team_lead_attributes)

def test_teamlead_contains_developer_attributes(team_lead):
    developer = Developer("test", 10, "php")
    developer_attributes = get_public_attributes_from_class(developer)
    team_lead_attributes = get_public_attributes_from_class(team_lead)
    assert developer_attributes.issubset(team_lead_attributes)

def test_methods_in_inherent_classes():
    square = Square(10)
    circle = Circle(20)
    rectangle = Rectangle(5, 50)
    my_figures = [square, circle, rectangle]
    for figure in my_figures:
        print(f"\n{figure.__doc__} - area {figure.area()}, perimeter - {figure.perimeter()}")