from django import forms
from .models import contactEnquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model=contactEnquiry
        fields=['Name','Mobile_Number','Email','messege']