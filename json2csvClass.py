import csv
import json

class JSONtoCSVConverter:
    def __init__(self, json_file_path, csv_file_path):
        self.json_file_path = json_file_path
        self.csv_file_path = csv_file_path

    def convert(self):
        with open(self.json_file_path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        with open(self.csv_file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            header = data[0].keys()
            csv_writer.writerow(header)
            for row in data:
                csv_writer.writerow(row.values())

if __name__ == "__main__":
    converter = JSONtoCSVConverter('sample.json', 'sample_converted.csv')
    converter.convert()
    print("JSONファイルをCSVファイルに変換しました。")
