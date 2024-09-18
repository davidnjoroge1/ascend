from django import forms
from .models import TikTokAccountSale

class TikTokAccountSaleForm(forms.ModelForm):
    class Meta:
        model = TikTokAccountSale
        fields = ['tiktok_username', 'account_description', 'account_screenshot']
        widgets = {
            'tiktok_username': forms.TextInput(attrs={'placeholder': '@yourusername'}),
            'account_description': forms.Textarea(attrs={'placeholder': 'Describe your account, include your WhatsApp number so our team can reach out to you...'}),
            'account_screenshot': forms.ClearableFileInput(attrs={'accept': 'image/*'}),
        }
