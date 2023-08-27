# your_app_name/urls.py
from django.urls import path
from . import views
# Set the app namespace
urlpatterns = [
    path('services/',views.services,name='services'),
    path('CookRegistation/',views.CookRegistation,name='CookRegistation'),
    # path('search/', views.search_view, name='search'),
]
