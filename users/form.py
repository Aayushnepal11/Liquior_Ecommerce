from django import forms
from . models import CustomerUsers

class UserCreationForm(CustomerUsers):
    first_name = forms.CharField(max_length=50, required=True, label="First Name:", widget=forms.TextInput(attrs={'class': 'textInput'}))
    last_name = forms.CharField(max_length=50, required=True, label="Last Name:", widget=forms.TextInput(attrs={'class': 'textInput'}))
    email = forms.CharField(max_length=100, required=True, label="Email:", widget=forms.EmailInput(attrs={'class': 'emailInput'}))
    password = forms.CharField(max_length=100, required=True, label="Password:", widget=forms.PasswordInput(attrs={'class': 'passwordInput'}))
    confirm_password = forms.CharField(max_length=100, required=True, label="Confirm Password:", widget=forms.PasswordInput(attrs={'class': 'passwordInput'}))
    phone = forms.CharField(max_length=50, required=True, label="Phone:", widget=forms.TextInput(attrs={'class': 'textInput'}))
    DOB = forms.CharField(max_length=50, required=True, label='DOB:',widget=forms.DateTimeInput(attrs={'class': 'textInput'}))
    gender = forms.CharField(max_length=50, label="Gender:", widget=forms.RadioSelect(choices=('Male', 'Female', 'Others')))
    """    class Meta:
        model = CustomerUsers
        fields = [
            'first_name', 'last_name', 'email', 'password',
            'confirm_password', 'phone', 'DOB', 'gender'
            ]
        """