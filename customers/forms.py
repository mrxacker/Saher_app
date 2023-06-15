from django import forms
from .models import Customer
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError  

class CustomerForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput({'class':'txt-input'}))
    email = forms.EmailField(widget=forms.EmailInput({'class':'txt-input'}))
    full_name = forms.CharField(widget=forms.TextInput({'class':'txt-input'}))
    password1 = forms.CharField(widget=forms.PasswordInput({'class':'txt-input'}))
    password2 = forms.CharField(widget=forms.PasswordInput({'class':'txt-input'}))

    def username_clean(self):  
        username = self.cleaned_data['username'].lower()  
        new = User.objects.filter(username = username)  
        if new.count():  
            raise ValidationError("User Already Exist")  
        return username  
  
    def clean_password2(self):  
        password1 = self.cleaned_data['password1']  
        password2 = self.cleaned_data['password2']  
  
        if password1 and password2 and password1 != password2:  
            raise ValidationError("Password don't match")  
        return password2  
  
    def email_clean(self):  
        email = self.cleaned_data['email'].lower()  
        new = User.objects.filter(email=email)  
        if new.count():  
            raise ValidationError(" Email Already Exist")  
        return email  

    class Meta:
        model = Customer
        fields = "__all__"