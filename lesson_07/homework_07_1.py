# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(f"{number} x {multiplier} = {result}")

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15


# task 2
"""  Написати функцію, яка обчислює суму двох чисел.
"""

def sum_numbers(a, b):
    return a + b

print(sum_numbers(5, 5))


# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""

def calculate_average(numbers):
    total_sum = 0

    for num in numbers:
        total_sum += num

    count = len(numbers)
    if count == 0:
        return 0

    return total_sum/count

my_list = [10, 20, 30, 40, 50]
print(calculate_average(my_list))

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""

def reverse_string(text):
    return text[::-1]
print(reverse_string("Python"))
        

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""

def find_longest_word(word_list):
    longest_word = ""

    for word in word_list:
        if len(word)>len(longest_word):
            longest_word = word
    return longest_word
my_list = ["apple", "banana", "pear", "watermelon", "kiwi"]
print(find_longest_word(my_list))

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):

    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1


"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""


# task 7
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" (враховуються як великі так і маленькі).
Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
"""
def has_h_letter(word):
    return "h" in word.lower()
my_word = "python"
result = has_h_letter(my_word)
print(result)

# task 8
""" Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими.
"""
def filter_strings_only(original_list):
    strings_only_list = []
    for item in original_list:
        if isinstance(item, str):
            strings_only_list.append(item)
    return strings_only_list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = filter_strings_only(lst1)
print(lst2)

# task 9
"""Порахувати кількість унікальних символів в строці.
Якщо їх більше 10 - вивести в консоль True, інакше - False.
"""
def has_unique_chars(text):
    unique_chars = set(text)
    count = len(unique_chars)
    return count > 10
print(has_unique_chars("abcdefghijk"))
print(has_unique_chars("abc"))

# task 10
""" Перевірте чи починається якесь речення з "By the time".
"""
def check_sentence_start(text, prefix):
    return text.startswith(prefix)
sentence = "By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for a kite, in good repair"
result = check_sentence_start(sentence, "By the time")
print(result)
