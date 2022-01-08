from django.views import View
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api.serializers import UserSerializer


class MyApiView(View):

    def get(self, request, *args, **kwargs):
        return JsonResponse({'message': 'Hello, World!'})


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

