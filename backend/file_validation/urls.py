from django.urls import path, include
from file_validation.apps import FileValidationConfig
from file_validation.views import FileValidationMainView


app_name = FileValidationConfig.name
urlpatterns = [
    # example: upload-file/
    path('', FileValidationMainView.as_view(), name='main'),
]