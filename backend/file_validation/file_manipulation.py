

def lower_str(string):
    return string.lower()

class FileManipulation:
    def __init__(self):
        pass

    def pre_process_data(self, csv_file):
        file_data = csv_file.read().decode("utf-8")
        columns_name = []
        data = []

        # TODO: Check if file has another line separator than \n
        lines = file_data.split('\n')

        columns_name = lines[0].split(',')
        columns_name_lower = map(lower_str, columns_name)
        columns_name = list(columns_name_lower)

        # remove header
        lines.pop(0)

        for line in lines:
            if line:
                fields = line.split(',')
                # TODO: Validate if there are empty fields because 
                # it will cause error in datatable.net script
                data.append(fields)
        #sys.exit(f'file {filename}, line {reader.line_num}: {e}')

        return [columns_name, data]
