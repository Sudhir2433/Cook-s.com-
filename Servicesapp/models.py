from django.db import models

# Create your models here.



class Services(models.Model):
   

    labour_id = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    AboutCook=models.CharField(max_length=500)
    Price=models.IntegerField(default=0)
    Catagry=models.CharField(max_length=50,default='')
    CooksRegistationDate=models.DateTimeField() 
    ContactNumber=models.CharField(max_length=15,default='')
    Image=models.ImageField(upload_to='shop/images')
    def __str__(self):
        return self.Name