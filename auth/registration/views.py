from dj_rest_auth.jwt_auth import set_jwt_cookies
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.utils import jwt_encode
from django.utils.translation import gettext_lazy as _
from rest_framework import status
from rest_framework.response import Response


class VerifyEmailView(VerifyEmailView):
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.kwargs['key'] = serializer.validated_data['key']
        confirmation = self.get_object()
        confirmation.confirm(self.request)
        response = Response({'detail': _('ok')}, status=status.HTTP_200_OK)

        user = confirmation.email_address.user
        access_token, refresh_token = jwt_encode(user)
        set_jwt_cookies(response, access_token, refresh_token)
        return response
