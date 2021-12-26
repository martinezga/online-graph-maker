import pandas as pd


def lower_str(string):
    return string.lower()


def pre_process_data(csv_file):
    file_data = pd.read_csv(csv_file)
    columns_name_list = []
    data_type = ['integer', 'integer', 'integer', 'integer', 'integer','integer', 'integer', 'integer', 'integer', 'integer']
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    columns_name_lower = map(lower_str, file_data.columns)
    columns_name_list = list(columns_name_lower)

    return [columns_name_list, data_type, data]
