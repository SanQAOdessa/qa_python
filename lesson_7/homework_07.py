# task 1
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
print("-"*20, "task 1")

def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result >= 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

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
print("-"*20, "task 2")

def sum_of_two_numbers(numer_one, number_two):
    return numer_one + number_two

print(f"Sum of 5 and 6 is: {sum_of_two_numbers(5, 6)}")

# task 3
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
print("-"*20, "task 3")

def arithmetic_mean(numbers):
    if len(numbers) != 0:
        return sum(numbers) / len(numbers)
    else:
        return 0

numbers = [1, 3 ,5]
print(f"arithmetic mean of {numbers} is {arithmetic_mean(numbers)}")

# task 4
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
print("-"*20, "task 4")

def reverse_string(my_string):
    return my_string[-1::-1]

some_string = "qwerty"
print(f"string '{some_string} reverted to: '{reverse_string(some_string)}")

# task 5
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
print("-"*20, "task 5")

def max_long_word_in_list(my_list: list):
    return sorted(my_list, key=lambda a: len(a))[-1]

list_of_words = ["a", "aa", "dddd", "sss"]
print(list_of_words)
print(f"max long word in {list_of_words} is: {max_long_word_in_list(list_of_words)}")

# task 6
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
print("-"*20, "task 6")

def find_substring(str1, str2):
    return str1.find(str2)

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1

# task 7
print("-"*20, "task 7")

def get_text_from_input_with_mandatory_symbol(symbol: str, attempts: int = 1):
    """
    function returns user inputs if symbols in lower or uppercase is present in user input
    otherwise returns False
    :param attempts: max quantity attempts for user input
    :param symbol: string that will be present in user input
    :return: string or False
    """
    user_input = ''
    user_attempt = 0
    while symbol.lower() not in user_input.lower():
        if user_attempt >= attempts:
            return False
        user_attempt += 1
        user_input = input(f"attempt {user_attempt} - enter text with '{symbol}': ")

    return user_input

print(get_text_from_input_with_mandatory_symbol('a', 2))
# task 8
print("-"*20, "task 8")
def sum_of_even_numbers(list_of_numbers: list, print_result: bool = False):
    """
    calculate sum of even numbers and print result if needed
    :param list_of_numbers: list of numbers like [1, 2, 3]
    :param print_result: True or False
    :return: sum of even numbers
    """
    result = sum([number for number in list_of_numbers if number % 2 == 0])
    if print_result:
        print(f"sum of even numbers from {list_of_numbers} is: {result}")

    return result

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sum_of_even_numbers_in_my_list = sum_of_even_numbers(my_list, print_result=True)

# task 9
print("-"*20, "task 9")

def calculate_needs_fuel_and_stops_for_traveling(distance, consumption, tank_capacity, print_result = False):
    """
    calculates needs fuel and stops for traveling by distance, consumption and tank capacity, prints result if needed
    :param distance: int
    :param consumption: int
    :param tank_capacity: int
    :param print_result: bool
    :return: tuple of fuel and stops results
    """
    needs_fuel = round(distance / consumption, 2)
    count_of_stops_in_gas_stations = int((needs_fuel // tank_capacity) + 1)
    if print_result:
        print(f"For trip by distance {distance} km with consumption {consumption} l per 100 km")
        print(f"you need {needs_fuel} liters of fuel and they will make {count_of_stops_in_gas_stations} "
              f"stops in gas stations")
    return needs_fuel, count_of_stops_in_gas_stations

print(calculate_needs_fuel_and_stops_for_traveling(1600, 9, 48, print_result=True))
# task 10
print("-"*20, "task 10")

def count_of_pages_for_photos(count_photos, photos_in_page):
    """
    calculate count of pages in album for photos
    :param count_photos: int - count of photos
    :param photos_in_page: int - count of photos in the page
    :return: int count of needs pages
    """
    photos_in_last_page = count_photos % photos_in_page
    pages_count = count_photos // photos_in_page
    if photos_in_last_page != 0:
        pages_count += 1
    return pages_count

print(count_of_pages_for_photos(100, 5))
"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""