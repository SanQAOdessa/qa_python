# alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та відобразіть всі символи одинарної лапки (') у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
from more_itertools.more import divide

# task 01
alice_in_wonderland = """
"Would you tell me, please, which way I ought to go from here?
That depends a good deal on where you want to get to," said the Cat.
"I don't much care where ——" said Alice.
"Then it doesn't matter which way you go," said the Cat.
"—— so long as I get somewhere," Alice added as an explanation.
"Oh, you're sure to do that," said the Cat, "if you only walk long enough."
"""

# task 02
max_index = len(alice_in_wonderland)
for index, letter in enumerate(alice_in_wonderland):
    if letter == "'":
        start_slice = index - 1 if index > 0 else 0
        end_slice = index + 2 if index < max_index else max_index
        print(f"letter ' in position {index} in substring {alice_in_wonderland[start_slice:end_slice]}")

# task 03
print(alice_in_wonderland)

"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""
# task 04
print("\n=========== task 04 =============")

"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
square_of_black_sea = 436402
square_of_azov_sea = 37800
common_square_of_seas = square_of_black_sea + square_of_azov_sea
answer = f"""
Common square of Black and Azov seas is {common_square_of_seas} km2
it is a sum of Black sea square ({square_of_black_sea} km2) 
and Azov sea square ({square_of_azov_sea} km2)
{square_of_black_sea} + {square_of_azov_sea} = {common_square_of_seas}
"""
print(answer)
# task 05
print("\n=========== task 05 =============")
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
total_product_count = 375291
first_and_second_floors_product_count = 250449
second_and_third_floors_product_count = 222950
second_floor_product_count = first_and_second_floors_product_count + second_and_third_floors_product_count - total_product_count
first_floor_product_count = first_and_second_floors_product_count - second_floor_product_count
third_floor_product_count = second_and_third_floors_product_count - second_floor_product_count
print(f"In the first floor {first_floor_product_count} products")
print(f"In the second floor {second_floor_product_count} products")
print(f"In the third floor {third_floor_product_count} products")
# task 06
print("\n=========== task 06 =============")

"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
month_count = 18
month_payment = 1179
total_sum = month_count * month_payment
print(f"Computer costs {total_sum} grn ({month_payment} grn/month * {month_count} months)")

# task 07
print("\n=========== task 07 =============")
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
data = {8019: 8, 9907: 9, 2789: 5, 7248 : 6, 7128: 5, 19224: 9}
for dividend, divider in data.items():
    print(f"{dividend} % {divider} = {dividend % divider}")

# task 08
print("\n=========== task 08 =============")

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
basket = {
    "big pizza": {"quantity": 4, "cost": 274},
    "medium pizza": {"quantity": 2, "cost": 218},
    "juice": {"quantity": 4, "cost": 35},
    "cake": {"quantity": 1, "cost": 350},
    "water": {"quantity": 3, "cost": 21}
}
bill = []
for item in basket.values():
    bill.append(item['quantity'] * item['cost'])
print(f"Irina's order will cost {sum(bill)} grn")

# task 09
print("\n=========== task 09 =============")

"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
count_photos = 232
photos_in_page = 8
photos_in_last_page = count_photos % photos_in_page
pages_count = count_photos // photos_in_page
if photos_in_last_page != 0:
    pages_count += 1
print(f"for {count_photos} photos Ihor needs {pages_count} pages")

# task 10
print("\n=========== task 10 =============")

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
consumption = 9
tank_capacity = 48

needs_fuel = round(1600 / 9, 2)
count_of_stops_in_gas_stations = int((needs_fuel // tank_capacity) + 1)

print(f"For trip by distance {distance} km with consumption {consumption} l per 100 km")
print(f"family needs {needs_fuel} liters of fuel and they will make {count_of_stops_in_gas_stations} stops in gas stations")
