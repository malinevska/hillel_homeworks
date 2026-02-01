# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result
from pprint import pprint

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]

my_record = ('Sandra', 'Malinevska', 28, 'QA Engineer', 'Kyiv')
people_records.insert(0, my_record)
pprint(people_records[:5]) #List with index 0 (New)
print("-" * 50)

people_records[1], people_records[5] = people_records[5], people_records[1]
pprint(people_records[:5]) #Swaped list (indexes 1<->5)
print("-" * 50)

target_indexes = [6, 10, 13]
results = []
print("Check people records:")

for index in target_indexes:
    person = people_records[index]
    name = person[0]
    age = person[2]
    is_adult = age >= 30
    results.append(is_adult)
    print(f"Index {index}: {name} (Age: {age}) >= 30? -> {is_adult}")
print("-" * 50)
