from django.forms import ModelForm 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    username= forms.CharField(widget=forms.TextInput(attrs={ "placeholder":"username"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={"placeholder":"enter email"}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"enter password"}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"repeat password"}))
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']