from django.urls import path

from api.views import MyApiView


urlpatterns = [
    # example: /api/v1/
    path('', MyApiView.as_view(), name='api-index'),
]