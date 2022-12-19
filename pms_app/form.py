from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User

from phone_field import PhoneField
from django.contrib.auth.password_validation import validate_password
from django.core import validators


class RegisterForm(UserCreationForm):
    # username = forms.CharField(max_length=100,required=True,
    #                             widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(required=True,
    #                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    # first_name= forms.CharField(max_length=100,required=True,
    #                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    # last_name= forms.CharField(max_length=100,required=True,
    #                          widget=forms.TextInput(attrs={'class': 'form-control'}))
    # password1= forms.PasswordInput(
    #                         widget=forms.Input(attrs={'class': 'form-control'}))
    # password2= forms.PasswordInput(
    #                         attrs={'class': 'form-control'})
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username','email', 'password1', 'password2', 'is_staff','groups']