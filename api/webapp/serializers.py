from rest_framework import serializers

from webapp.models import *
from phone_verify.serializers import SMSVerificationSerializer

class UserSerializer(serializers.ModelSerializer):
    session_token = serializers.CharField(required=True, max_length=255)
    security_code = serializers.CharField(required=True, max_length=6)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password',
            'phone_number',
            'session_token',
            'security_code'
        ]

class PhoneSerializer(UserSerializer, SMSVerificationSerializer):
	pass