
from django.db import models
from django.contrib.auth.models import User

class SellRequest(models.Model):
    STATUS_PENDING = 'pending'
    STATUS_APPROVED = 'approved'
    STATUS_DECLINED = 'declined'
    STATUS_TRANSFERRED = 'transferred'
    STATUS_FLAGGED = 'flagged'

    STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_APPROVED, 'Approved'),
        (STATUS_DECLINED, 'Declined'),
        (STATUS_TRANSFERRED, 'Transferred'),
        (STATUS_FLAGGED, 'Flagged'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=STATUS_PENDING)


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tiktokUsername = models.CharField(max_length=100)
    accountDescription = models.TextField()
    accountScreenshot = models.ImageField(upload_to='account_screenshots/')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    admin_comments = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.tiktokUsername} - {self.status}"