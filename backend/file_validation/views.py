from django.views import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages


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

        input_file = FileManipulation()
        pre_processed_data = input_file.pre_process_data(csv_file)

        messages.success(request, f'File {csv_file.name} uploaded successfully')
        context = {
            'is_csv_display': True,
            'headers': pre_processed_data[0],
            'data': pre_processed_data[1],
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
        csv_headers = request.POST['csv_headers_list']
        csv_data = request.POST['csv_data_list']

        context = {
            'csv_headers': csv_headers,
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
