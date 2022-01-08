from django.views import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages
import json


class FileValidationMainView(View):
    def __init__(self):
        self.template_name = 'file_validation/preview-data.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
    
    def post(self, request, *args, **kwargs):
        csv_file = request.FILES["csv_file"]
        URL_file_validation_main = 'file_validation:main'

        if not csv_file.name.endswith('.csv'):
            messages.error(request, 'File is not CSV type')
            return redirect(URL_file_validation_main)

        if csv_file.multiple_chunks():
            messages.error(request, f'Uploaded file is too big ({csv_file.size/(1000*1000)}.2f MB)')
            return redirect(URL_file_validation_main)
        
        # TODO: error catching when file name is too long

        from file_validation.file_manipulation import FileManipulation
        # TODO: Think about error handling

        pre_processed_data = FileManipulation().pre_process_data(csv_file)

        messages.success(request, f'File {csv_file.name} uploaded successfully')
        context = {
            'is_csv_display': True,
            'headers': pre_processed_data[0],
            'data': pre_processed_data[1],
            'output_data': pre_processed_data[2],
        }
        return render(
            request,
            self.template_name,
            context
        )

class FileValidationDataTypeView(View):
    def __init__(self):
        self.template_name = 'file_validation/save-data.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
    
    def post(self, request, *args, **kwargs):
        csv_data = request.POST['csv_data']
        csv_data = json.loads(csv_data)
        data_headers = csv_data.get('headers')
        data_types_options = [
            'string',
            'integer',
            'float',
            'boolean',
            'date',
            'datetime',
            'time',
            'timestamp',
        ]

        max_id = csv_data.get('headers_count')
        headers_id = [f'header{number}' for number in range(max_id)]
        data_tuple_headers = list(zip(headers_id, data_headers))

        context = {
            'csv_data': csv_data,
            'data_tuple_headers': data_tuple_headers,
            'data_types_options': data_types_options,
        }

        return render(
            request,
            self.template_name,
            context
        )

class FileValidationSaveDataView(View):
    def __init__(self):
        self.template_name = 'file_validation/save-data.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
    
    def post(self, request, *args, **kwargs):
        csv_data = request.POST['csv_data']
        csv_data = json.loads(csv_data)
        data_tuple_headers = request.POST['data_tuple_headers']
        data_tuple_headers = json.loads(data_tuple_headers)
        csv_data['headers_and_types'] = []

        for header_id, header_name in data_tuple_headers:
            header_type = request.POST[header_id]
            csv_data['headers_and_types'].append((header_name, header_type))

        from file_validation.file_manipulation import FileManipulation

        response_dict = FileManipulation().save_data(csv_data)

        context = {
            'is_save_data': True,
            'status': 200,
        }
        # TODO: Return to main page showing user's dataset list
        return render(
            request,
            self.template_name,
            context
        )
