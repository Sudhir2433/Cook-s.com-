from django.db import models
from tinymce.models import HTMLField
class contactEnquiry(models.Model):
    Name=models.CharField(max_length=50)
    Mobile_Number=models.CharField(max_length=50)
    Email=models.CharField(max_length=50)
    messege=models.TextField()

class News(models.Model):
    title=models.CharField(max_length=150)
    news_desc=HTMLField()