from django.db import models

class TikTokBoost(models.Model):
    FOLLOWER_CHOICES = [
        (1000, '1,000 followers - 2,599 KSH'),
        (5000, '5,000 followers - 7,500 KSH'),
        (10000, '10,000 followers - 10,000 KSH'),
        (50000, '50,000 followers - 25,000 KSH'),
    ]

    username = models.CharField(max_length=100)
    follower_package = models.IntegerField(choices=FOLLOWER_CHOICES)
    payment_screenshot = models.ImageField(upload_to='tiktok_screenshots/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"TikTok - {self.username} - {self.follower_package} followers"

class InstagramBoost(models.Model):
    FOLLOWER_CHOICES = [
        (1000, '1,000 followers - 2,599 KSH'),
        (5000, '5,000 followers - 7,500 KSH'),
        (10000, '10,000 followers - 10,000 KSH'),
        (50000, '50,000 followers - 25,000 KSH'),
    ]

    username = models.CharField(max_length=100)
    follower_package = models.IntegerField(choices=FOLLOWER_CHOICES)
    payment_screenshot = models.ImageField(upload_to='instagram_screenshots/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"Instagram - {self.username} - {self.follower_package} followers"

class YouTubeBoost(models.Model):
    SUBSCRIBER_CHOICES = [
        (1000, '1,000 subscribers - 2,599 KSH'),
        (5000, '5,000 subscribers - 7,500 KSH'),
        (10000, '10,000 subscribers - 10,000 KSH'),
        (50000, '50,000 subscribers - 25,000 KSH'),
    ]

    channel_url = models.URLField(max_length=200)
    subscriber_package = models.IntegerField(choices=SUBSCRIBER_CHOICES)
    payment_screenshot = models.ImageField(upload_to='youtube_screenshots/')
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    def __str__(self):
        return f"YouTube - {self.channel_url} - {self.subscriber_package} subscribers"