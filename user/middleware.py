from django.utils import timezone

from .models import UserMeta


class LastUserSessionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        if request.user.is_authenticated:
            user_meta, _ = UserMeta.objects.get_or_create(user=request.user)
            user_meta.last_session = timezone.now()
            user_meta.save()

        return response
