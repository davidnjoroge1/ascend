from django import forms
from .models import TikTokBoostRequest

class TikTokBoostRequestForm(forms.ModelForm):
    class Meta:
        model = TikTokBoostRequest
        fields = ['tiktok_username', 'follower_package', 'payment_screenshot']