import os
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import SnapchatBoost, YouTubeBoostRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import TikTokBoostRequest
from django.conf import settings
from django.http import FileResponse, Http404
from .models import InstagramBoostRequest




@login_required(login_url='/authorize/login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')
@login_required(login_url='/authorize/login')
def tiktok_boost(request):
    if request.method == 'POST':
        tiktok_username = request.POST.get('tiktokUsername')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if tiktok_username and follower_package and payment_screenshot:
            try:
                follower_package = int(follower_package)
                if follower_package not in [1000, 5000, 10000, 50000]:
                    raise ValueError("Invalid follower package")

                TikTokBoostRequest.objects.create(
                    user=request.user,
                    tiktok_username=tiktok_username,
                    follower_package=follower_package,
                    payment_screenshot=payment_screenshot
                )
                messages.success(request, 'Your TikTok boost request has been submitted successfully!')
                return redirect('dashboard')
            except ValueError:
                messages.error(request, 'Invalid follower package selected.')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/tiktok.html')

# Instagram Boost View
@login_required(login_url='/authorize/login')
def instagram_boost(request):
    if request.method == 'POST':
        instagram_username = request.POST.get('instagramUsername')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if instagram_username and follower_package and payment_screenshot:
            try:
                follower_package = int(follower_package)
                if follower_package not in [1000, 5000, 10000, 50000]:
                    raise ValueError("Invalid follower package")

                InstagramBoostRequest.objects.create(
                    user=request.user,
                    instagram_username=instagram_username,
                    follower_package=follower_package,
                    payment_screenshot=payment_screenshot
                )
                messages.success(request, 'Your Instagram boost request has been submitted successfully!')
                return redirect('dashboard')
            except ValueError:
                messages.error(request, 'Invalid follower package selected.')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/instagram.html')

# Snapchat Boost View
@login_required(login_url='/authorize/login')
def snapchat_boost(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        follower_package = request.POST.get('followerPackage')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if username and follower_package and payment_screenshot:
            SnapchatBoost.objects.create(
                user=request.user,  # Link to the logged-in user
                username=username,
                follower_package=follower_package,
                payment_screenshot=payment_screenshot
            )
            messages.success(request, 'Your Snapchat boost request has been submitted successfully!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/snapchat.html')

# YouTube Boost View
@login_required(login_url='/authorize/login')
def youtube_boost(request):
    if request.method == 'POST':
        youtube_channel = request.POST.get('youtubeChannel')
        boost_package = request.POST.get('boostPackage')
        watch_hours = request.POST.get('watchHours')
        comment_boost = request.POST.get('commentBoost')
        payment_screenshot = request.FILES.get('paymentScreenshot')

        if youtube_channel and boost_package and watch_hours and payment_screenshot:
            try:
                comment_boost = int(comment_boost) if comment_boost else 0

                YouTubeBoostRequest.objects.create(
                    user=request.user,
                    youtube_channel=youtube_channel,
                    boost_package=boost_package,
                    watch_hours=watch_hours,
                    comment_boost=comment_boost,
                    payment_screenshot=payment_screenshot
                )
                messages.success(request, 'Your YouTube boost request has been submitted successfully!')
                return redirect('dashboard')
            except ValueError:
                messages.error(request, 'Invalid input for comment boost.')
        else:
            messages.error(request, 'Please fill all the required fields.')

    return render(request, 'dashboard/youtube.html')

# Coming Soon View for Other Platforms
@login_required(login_url='/authorize/login')
def coming_soon(request, platform):
    messages.info(request, f'{platform.capitalize()} boost feature is coming soon!')
    return redirect('dashboard')


def serve_media(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'))
    raise Http404