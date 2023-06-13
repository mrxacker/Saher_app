from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={'class':'txt-input','placeholder':'Your Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'txt-input','placeholder':'Email Address'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'class':'txt-input','placeholder':'Phone Number'}))
    message = forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'txt-input',
            'placeholder':'Leave Message',
            'cols':30,
            'rows':9}))
    class Meta:
        model = Feedback
        fields = "__all__"

        