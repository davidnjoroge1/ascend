from django import forms
from .models import BuyAccountRequest

class BuyAccountRequestForm(forms.ModelForm):
    class Meta:
        model = BuyAccountRequest
        fields = ['account', 'username', 'package', 'mpesa_code', 'whatsapp_number']
