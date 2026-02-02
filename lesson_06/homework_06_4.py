my_list = [5, 10, 17, 23, 4, 8, 11, 42, 67, 33]
sum = 0
for item in my_list:
    if item % 2 == 0:
        sum += item
print(f"Sum of even numbers: {sum}")