from django import forms  
from django.contrib.auth.models import User  
from django.contrib.auth.forms import UserCreationForm  
from django.core.exceptions import ValidationError  
from django.forms.fields import EmailField  
from django.forms.forms import Form  
from django.contrib.auth.forms import AuthenticationForm
  

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username:', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'txt-input','placeholder':'Username'}))  
    password = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class':'txt-input','placeholder':'Password'}))  



class CustomUserCreationForm(UserCreationForm):  
    username = forms.CharField(label='Username:', min_length=5, max_length=150, widget=forms.TextInput(attrs={'class':'txt-input'}))  
    password1 = forms.CharField(label='Password:', widget=forms.PasswordInput(attrs={'class':'txt-input'}))  
    password2 = forms.CharField(label='Confirm password:', widget=forms.PasswordInput(attrs={'class':'txt-input'}))  
    email = forms.EmailField(label='Email:', widget=forms.EmailInput(attrs={'class':'txt-input'}))  
    is_superuser = forms.BooleanField(label='This is Admin User', required=False)

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

    def save(self, commit = True):  
        user = User.objects.create_user(  
            username= self.cleaned_data['username'],   
            password= self.cleaned_data['password1'] ,
            email= self.cleaned_data['email'],
            is_superuser= self.cleaned_data['is_superuser'] 
        )  
        return user  