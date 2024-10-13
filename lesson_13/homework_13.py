import csv
import json
import logging

from pathlib import Path
import xml.etree.ElementTree as ET


# task 1 - compare and save csv file
def save_uniq_data_from_csv_files(file1_name, file2_name):
    data1 = data2 = []
    with open(file1_name) as file1:
        data1 = list(csv.reader(file1))
        title = data1[0]
        data1 = data1[1:]


    with open(file2_name) as file2:
        data2 = list(csv.reader(file2))[1:]

    data1.extend(data2)
    # add key to compare
    for row in data1:
        row.append("".join(row))

    result = []
    result.insert(0, title)

    for element in data1:
        for res in result:
            if element[-1] == res[-1]:
                break
        else:
            result.append(element)

    with open("result_prykhodko.csv", "w") as result_file:
        writer = csv.writer(result_file)
        writer.writerows(result)

save_uniq_data_from_csv_files("random-michaels.csv", "random.csv")


# task 2 - validate json data in the file
def log_json_format_error(file_name: str):
    log_message = f"file {file_name} contains data in not valid json format"

    # Створення та налаштування логера
    logging.basicConfig(
        filename='json_format_errors.log',
        level=logging.ERROR,
        format='%(asctime)s - %(message)s'
        )
    logger = logging.getLogger("log_json_format_error")

    # Логування події
    logger.error(log_message)

def validate_json_format():
    directory_with_json_files = Path.cwd() / "json_files"

    extension = '.json'
    files_with_extension = [f for f in directory_with_json_files.iterdir() if f.suffix == extension]

    for file in files_with_extension:
        with open(file) as f:
            try:
                json.load(f)
            except json.JSONDecodeError:
                log_json_format_error(f.name)

validate_json_format()

# task 3 - find data in the xml tree form xml file
def get_incoming_by_group_number(target_number:int | str):
    tree = ET.parse('groups.xml')
    root = tree.getroot()

    for group in root.findall('group'):
        number = group.find('number')
        if number is not None and number.text == str(target_number):
            timing_exbytes = group.find('timingExbytes')
            if timing_exbytes is not None:
                incoming = timing_exbytes.find('incoming')
                if incoming is not None:
                    return incoming.text

    return None

for i in range(6):
    print(f" incoming for group {i} is {get_incoming_by_group_number(i)}")
