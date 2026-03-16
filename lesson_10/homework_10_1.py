
print("Task1")
class Employee:
    def __init__(self, name, salary, **kwargs):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def __init__(self, department, **kwargs):
        super().__init__(**kwargs)
        self.department = department

class Developer(Employee):
    def __init__(self, programming_language, **kwargs):
        super().__init__(**kwargs)
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        super().__init__(
            name=name,
            salary=salary,
            department=department,
            programming_language=programming_language
        )
        self.team_size = team_size

def test_teamLead():
    teamLead = TeamLead(
        name="John",
        salary=5000,
        department="R&D",
        programming_language="Python",
        team_size=3
    )

    attributes = ["name", "salary", "department", "programming_language", "team_size"]
    for attr in attributes:
        assert hasattr(teamLead, attr), f"Error: Attribute {attr} is not available for TeamLead"

    assert teamLead.name == "John"
    assert teamLead.salary == 5000
    assert teamLead.department == "R&D"
    assert teamLead.programming_language == "Python"
    assert teamLead.team_size == 3

print("Test passed ✅")

if __name__ == "__main__":
    test_teamLead()
print("-" * 20)

print("Task2")
from abc import ABC, abstractmethod
import math

class Figure(ABC):
    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimeter(self):
        pass

class Square(Figure):
    def __init__(self, side):
        self.__side = side

    def get_area(self):
        return self.__side ** 2

    def get_perimeter(self):
        return self.__side * 4

class Circle(Figure):
    def __init__(self, radius):
        self.__radius = radius

    def get_area(self):
        return math.pi * (self.__radius ** 2)

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("A triangle with these sides does not exist")
        self.__a = side_a
        self.__b = side_b
        self.__c = side_c

    def get_perimeter(self):
        return self.__a + self.__b + self.__c

    def get_area(self):
        p = self.get_perimeter() / 2
        return math.sqrt(p * (p - self.__a) * (p - self.__b) * (p - self.__c))

figures = [
    Square(5),
    Circle(3),
    Triangle(3, 4, 5)
]

for figure in figures:
    print(f"Figure: {figure.__class__.__name__}")
    print(f"Area: {figure.get_area():.2f}")
    print(f"Perimeter: {figure.get_perimeter():.2f}")
    print("-" * 20)
