from django.db import models
from apps.users.models import User

class Dependent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob =  models.DateTimeField()
    gender = models.CharField(max_length=255)
    height = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)
    blood_type = models.CharField(max_length=255)
    image = models.ImageField(upload_to="profile_image", blank=True)
    user = models.ForeignKey(User, related_name="dependents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)