import csv
import os
import json
import logging
import xml.etree.ElementTree as ET

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    encoding='utf-8',
    handlers=[
        logging.FileHandler("json__Malinevska.log", mode='a', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("QA_Logger")

""" Завдання 1: Робота з CSV """
file1 = r"automation_qa/ideas_for_test/work_with_csv/random.csv"
file2 = r"automation_qa/ideas_for_test/work_with_csv/random-michaels.csv"
output_file = "result_Malinevska.csv"

def merge_csv_files(f1, f2, out):
    unique_rows = set()
    for path in [f1, f2]:
        if os.path.exists(path):
            with open(path, mode='r', encoding='utf-8') as f:
                reader = csv.reader(f)
                for row in reader:
                    unique_rows.add(tuple(row))
        else:
            print(f"Error: File not found {path}")

    with open(out, mode='w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        for row in unique_rows:
            writer.writerow(row)
    print(f"CSV task complete. Saved as: {out}")


""" Завдання 2: Валідація JSON """
folder_to_check = r"automation_qa/ideas_for_test/work_with_json"

def validate_json_files(path):
    if not os.path.exists(path):
        print(f"Error: Folder {path} not found!")
        return

    for filename in os.listdir(path):
        if filename.endswith(".json"):
            file_path = os.path.join(path, filename)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    json.load(f)
                print(f"File {filename}: Valid")
            except (json.JSONDecodeError, ValueError) as e:
                logger.error(f"File {filename} is not valid JSON. Error: {e}")
                print(f"File {filename}: INVALID (logged)")


""" Завдання 3: Пошук в XML """
xml_path = r"automation_qa/ideas_for_test/work_with_xml/groups.xml"

def find_timing_by_group(file_path, group_number):
    if not os.path.exists(file_path):
        logger.error(f"XML file not found: {file_path}")
        return

    try:
        tree = ET.parse(file_path)
        root = tree.getroot()

        for group in root.findall('group'):
            number_tag = group.find('number')
            if number_tag is not None and number_tag.text == str(group_number):
                timing = group.find('timingExbytes')
                if timing is not None:
                    incoming = timing.find('incoming')
                    if incoming is not None:
                        value = incoming.text
                        logger.info(f"Group {group_number} -> timingExbytes/incoming: {value}")
                        return value

        logger.info(f"Group {group_number} not found in XML.")
    except ET.ParseError as e:
        logger.error(f"XML Parse Error in {file_path}: {e}")


if __name__ == "__main__":
    merge_csv_files(file1, file2, output_file)
    validate_json_files(folder_to_check)
    find_timing_by_group(xml_path, "10")