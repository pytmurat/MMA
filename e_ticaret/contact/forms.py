from django import forms
from .models import FormModel

class ContactForm(forms.ModelForm):
    #css ler eklenecek widged ile
    isim = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"isim"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control","placeholder":"email"}))
    message = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control","placeholder":"message"}))
    konu = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control","placeholder":"konu"}))
    class Meta:
        model = FormModel
        fields = ["isim","email","konu","message"]
        #burası htmle de ne gorunecek
        
