from django.contrib import admin
from .models import Register
# Register your models here.

# class ServicesAdmin(admin.ModelAdmin):
# list_display=("Name","AboutCook","Price","Catagry","CooksRegistationDate","ContactNumber","Image","labour_id")
class RegisterAdmin(admin.ModelAdmin):
    list_display=('username','email','fname','lname','pass1','pass2')
admin.site.register(Register,RegisterAdmin)