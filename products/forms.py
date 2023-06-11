from django import forms
from .models import Product
from subcategories.models import Subcategory

class ProductForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    subcategory = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=Subcategory.objects.all())
    image = forms.ImageField()
    price_old = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}), required=False)
    price_new = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    desc = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    
    class Meta:
        model = Product
        fields = "__all__"

        