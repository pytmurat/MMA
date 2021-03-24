from django import forms
from django.contrib.auth.forms import UserCreationForm

class Login(forms.Form):
    username = forms.CharField()
    password = forms.CharField()
    

 class Register(UserCreationForm):
     username = forms.CharField()
     password1 = forms.CharField()
     password2 = forms.CharField()
     email = forms.CharField()   
     class Meta:
         model = User 
         fields = ["username","password1","password2","email"]
