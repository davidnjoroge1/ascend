from django.http import JsonResponse
from django.shortcuts import render
from .models import Account
from .forms import BuyAccountRequestForm

def account_list(request):
    accounts = Account.objects.all()
    new_products = Account.objects.filter(is_new=True)
    return render(request, 'buy_account/account_list.html', {'accounts': accounts, 'new_products': new_products})

def buy_account(request):
    if request.method == 'POST':
        form = BuyAccountRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            # Provide detailed error messages
            return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    return JsonResponse({'success': False, 'message': 'Invalid request method'})
