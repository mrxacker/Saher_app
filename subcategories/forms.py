from django import forms
from .models import Subcategory
from categories.models import Category

class SubcategoryForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    category = forms.ModelChoiceField(widget=forms.Select(attrs={'class':'form-control'}), queryset=Category.objects.all())
    icon = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = Subcategory
        fields = "__all__"

        