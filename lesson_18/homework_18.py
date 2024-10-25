import pytest
import logging


def even_numbers_generator(max_value: int):
    if max_value < 0:
        raise ValueError("max_value must be greater or equal 0")
    value = 0
    while value <= max_value:
        if value%2 == 0:
            yield value
        value += 1

def test_even_numbers_generator():
    expected_result = [0, 2, 4, 6]
    actual_result = []
    gen_numbers = even_numbers_generator(7)
    for num in gen_numbers:
        actual_result.append(num)
    assert actual_result == expected_result, "somthing wrong!!"


def fibonacci_generator(max_value):
    a, b = 0, 1
    while a <= max_value:
        yield a
        a, b = b, a + b

def test_fibonacci_generator():
    expected_result = [0, 1, 1, 2, 3, 5, 8]
    actual_result = []
    fib_generator = fibonacci_generator(10)
    for num in fib_generator:
        actual_result.append(num)
    assert actual_result == expected_result, "somthing wrong!!"

class ReversListIterator:
    def __init__(self, my_list):
        self.my_list = my_list
        self.current_element_index = len(my_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_element_index > 0:
            self.current_element_index -= 1
            return self.my_list[self.current_element_index]
        else:
            raise StopIteration

def test_revers_list_iterator():
    expected_result = [4, 3, 2, 1]
    actual_result = []

    revers_iterator = ReversListIterator([1, 2, 3, 4])
    for elem in revers_iterator:
        actual_result.append(elem)
    assert actual_result == expected_result, "somthing wrong!!"

class EvenNumbersIterator:
    def __init__(self, max_value):
        self.max_value = max_value
        self.current_value = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_value < self.max_value:
            self.current_value += 1
            if self.current_value % 2 == 0:
                return self.current_value
            else:
                self.current_value += 1
                if self.current_value > self.max_value:
                    raise StopIteration
                return self.current_value
        else:
            raise StopIteration

def test_even_numbers_iterator():
    expected_result = [0, 2, 4, 6]
    actual_result = []
    numbers_iterator = EvenNumbersIterator(7)
    for num in numbers_iterator:
        actual_result.append(num)
    assert actual_result == expected_result, "somthing wrong!!"

def my_function_with_args_and_result(arg1, arg2):
    return f"it is result {arg1} - {arg2}"

def logg_call_functions(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        logger = logging.getLogger("func params")
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
        logger.addHandler(logging.StreamHandler())
        logging.info(f"Function {func.__name__} executed with params {args} result: {result}")

        return result
    return wrapper

def test_decorated_function():
    decorated_function = logg_call_functions(my_function_with_args_and_result)
    decorated_function(5, 90)

def divide_numbers(num1, num2):
    return num1/num2

def my_exception_catching(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Exception found {e}")
            return None
    return wrapper

def test_exception_catching():
    find_exception = my_exception_catching(divide_numbers)
    find_exception(1, 0)
