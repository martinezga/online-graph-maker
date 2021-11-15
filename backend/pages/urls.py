from django.urls import path

from pages.views import PagesView


urlpatterns = [
    # example: /
    path('', PagesView.as_view(), name='home'),
]