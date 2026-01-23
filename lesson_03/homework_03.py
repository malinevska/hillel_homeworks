alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк

alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don\'t much care where ——" said Alice.\n"Then it doesn\'t matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)


"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""

Black_sea_area = 436402
Azov_sea_area = 37800
total_area = Black_sea_area + Azov_sea_area
print(f"Чорне та Азовське моря разом займають: {total_area} км2 ")


# task 05
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""

total_goods = 375291
warehouse_1_2 = 250449
warehouse_2_3 = 222950

warehouse_1 = total_goods - warehouse_2_3
warehouse_2 = warehouse_1_2 - warehouse_1
warehouse_3 = total_goods - warehouse_1_2
print(f"Склад 1: {warehouse_1} товарів, склад 2: {warehouse_2} товарів, склад 3: {warehouse_3} товарів")

# task 06
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""

payment_per_month = 1179
duration_years = 1.5
total_months = duration_years * 12
computer_price = total_months * payment_per_month
print(f"Вартість комп'ютера: {computer_price} грн")

# task 07
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""

result_a = 8019 % 8
print(f"a) Остача 8019 : 8 = {result_a}")

result_b = 9907 % 9
print(f"b) Остача 9907 : 9 = {result_b}")

result_c = 2789 % 5
print(f"c) Остача 2789 : 5 = {result_c}")

result_d = 7248 % 6
print(f"d) Остача 7248 : 6 = {result_d}")

result_e = 7128 % 5
print(f"e) Остача 7128 : 5 = {result_e}")

result_f = 19224 % 9
print(f"f) Остача 19224 : 9 = {result_f}")    

# task 08
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""

large_pizza = 4
medium_pizza = 2
juice = 4
cake = 1
water = 3

large_pizza_price = 274
medium_pizza_price = 218
juice_price = 35
cake_price = 350
water_price = 21

large_pizza_cost = large_pizza * large_pizza_price
medium_pizza_cost = medium_pizza * medium_pizza_price
juice_cost = juice * juice_price
cake_cost = cake * cake_price
water_сost = water * water_price

total_amount = large_pizza_cost + medium_pizza_cost + juice_cost + cake_cost + water_сost
print(f"Іринці потрібно всього {total_amount} грн, щоб зробити замовлення")
 

# task 09
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""

total_photos = 232
photos_per_page = 8
pages_needed = total_photos // photos_per_page
print(f"Ігорю знадобиться {pages_needed} сторінок, щоб вклеїти всі фото")


# task 10
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""

distance = 1600
liters_per_100km = 9   
tank_capacity = 48

total_fuel_needed = (distance / 100) * liters_per_100km
stops_needed = (total_fuel_needed // tank_capacity) - 1
print(f"Для подорожі з Харкова до Будапешту знадобиться {int(total_fuel_needed)} літрів бензину. Щонайменше {int(stops_needed)} разів родині необхідно заїхати на заправку під час подорожі")

