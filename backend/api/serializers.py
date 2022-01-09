from django.contrib.auth.models import User, Group
from rest_framework import serializers
from api import models


class UserSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class DatasetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Dataset
        fields = [
            'id',
            'user_id',
            'filename',
            'content_json',
            'created_at',
            'updated_at',
            'updated_by',
            'deleted_at',
            'deleted_by',
            ]
