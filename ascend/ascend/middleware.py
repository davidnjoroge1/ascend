from django.shortcuts import redirect
from django.urls import reverse, resolve
from django.conf import settings

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # List of URL patterns that require authentication
        protected_routes = [
            'dashboard',
            'profile',
            # Add other URL patterns that require authentication
        ]

        # Check if the current path requires authentication
        if not request.user.is_authenticated:
            # Resolve the current path to a URL name
            try:
                current_url_name = resolve(request.path_info).url_name
            except:
                current_url_name = None

            if current_url_name in protected_routes:
                # Redirect to login page if user is not authenticated
                return redirect(f"{reverse('login')}?next={request.path}")

        response = self.get_response(request)
        return response