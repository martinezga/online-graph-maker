from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions
from api import models, serializers
from rest_framework.views import APIView
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = serializers.UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class DatasetList(APIView):

    def get(self, request, format=None):
        datasets = models.Dataset.objects.all()
        serializer = serializers.DatasetSerializer(datasets, many=True)

        return Response(serializer.data)
