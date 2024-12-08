import csv
import json

def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, mode='r', encoding='utf-8') as json_file:
        data = json.load(json_file)
    
    with open(csv_file_path, mode='w', encoding='utf-8', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        header = data[0].keys()
        csv_writer.writerow(header)
        for row in data:
            csv_writer.writerow(row.values())

if __name__ == "__main__":
    json_file_path = 'sample.json'
    csv_file_path = 'sample_converted.csv'
    json_to_csv(json_file_path, csv_file_path)
    print(f"JSONファイル '{json_file_path}' をCSVファイル '{csv_file_path}' に変換しました。")
