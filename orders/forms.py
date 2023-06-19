from django import forms
from .models import Order


payment_methods = [
    ('cash', 'CASH'),
    ('cart', 'Credit Cart'),
]

class OrderForm(forms.ModelForm):

    payment_type = forms.CharField(widget=forms.RadioSelect(choices=payment_methods))
    full_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','rows':'5'}))
    
    class Meta:
        model = Order
        fields = ['payment_type', 'full_name', 'phone_number', 'address','note']
