from django.urls import path
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('dashboard/', TemplateView.as_view(template_name="dashboard.html"), name='dashboard'),
    path('signup/', TemplateView.as_view(template_name="signup.html"), name='signup'),
    path('email-verification/<key>/', TemplateView.as_view(template_name="email_verification.html"),
         name='email-verification'),
]
