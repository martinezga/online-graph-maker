from django.views import View
from django.shortcuts import render


class PagesView(View):

    def get(self, request, *args, **kwargs):
        return render(request, template_name='home.html')