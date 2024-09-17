from django.shortcuts import render, redirect
from django.contrib import messages
from .models import TikTokBoost, InstagramBoost, YouTubeBoost

def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

def tiktok_boost(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if username and follower_package and payment_screenshot:
            TikTokBoost.objects.create(
                username=username,
                follower_package=follower_package,
                payment_screenshot=payment_screenshot
            )
            messages.success(request, 'Your TikTok boost request has been submitted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/tiktok.html')

def instagram_boost(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if username and follower_package and payment_screenshot:
            InstagramBoost.objects.create(
                username=username,
                follower_package=follower_package,
                payment_screenshot=payment_screenshot
            )
            messages.success(request, 'Your Instagram boost request has been submitted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/instagram.html')

def snapchat_boost(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if username and follower_package and payment_screenshot:
            snapchat_boost.objects.create(
                username=username,
                follower_package=follower_package,
                payment_screenshot=payment_screenshot
            )
            messages.success(request, 'Your Snapchat boost request has been submitted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/snapchat.html')

def youtube_boost(request):
    if request.method == 'POST':
        channel_url = request.POST.get('channelUrl')
        subscriber_package = request.POST.get('subscriberPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if channel_url and subscriber_package and payment_screenshot:
            YouTubeBoost.objects.create(
                channel_url=channel_url,
                subscriber_package=subscriber_package,
                payment_screenshot=payment_screenshot
            )
            messages.success(request, 'Your YouTube boost request has been submitted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/youtube.html')



def coming_soon(request, platform):
    messages.info(request, f'{platform.capitalize()} boost feature is coming soon!')
    return redirect('dashboard')