from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_verified = models.BooleanField(default=False)
    account_type = models.CharField(max_length=10, choices=[('company', 'Company'), ('personal', 'Personal')])

class CompanyAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    registration_number = models.CharField(max_length=100)
    secret_number = models.CharField(max_length=10)
    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)
    address = models.TextField()
    key_officers_details = models.TextField()
    organization_type = models.CharField(max_length=100)

class PersonalAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.CharField(max_length=10, choices=[('male', 'Male'), ('female', 'Female')])
    address = models.TextField()
    security_question = models.CharField(max_length=255)
    security_answer = models.CharField(max_length=255)
