from django.db import models

class CommonKey(models.Model):
    # Add any fields you need for the common key here
    pass

class Aboutyou(models.Model):
    common_key = models.OneToOneField(CommonKey, on_delete=models.CASCADE)
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    contact_info = models.OneToOneField('ContactDetail', on_delete=models.CASCADE, related_name='about_you', null=True)
    address_info = models.OneToOneField('Address', on_delete=models.CASCADE, related_name='about_you', null=True)

    def __str__(self):
        return self.fname

class ContactDetail(models.Model):
    common_key = models.OneToOneField(CommonKey, on_delete=models.CASCADE)
    email = models.EmailField()
    contact = models.CharField(max_length=12)

    def __str__(self):
        return self.email

class Address(models.Model):
    common_key = models.OneToOneField(CommonKey, on_delete=models.CASCADE)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip = models.CharField(max_length=6)

    def __str__(self):
        return self.city
