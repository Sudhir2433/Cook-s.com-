from django import forms
from paymentapp.models import Aboutyou,ContactDetail,Address

class AboutyouForm(forms.ModelForm):
    class Meta:
        model=Aboutyou
        fields='__all__'

class ContactDetailForm(forms.ModelForm):
    class Meta:
        model=ContactDetail
        fields='__all__'

class AddressForm(forms.ModelForm):
    class Meta:
        model=Address
        fields='__all__'