from django.urls import path, include
from rest_framework import routers

from api import views
from api.apps import ApiConfig


router = routers.DefaultRouter()
# example: /api/v1/users/
router.register(r'users', views.UserViewSet)
# example: /api/v1/datasets/
router.register(r'datasets', views.UserViewSet)


app_name = ApiConfig.name
urlpatterns = [
    # example: /api/v1/
    path('', views.MyApiView.as_view(), name='api-index'),
    path('', include(router.urls)),
]