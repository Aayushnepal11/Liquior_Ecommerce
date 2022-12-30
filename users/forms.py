from django import forms
from . models import customerUser
class RegistrationForm(forms.ModelForm):
    class Meta:
        fields = ['__all__']
        model = customerUser
        