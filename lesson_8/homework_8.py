
my_data = ["1,2,3,4", "1,2,3,4,50", "qwerty1,2,3"]

def sum_of_numbers_in_string(my_string: str):
    """
    returns sum of numbers if only numbers in string, esle - returns text - I can`t do this
    :param my_string: string with numbers, separated by comma
    :return: sum of numbers or text I can`t do this
    """
    try:
        result = sum([int(item) for item in my_string.split(',')])
    except ValueError:
        result = "I can`t do this"
    except Exception as e:
        result = f"Unexpected error: {e}"

    return result

for item in my_data:
    print(sum_of_numbers_in_string(item))