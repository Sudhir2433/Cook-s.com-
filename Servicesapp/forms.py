from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
from .models import Services
class CookRegistrationForm(forms.ModelForm):
    class Meta:
        model=Services
        fields=('Name','AboutCook','Price','Catagry','CooksRegistationDate','ContactNumber','Image')
    
class SearchForm(forms.Form):
    search_query = forms.CharField(max_length=100,required=False)   