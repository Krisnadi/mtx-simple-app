from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from dj_rest_auth.registration.views import VerifyEmailView, SocialLoginView


class VerifyEmailView(VerifyEmailView):
    pass


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
