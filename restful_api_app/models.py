from django.db import models
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage

files = FileSystemStorage(location='/Users/yejiahn/Desktop/projects/mpulse/mpulse_project/project_app/folder')
# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.IntegerField(blank=True)
    client_member_id = models.IntegerField(blank=True)
    account_id = models.IntegerField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    media = models.FileField(null=True, blank=True, storage=files)

    def __str__(self):
        return self.first_name
    class Meta:
        managed = True
        unique_together = ('phone_number', 'client_member_id')