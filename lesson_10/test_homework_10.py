import unittest
import string
import random

from lesson_10.homework_10 import *


class TestHomework10(unittest.TestCase):

    def test_correct_login(self):
        user_name = ''.join(random.choices(string.ascii_letters, k=7))
        expected_result = f"Username: {user_name}, Status: success"

        log_event(user_name, 'success')
        actual_data_in_file = get_last_message_from_login_file()

        self.assertEqual(expected_result, actual_data_in_file)

    def test_expired_login(self):
        user_name = ''.join(random.choices(string.ascii_letters, k=7))
        expected_result = f"Username: {user_name}, Status: expired"

        log_event(user_name, 'expired')
        actual_data_in_file = get_last_message_from_login_file()

        self.assertEqual(expected_result, actual_data_in_file)

    def test_error_login(self):
        user_name = ''.join(random.choices(string.ascii_letters, k=7))
        expected_result = f"Username: {user_name}, Status: no status"

        log_event(user_name, 'no status')
        actual_data_in_file = get_last_message_from_login_file()

        self.assertEqual(expected_result, actual_data_in_file)

    def test_empty_name_login(self):
        user_name = ''
        expected_result = f"Username: {user_name}, Status: no status"

        log_event(user_name, 'no status')
        actual_data_in_file = get_last_message_from_login_file()

        self.assertEqual(expected_result, actual_data_in_file)

    def test_empty_status_login(self):
        user_name = ''.join(random.choices(string.ascii_letters, k=7))
        expected_result = f"Username: {user_name}, Status:"

        log_event(user_name, '')
        actual_data_in_file = get_last_message_from_login_file()

        self.assertEqual(expected_result, actual_data_in_file)