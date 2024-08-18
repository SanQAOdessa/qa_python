# task 01 == Виправте синтаксичні помилки
print("Hello", end=" ")
print("world!")

# task 02 == Виправте синтаксичні помилки
hello = "Hello"
world = "world"
if True:
    print(f"{hello} {world}!")

# task 03  == Вставте пропущену змінну у ф-цію print
for letter in "Hello world!":
    print(letter)

# task 04 == Зробіть так, щоб кількість бананів була
# завжди в чотири рази більша, ніж яблук
apples = 2
banana = apples * 4

# task 05 == виправте назви змінних
storona_1 = 1
storona_2 = 2
storona_3 = 3
storona_4 = 4

# task 06 == Порахуйте периметр фігури з task 05
# та виведіть його для користувача
perimeter = storona_1 + storona_2 + storona_3 + storona_4
print(f"perimeter of figure is: {perimeter}")


"""
    # Задачі 07 -10:
    # Переведіть задачі з книги "Математика, 2 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в другому класі
"""
# task 07
"""
У саду посадили 4 яблуні. Груш на 5 більше яблунь, а слив - на 2 менше.
Скільки всього дерев посадили в саду?
"""
apples_tree_count = 4
pear_tree_count = apples_tree_count + 5
plum_tree_count = apples_tree_count - 2
all_tree_counts = apples_tree_count + pear_tree_count + plum_tree_count
print(f"У саду посадили {apples_tree_count} яблуні")
print(f"Груш на 5 більше яблунь, тобто {apples_tree_count} + 5 = що дорівнює {pear_tree_count}")
print(f"Слив на 2 менше, тобто {apples_tree_count} - 2 = що дорівнює {plum_tree_count}")
print(f"разом кількість дерев {apples_tree_count}+{pear_tree_count}+{plum_tree_count}={all_tree_counts}")
# task 08
"""
До обіду температура повітря була на 5 градусів вище нуля.
Після обіду температура опустилася на 10 градусів.
Надвечір потепліло на 4 градуси. Яка температура надвечір?
"""
temperature_am = 5
temperature_pm = temperature_am - 10
temperature_evening = temperature_pm + 4
print(f"Evening temperature is: {temperature_evening}")
# task 09
"""
Взагалі у театральному гуртку - 24 хлопчики, а дівчаток - вдвічі менше.
1 хлопчик захворів та 2 дівчинки не прийшли сьогодні.
Скільки сьогодні дітей у театральному гуртку?
"""
boys_count = 24
girls_count = int(boys_count / 2)
absent_boys_count = 1
absent_girls_count = 2
children_in_theatre = boys_count + girls_count - absent_boys_count - absent_girls_count
print(f"There are {children_in_theatre} children in theatre today")

# task 10
"""
Перша книжка коштує 8 грн., друга - на 2 грн. дорожче,
а третя - як половина вартості першої та другої разом.
Скільки будуть коштувати усі книги, якщо купити по одному примірнику?
"""
first_book_cost = 8
second_book_cost = first_book_cost + 2
third_book_cost = (first_book_cost + second_book_cost) / 2
exemplar_count = 1
total_sum = (first_book_cost + second_book_cost + third_book_cost) * exemplar_count
print(f"Total sum for three books in {exemplar_count} exemplar equals {total_sum} hryvnas")
