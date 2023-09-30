from django import forms
from core.models import CreditCard

class CreditCardForm(forms.ModelForm):
    name = forms.CharField(widget=forms. TextInput(attrs={"placeholder":"Card Holder Name"}))
    number = forms.CharField(widget=forms. TextInput(attrs={"placeholder":"Card Number"}))
    month = forms.CharField(widget=forms. TextInput(attrs={"placeholder":"Expiry Month"}))
    year = forms.CharField(widget=forms. TextInput(attrs={"placeholder":"Expiry Month"}))
    cvv = forms.CharField(widget=forms. TextInput(attrs={"placeholder":"CVV"}))


    class Meta:
        model = CreditCard
        fields = ['name', 'number', 'month', 'year', 'cvv', 'card_type']
        