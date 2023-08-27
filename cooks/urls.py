from django.contrib import admin
from django.urls import path,include
# from cooks.views import SaveContactForm
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    # path('SaveContactForm/',views.SaveContactForm,name='SaveContactForm')
]
