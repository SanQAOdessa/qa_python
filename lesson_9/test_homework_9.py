import unittest

from lesson_9.homeworks import *


class TestHomework9(unittest.TestCase):

    def test_add_positive(self):
        self.assertEqual(11, sum_of_two_numbers(5, 6))

    def test_add_negative(self):
        self.assertEqual(-5, sum_of_two_numbers(-2, -3))

    def test_add_type_error(self):
        try:
            sum_of_two_numbers("4", 5)
        except TypeError:
            print("TypeError raised")
        else:
            self.fail("TypeError is not raised")

    def test_revert_string(self):
        test_string = "qwerty"
        expected_result = "ytrewq"
        actual_result = reverse_string(test_string)
        self.assertEqual(expected_result, actual_result)

    def test_revert_string_type_error(self):
        try:
            reverse_string(123)
        except TypeError:
            print("TypeError raised")
        else:
            self.fail("TypeError is not raised")

    def test_sum_of_even_numbers_with_even_numbers(self):
        test_data = [1, 2, 3, 4, 5, 6]
        expected_result = 12
        actual_result = sum_of_even_numbers(test_data)
        self.assertEqual(expected_result, actual_result)

    def test_sum_of_even_numbers_with_out_even_numbers(self):
        test_data = [1, 3, 5]
        expected_result = 0
        actual_result = sum_of_even_numbers(test_data)
        self.assertEqual(expected_result, actual_result)

    def test_calculate_fuel_and_stop_with_correct_data(self):
        # test data
        distance, consumption, tank_capacity = 1000, 10, 100
        fuel, stops = calculate_needs_fuel_and_stops_for_traveling(distance, consumption, tank_capacity)
        expected_fuel = 100
        expected_stops = 2
        self.assertEqual(expected_fuel, fuel)
        self.assertEqual(expected_stops, stops)

    def test_calculate_fuel_and_stop_with_zero_division(self):
        # test data
        distance, consumption, tank_capacity = 1000, 0, 100
        try:
            calculate_needs_fuel_and_stops_for_traveling(distance, consumption, tank_capacity)
        except ZeroDivisionError:
            print("ZeroDivisionError raised")
        else:
            self.fail("ZeroDivisionError is not raised")


    def test_count_of_photos_with_one_full_page(self):
        # test data
        count_of_photos = 10
        photos_in_one_page = 10
        expected_result = 1
        actual_result = count_of_pages_for_photos(count_of_photos, photos_in_one_page)
        self.assertEqual(expected_result, actual_result)

    def test_count_of_photos_with_none_full_page(self):
        # test data
        count_of_photos = 15
        photos_in_one_page = 10
        expected_result = 2
        actual_result = count_of_pages_for_photos(count_of_photos, photos_in_one_page)
        self.assertEqual(expected_result, actual_result)

    def test_select_strings_in_list(self):
        test_list = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
        expected_result = ['1', '2', 'False', '6', 'Python', 'Lorem Ipsum']
        actual_result = select_all_strings_in_list(test_list)
        self.assertListEqual(expected_result, actual_result)

if __name__ == '__main__':
    unittest.main(verbosity=2)