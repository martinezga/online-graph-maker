from django.urls import path

from api.views import MyApiView
from api.apps import ApiConfig


app_name = ApiConfig.name
urlpatterns = [
    # example: /api/v1/
    path('', MyApiView.as_view(), name='api-index'),
]