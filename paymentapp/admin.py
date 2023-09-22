from paymentapp.models import Aboutyou,ContactDetail,Address
from django.contrib import admin

class AboutAdmin(admin.ModelAdmin):
     list_display=(id,'fname','lname')
admin.site.register(Aboutyou,AboutAdmin)

class ContactdetailAdmin(admin.ModelAdmin):
     list_display=(id,'email','contact')
admin.site.register(ContactDetail,ContactdetailAdmin)

class AddressAdmin(admin.ModelAdmin):
     list_display=(id,'address1','address2','city','state','zip')

admin.site.register(Address,AddressAdmin)
