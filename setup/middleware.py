from django.conf import settings
from django.shortcuts import redirect
from django.urls import resolve

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        public_views = ['login', 'logout', 'registro',]

        current_view = resolve(request.path_info).url_name

        if request.path.startswith('/admin'):
            return self.get_response(request)

        if not request.user.is_authenticated and current_view not in public_views:
            return redirect('login')
        
        return self.get_response(request)