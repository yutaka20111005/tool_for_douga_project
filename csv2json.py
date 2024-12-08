import csv
import json

def csv_to_json(csv_file_path, json_file_path):
    data = []
    with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)
    
    with open(json_file_path, mode='w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    csv_file_path = 'sample.csv'
    json_file_path = 'sample_converted.json'
    csv_to_json(csv_file_path, json_file_path)
    print(f"CSVファイル '{csv_file_path}' をJSONファイル '{json_file_path}' に変換しました。")
