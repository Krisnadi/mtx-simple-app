from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    login_count = serializers.IntegerField(source='usermeta.login_count')
    last_session = serializers.DateTimeField(source='usermeta.last_session')

    class Meta:
        model = User
        fields = (
            'email', 'first_name', 'last_name', 'last_login', 'date_joined', 'login_count', 'last_session')
