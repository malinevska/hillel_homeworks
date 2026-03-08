def calcucalte_string_sum(data_string):
    total = 0
    numbers = data_string.split(',')
    for number in numbers:
        total += float(number)
    return total

data_list = [
    "1,2,3,4",
    "1,2,3,4,50",
    "qwerty1,2,3"
]

for element in data_list:
    try:
        result = calcucalte_string_sum(element)
        print(result)
    except ValueError:
        print("Не можу це зробити!")