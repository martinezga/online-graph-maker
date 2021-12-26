import pandas as pd


def lower_str(string):
    return string.lower()

class FileManipulation:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def pre_process_data(self):
        file_data = pd.read_csv(self.csv_file)
        columns_name_list = []
        data_type = ['integer', 'integer', 'integer', 'integer', 'integer','integer', 'integer', 'integer', 'integer', 'integer']
        data = [10, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        columns_name_lower = map(lower_str, file_data.columns)
        columns_name_list = list(columns_name_lower)

        return [columns_name_list, data_type, data]
