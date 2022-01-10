from django.urls import path
from rest_framework import routers

from .views import UserViewSet, UserStatistic

router = routers.SimpleRouter()
router.register('user', UserViewSet)

urlpatterns = [
    path('statistic/', UserStatistic.as_view(), name='user_statistic'),
]

urlpatterns += router.urls
