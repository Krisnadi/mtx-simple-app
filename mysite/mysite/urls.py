"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
# from django.views.generic import TemplateView
# from drf_yasg.views import get_schema_view
# from drf_yasg import openapi


# schema_view = get_schema_view(
#     openapi.Info(
#         title='API Docs',
#         default_version='v1',
#     )
# )

urlpatterns = [
    path('', include('frontsite.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/', include('auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('password-reset/confirm/<uidb64>/<token>/',
    #      TemplateView.as_view(template_name="password_reset_confirm.html"),
    #      name='password_reset_confirm'),
    # path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='api_docs'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
