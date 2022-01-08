from django.urls import path

from pages.views import PagesView
from pages.apps import PagesConfig


app_name = PagesConfig.name
urlpatterns = [
    # example: /
    path('', PagesView.as_view(), name='home'),
]