from django.contrib import admin
from django.urls import path
# from cooks.views import SaveContactForm
from . import views
urlpatterns = [
    path('quickview/<int:labour_id>',views.quickview,name='quickview'),
    path('address/<int:labour_id>/',views.address,name='address'),
    path('contactDetail/',views.contactDetail,name='contactDetail'),
    path('aboutyou/',views.aboutyou,name='aboutyou'),
    path('paynow/',views.paynow,name='paynow'),
]
