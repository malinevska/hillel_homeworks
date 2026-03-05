class Student:
    def __init__(self, first_name, second_name, age, average_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.average_score = average_score
    def update_score(self, new_score):
        self.average_score = new_score
    def display_info(self):
        print(f"Student: {self.first_name} {self.second_name}, age: {self.age}, average score: {self.average_score}")

student1 = Student("John", "Smith", 45, 90)
student1.update_score(92.0)
student1.display_info()

