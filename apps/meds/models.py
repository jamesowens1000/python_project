from django.db import models
from apps.users.models import User

class Dependent(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dob =  models.DateTimeField()
    gender = models.CharField(max_length=255)
    height = models.CharField(max_length=255, null=True)
    weight = models.CharField(max_length=255, null=True)
    blood_type = models.CharField(max_length=255, null=True)
    # image = models.ImageField(upload_to="profile_image", blank=True)
    user = models.ForeignKey(User, related_name="dependents")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Vaccination(models.Model):
    name = models.CharField(max_length=255)
    abbreviation = models.CharField(max_length=255)
    description = models.TextField()
    url = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Age_Group(models.Model):
    name = models.CharField(max_length=255)
    min_age = models.CharField(max_length=255)
    max_age = models.CharField(max_length=255)
    vaccinations = models.ManyToManyField(Vaccination, related_name="age_groups")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)