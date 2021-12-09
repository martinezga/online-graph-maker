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

        if not csv_file.name.endswith('.csv'):
            return JsonResponse({'status': 'no es un csv'})

        if csv_file.multiple_chunks():
            return JsonResponse({'status': 'archivo demasiado grande'})

        return JsonResponse({'status': csv_file.name})
        # messages.success(request, 'File uploaded successfully')
        # return redirect('file_validation:main')
