from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Login(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class":"sign-in-htm"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"sign-in-htm"}))
    

class Register(UserCreationForm):
     username = forms.CharField(widget=forms.TextInput({"class":"group"}))
     password1 = forms.CharField(widget=forms.PasswordInput({"class":"group"}))
     password2 = forms.CharField(widget=forms.PasswordInput({"class":"group"}))
     email = forms.CharField(widget=forms.EmailInput({"class":"group"}))   
     class Meta:
         model = User 
         fields = ["username","password1","password2","email"]
