from django.urls import path, include
from file_validation.apps import FileValidationConfig
from . import views


app_name = FileValidationConfig.name
urlpatterns = [
    # example: upload-file/
    path('', views.FileValidationMainView.as_view(), name='main'),
    # example: upload-file/data-type/
    path('data-type/', views.FileValidationDataTypeView.as_view(), name='data_type'),
]