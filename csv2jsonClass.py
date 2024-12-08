import csv
import json

class CSVtoJSONConverter:
    def __init__(self, csv_file_path, json_file_path):
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path

    def convert(self):
        data = []
        with open(self.csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open(self.json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

if __name__ == "__main__":
    converter = CSVtoJSONConverter('sample.csv', 'sample_converted.json')
    converter.convert()
    print("CSVファイルをJSONファイルに変換しました。")
