from django.contrib import admin
from Servicesapp.models import Services
# Register your models here.
# class ServicesAdmin(admin.ModelAdmin):
#     list_display=("Name","AboutCook","Price","Catagry","CooksRegistationDate","ContactNumber","Image","labour_id")
# admin.site.register(Services,ServicesAdmin)
admin.site.register(Services)