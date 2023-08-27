from django.contrib import admin
from cooks.models import contactEnquiry,News
# Register your models here.
# class ContactAdmin(admin.ModelAdmin):
#     list_display=('Name','subject','Email','message')
admin.site.register(contactEnquiry) #with the help of this both ContactEnquery,ContactAdmin together     
# admin.site.register(contactEnquiry)

class NewsAdmin(admin.ModelAdmin):
    list_display=('title','news_desc')
admin.site.register(News,NewsAdmin)    