from django.http.response import JsonResponse
from django.views import View
from django.shortcuts import render


class FileValidationMainView(View):
    def __init__(self):
        self.template_name = 'file_validation/file_validation.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
        )
