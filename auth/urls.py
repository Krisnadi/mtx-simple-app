from django.urls import path

from .views import VerifyEmailView, GoogleLogin, FacebookLogin, LoginView


urlpatterns = [
    path('account-confirm-email/',
         VerifyEmailView.as_view(),
         name='account_email_verification_sent'),
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path('facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('login/', LoginView.as_view(), name='rest_login'),
]
