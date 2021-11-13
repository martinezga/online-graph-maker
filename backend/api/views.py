from django.views import View
from django.http.response import JsonResponse


class MyApiView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, World!'})
