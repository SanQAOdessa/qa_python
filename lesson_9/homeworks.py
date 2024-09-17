def sum_of_two_numbers(numer_one, number_two):
    return numer_one + number_two

def reverse_string(my_string):
    return my_string[-1::-1]

def sum_of_even_numbers(list_of_numbers: list):
    """
    calculate sum of even numbers and print result if needed
    :param list_of_numbers: list of numbers like [1, 2, 3]
    :return: sum of even numbers
    """
    return sum([number for number in list_of_numbers if number % 2 == 0])

def calculate_needs_fuel_and_stops_for_traveling(distance, consumption, tank_capacity):
    """
    calculates needs fuel and stops for traveling by distance, consumption and tank capacity, prints result if needed
    :param distance: int
    :param consumption: int
    :param tank_capacity: int
    :return: tuple of fuel and stops results
    """
    needs_fuel = round(distance / consumption, 2)
    count_of_stops_in_gas_stations = int((needs_fuel // tank_capacity) + 1)

    return needs_fuel, count_of_stops_in_gas_stations

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

def select_all_strings_in_list(input_list: list):
    return [item for item in input_list if isinstance(item, str)]