from logging import PlaceHolder
from tkinter.tix import Form
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, required=False, label="Name:", widget=forms.TextInput(attrs={'class': 'name_Input'}))
    email = forms.CharField(max_length=100, required=True, label="Email:" ,widget=forms.EmailInput(attrs={'class': 'email_Input'}))
    message = forms.CharField(max_length=255, widget=forms.Textarea(attrs={'class': 'message_Input'}), required=False,label="Mesage:")

