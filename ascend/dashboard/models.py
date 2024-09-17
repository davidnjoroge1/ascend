from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings


class TikTokBoostRequest(models.Model):
    FOLLOWER_PACKAGE_CHOICES = [
        (1000, '1,000 followers - 2,599 KSH'),
        (5000, '5,000 followers - 7,500 KSH'),
        (10000, '10,000 followers - 10,000 KSH'),
        (50000, '50,000 followers - 25,000 KSH'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tiktok_username = models.CharField(max_length=100)
    follower_package = models.IntegerField(choices=FOLLOWER_PACKAGE_CHOICES)
    payment_screenshot = models.ImageField(upload_to='tiktok_payments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"TikTok Boost for {self.tiktok_username} - {self.follower_package} followers"

    def get_payment_screenshot_url(self):
        if self.payment_screenshot:
            return settings.MEDIA_URL + self.payment_screenshot.name
        return ''
class InstagramBoostRequest(models.Model):
    FOLLOWER_PACKAGE_CHOICES = [
        (1000, '1,000 followers - 2,599 KSH'),
        (5000, '5,000 followers - 7,500 KSH'),
        (10000, '10,000 followers - 10,000 KSH'),
        (50000, '50,000 followers - 25,000 KSH'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    instagram_username = models.CharField(max_length=100)
    follower_package = models.IntegerField(choices=FOLLOWER_PACKAGE_CHOICES)
    payment_screenshot = models.ImageField(upload_to='instagram_payments/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Instagram Boost for {self.instagram_username} - {self.follower_package} followers"

    def get_payment_screenshot_url(self):
        if self.payment_screenshot:
            return settings.MEDIA_URL + self.payment_screenshot.name
        return ''

class YouTubeBoostRequest(models.Model):
    BOOST_PACKAGE_CHOICES = [
        ('1000_subs', '1,000 Subscribers - 5,000 KSH'),
        ('5000_subs', '5,000 Subscribers - 20,000 KSH'),
        ('10000_subs', '10,000 Subscribers - 35,000 KSH'),
        ('50000_subs', '50,000 Subscribers - 75,000 KSH'),
    ]

    WATCH_HOURS_CHOICES = [
        ('1000_hours', '1,000 Watch Hours - 3,000 KSH'),
        ('5000_hours', '5,000 Watch Hours - 10,000 KSH'),
        ('10000_hours', '10,000 Watch Hours - 20,000 KSH'),
        ('50000_hours', '50,000 Watch Hours - 50,000 KSH'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    youtube_channel = models.URLField(max_length=200)
    boost_package = models.CharField(max_length=20, choices=BOOST_PACKAGE_CHOICES)
    watch_hours = models.CharField(max_length=20, choices=WATCH_HOURS_CHOICES)
    comment_boost = models.PositiveIntegerField(blank=True, null=True)
    payment_screenshot = models.ImageField(upload_to='youtube_payments/')
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"YouTube Boost for {self.youtube_channel} - {self.boost_package} package"

    def get_payment_screenshot_url(self):
        if self.payment_screenshot:
            return settings.MEDIA_URL + self.payment_screenshot.name
        return ''

class SnapchatBoost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    follower_package = models.CharField(max_length=50)
    payment_screenshot = models.ImageField(upload_to='payment_screenshots/')
    submission_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.username}"
