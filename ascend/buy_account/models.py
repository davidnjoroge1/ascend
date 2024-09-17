from django.db import models

class Account(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='account_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    follower_count = models.PositiveIntegerField()  # Custom number of followers
    is_new = models.BooleanField(default=False)  # Flag to indicate if the account is new
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BuyAccountRequest(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    username = models.CharField(max_length=255)
    package = models.CharField(max_length=255)  # Package details, e.g., '1,000 followers'
    mpesa_code = models.CharField(max_length=255, blank=True, null=True)
    whatsapp_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return f"{self.username} - {self.account.title}"
