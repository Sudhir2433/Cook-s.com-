from django.contrib import admin
from django.urls import path
# from cooks.views import SaveContactForm
from . import views
urlpatterns = [
    
    
    path('quickview/<int:labour_id>',views.quickview,name='quickview'),
    # path('SaveContactForm/',views.SaveContactForm,name='SaveContactForm')
]
