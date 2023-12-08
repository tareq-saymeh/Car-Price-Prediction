import os
import json
import re 
from bs4 import BeautifulSoup

def extract_data(file_content):
    soup = BeautifulSoup(file_content, 'html.parser')

    driving_table = soup.find('table', class_='driving-table')
    if driving_table is None:
        # Handle the case where the table is not found (e.g., print a message, skip the file, etc.)
        print(f"Table not found in the file content.")
        return None

    car_name_element = driving_table.find('h3')
    car_model_element = driving_table.find('h5')
    car_price_element = driving_table.find('h5', class_='post-price')

    car_name = car_name_element.text.strip() if car_name_element else None
    car_model = car_model_element.text.strip() if car_model_element else None
    car_price_text = car_price_element.text.strip() if car_price_element else None
    car_price_match = re.search(r'(\d+)', car_price_text)
    car_price = car_price_match.group(1) if car_price_match else None
    # Extract features and their values
    list_ads_table = soup.find('table', class_='list_ads')
    features = {}

    # Check if the 'list_ads_table' is found
    if list_ads_table:
        for row in list_ads_table.find_all('tr', class_='list-row'):
            columns = row.find_all('td')
            key_element = columns[0].text.strip()
            value_element = columns[1].text.strip()

            # Check if key and value elements are found
            if key_element and value_element:
                # If the key already exists, check if it's a list
                if key_element in features:
                    # If it's not a list, convert it to a list
                    if not isinstance(features[key_element], list):
                        features[key_element] = [features[key_element]]
                    features[key_element].append(value_element)
                else:
                    features[key_element] = value_element

    data = {
        'car_name': car_name,
        'car_model': car_model,
        'car_price': car_price,
        **features  # include features directly in the main dictionary
    }

    return data

all_data = []

# The directory of the data
files_directory = 'C:/Users/Tareq/Desktop/ml/data'

# List of keys you want to ensure are present in the output JSON
required_keys = ["لون السيارة", "نوع الوقود", "أصل السيارة", "رخصة السيارة", "نوع الجير", "الزجاج", "قوة الماتور", "عداد السيارة", "عدد الركاب", "وسيلة الدفع", "معروضة", "أصحاب سابقون"]

for file_name in os.listdir(files_directory):
    if file_name.endswith('.txt'):
        file_path = os.path.join(files_directory, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()

            # Print the file content for debugging

            data = extract_data(file_content)



            if data:
                all_data.append(data)
            else:
                print(f"Skipping file: {file_path}")

# Set default values for required keys if not found
for data in all_data:
    for key in required_keys:
        if key not in data:
            data[key] = None

# Fill missing data with 'None'
for data in all_data:
    for key in data:
        if data[key] is None:
            data[key] = None

# JSON file that will save data
output_json_file = 'output.json'

with open(output_json_file, 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=2)