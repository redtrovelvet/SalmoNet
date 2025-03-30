from django.core.cache import cache
from django.http import HttpResponse

class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.max_requests = 10
        self.time_window = 60

    def __call__(self, request):
        key = f'rate_limit:{request.user.id}'
        requests_made = cache.get(key, 0)
        if requests_made >= self.max_requests:
            return HttpResponse('Too Many Requests', status=429)
        cache.set(key, requests_made + 1, self.time_window)
        return self.get_response(request)