import json
from django.conf import settings
from django.http import response
from psycopg2 import connect, sql, Error


def lower_str(string):
    return string.lower()

class FileManipulation:
    def __init__(self):
        pass

    def pre_process_data(self, csv_file):
        file_data = csv_file.read().decode("utf-8")
        columns_name = []
        data = []
        output_data = {}

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

        # TODO: validate dataset name
        output_data['dataset_name'] = csv_file.name
        output_data['headers'] = columns_name
        output_data['headers_count'] = len(columns_name)
        output_data['data'] = data
        output_data = json.dumps(output_data)

        return [columns_name, data, output_data]

    def execute_sql(self, command , sql_query):
        data_conexion = settings.DATABASES['graph_db']
        response_info = {
            'is_execution_ok': False,
            'error_message': '',
            'data': '',
        }
        try:
            with connect(
                dbname=data_conexion['NAME'],
                user=data_conexion['USER'],
                password=data_conexion['PASSWORD'],
                host=data_conexion['HOST']
            ) as conn:
                try:
                    with conn.cursor() as cur:
                        sql_object = sql.SQL(sql_query)
                        cur.execute(sql_object)
                        if command == 'select':
                            response_info['data'] = cur.fetchall()
                        else:
                            conn.commit()
                        
                        response_info['is_execution_ok'] = True
                except Error as e:
                    response_info['error_message'] = 'Error executing sql'
                    print('error executing sql', e.pgerror)
                finally:
                    if cur is not None:
                        cur.close()
        except Error as e:
            print('error connecting to database', e.pgerror)
        finally:
            if conn is not None:
                conn.close()

        return response_info

    def save_data(self, csv_data):
        dataset_name = csv_data.get('dataset_name')
        headers = csv_data.get('headers')
        headers_and_types = csv_data.get('headers_and_types')
        data_content = csv_data.get('data')
        response_info = {
            'is_saved': False,
            'error_message': '',
        }

        # CREATE table
        query_create = f"CREATE TABLE IF NOT EXISTS {dataset_name}"
        query_columns = "id SERIAL PRIMARY KEY, "

        # TODO: correlationate user's ID with table and add audit columns
        for header_and_type in headers_and_types:
            header_name = header_and_type[0]
            header_type = header_and_type[1]

            if header_type == 'string':
                query_columns =+ f"{header_name} VARCHAR(128) NOT NULL, "

            elif header_type == 'integer':
                query_columns =+ f"{header_name} INTEGER NOT NULL, "

            elif header_type == 'float':
                query_columns =+ f"{header_name} FLOAT NOT NULL, "
            
            elif header_type == 'boolean':
                query_columns =+ f"{header_name} BOOLEAN NOT NULL, "
            
            elif header_type == 'date':
                query_columns =+ f"{header_name} DATE NOT NULL, "
            
            elif header_type == 'time':
                query_columns =+ f"{header_name} TIME NOT NULL, "
            
            elif header_type == 'datetime':
                query_columns =+ f"{header_name} DATETIME NOT NULL, "
            
            elif header_type == 'timestamp':
                query_columns =+ f"{header_name} TIMESTAMP NOT NULL, "
            
            else:
                query_columns =+ f"{header_name} VARCHAR(128) NOT NULL, "

        # delete last comma and space
        query_columns = query_columns[:-2]
        # format final query
        query_create = f"{query_create} ({query_columns});"

        execution_response = self.execute_sql('create', query_create)

        if not execution_response.get('is_execution_ok'):
            response_info['error_message'] = 'Error creating table'
            return response_info

        # Once the table is created, INSERT data
        query_insert = ''
        headers_statement = ''
        values_statement = ''

        for header in headers:
            if header == headers[-1]:
                headers_statement += f"{header}"
            else:
                headers_statement += f"{header}, "
        
        for data_row in data_content:
            data_row_str = str(tuple(data_row))

            if data_row == data_content[-1]:
                values_statement += f"{data_row_str}"
            else:
                values_statement += f"{data_row_str}, "

        query_insert = f"INSERT INTO {dataset_name} ({headers_statement}) VALUES {values_statement};"
        execution_response = self.execute_sql('insert', query_insert)
        
        if not execution_response.get('is_execution_ok'):
            response_info['error_message'] = 'Error inserting data'
        else:
            response_info['is_saved'] = True
        
        return response_info


    def get_data(self, dataset_name, **kwargs):
        response_info = {
        }
        user_id = kwargs.get('user_id')

        if user_id:
            query_select = f"SELECT * FROM {dataset_name} WHERE user_id = {user_id};"
        # TODO: search not only by user_id but also by other columns (?)
        else:
            # TODO: exclude deleted datasets
            query_select = f"SELECT * FROM {dataset_name};"
        
        execution_response = self.execute_sql('select', query_select)
        
        if not execution_response.get('is_execution_ok'):
            response_info['error_message'] = 'Error getting data'
        else:
            response_info['is_saved'] = True

        return response_info
