from django.views import View
from django.shortcuts import render, redirect
from django.http.response import JsonResponse
from django.contrib import messages


class FileValidationMainView(View):
    def __init__(self):
        self.template_name = 'file_validation/file_validation.html'

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

        # TODO: Pre-process data in csv file
        input_file = FileManipulation(csv_file)
        pre_processed_data = input_file.pre_process_data()
        # TODO: Show pre-processed data in frontend to user
        # TODO: Get user validation
        # TODO: Save data to database
        messages.success(request, f'File {csv_file.name} uploaded successfully')
        context = {
            'display_csv': True,
            'headers': pre_processed_data[0],
            'data_type': pre_processed_data[1],
            'data': pre_processed_data[2],
        }
        return render(
            request,
            self.template_name,
            context
        )
