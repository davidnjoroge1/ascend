
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SellRequest
from django.contrib import messages

@login_required
def sell(request):
    user_requests = SellRequest.objects.filter(user=request.user).order_by('-created_at')

    if request.method == 'POST':
        tiktokUsername = request.POST.get('tiktokUsername')
        accountDescription = request.POST.get('accountDescription')
        accountScreenshot = request.FILES.get('accountScreenshot')

        if tiktokUsername and accountDescription and accountScreenshot:
            SellRequest.objects.create(
                user=request.user,
                tiktokUsername=tiktokUsername,
                accountDescription=accountDescription,
                accountScreenshot=accountScreenshot
            )
            messages.success(request, 'Your sell request has been submitted successfully!')
            return redirect('sell:sell')
        else:
            messages.error(request, 'Please fill out all fields and upload a screenshot.')

    return render(request, 'sell/sell.html', {'user_requests': user_requests})

@login_required
def delete_request(request, request_id):
    sell_request = SellRequest.objects.get(id=request_id, user=request.user)
    sell_request.delete()
    messages.success(request, 'Your sell request has been deleted.')
    return redirect('sell:sell')