from allauth.account.adapter import get_adapter
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import VerifyEmailView
from dj_rest_auth.views import LoginView

from user.models import UserMeta


class VerifyEmailView(VerifyEmailView):
    pass


class LoginView(LoginView):

    def add_login_count(self):
        user_meta, _ = UserMeta.objects.get_or_create(user=self.user)
        user_meta.login_count += 1
        user_meta.save()

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        self.serializer.is_valid(raise_exception=True)

        self.login()
        self.add_login_count()
        return self.get_response()


class CustomSocialLoginView(LoginView):
    serializer_class = SocialLoginSerializer

    def process_login(self):
        get_adapter(self.request).login(self.request, self.user)


class GoogleLogin(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(CustomSocialLoginView):
    adapter_class = FacebookOAuth2Adapter
