# your_app_name/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):
    # You can add additional fields to the form here if needed.
    # Example: email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username' ,'email','first_name','last_name','password1', 'password2']
    # email validation


        email = forms.EmailField()
        def clean_email(self):
            email = self.cleaned_data.get('email')
            if User.objects.filter(email=email).exists():
               raise forms.ValidationError("This email is already registered.")
            return email  

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)