from django.db import models

# Create your models here.
# your_app_name/models.py
# from django.contrib.auth.models import Use

class Register(models.Model):
    username=models.CharField(max_length=100,default='xyz@#123')
    email=models.EmailField(max_length=100,default='default@example.com')
    fname=models.CharField(max_length=50,default='xyz')
    lname=models.CharField(max_length=50,default='xyz')
    pass1=models.CharField(max_length=50,default='1234')
    pass2=models.CharField(max_length=50,default='1234')
