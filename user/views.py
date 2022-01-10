from datetime import timedelta

from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserMeta
from .serializers import UserSerializer


class UserViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer


class UserStatistic(APIView):

    def get(self, request, format=None):
        total_signup = User.objects.count()
        today_active_session = UserMeta.objects.filter(last_session__date=timezone.now().date()).count()
        active_session_7_days = UserMeta.objects.filter(
            last_session__gte=timezone.now()-timedelta(days=7)).count()
        average_active_session = round(active_session_7_days / 7, 2)

        return Response({
            'total_signup': total_signup,
            'today_active_session': today_active_session,
            'average_active_session': average_active_session
        })
