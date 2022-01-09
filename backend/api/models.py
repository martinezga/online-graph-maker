from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User


class Dataset(models.Model):
    user_id = ForeignKey(User)
    filename = models.CharField(max_length=128)
    content_json = models.JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, default='')
    updated_by = models.CharField(max_length=150, blank=True, default='')
    deleted_at = models.DateTimeField(blank=True, default='')
    deleted_by = models.CharField(max_length=150, blank=True, default='')

    class Meta:
        verbose_name_plural = 'datasets'
