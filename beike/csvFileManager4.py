import csv
import os


class CsvFileManager4:
    def read(self, filename):
        base_path = os.path.dirname(__file__)
        path = base_path.replace('beike','data/'+filename)
        list = []
        with open(path, 'r') as file:
            data_table = csv.reader(file)
            for row in data_table:
                list.append(row)
        return list


if __name__ == '__main__':
    test_data = CsvFileManager4().read('test_data.csv')
    print(test_data[0])