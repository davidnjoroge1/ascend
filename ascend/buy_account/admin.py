from django.contrib import admin
from .models import Account
from .models import Account, BuyAccountRequest


class AccountAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'follower_count', 'is_new', 'created_at')
    list_filter = ('is_new',)
    search_fields = ('title', 'description')
    ordering = ('-created_at',)

@admin.register(BuyAccountRequest)
class BuyAccountRequestAdmin(admin.ModelAdmin):
    list_display = ('username', 'account', 'package', 'mpesa_code', 'whatsapp_number', 'created_at', 'status')
    search_fields = ('username', 'mpesa_code', 'whatsapp_number')
    list_filter = ('status',)

admin.site.register(Account, AccountAdmin)
