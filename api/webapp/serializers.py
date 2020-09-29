from rest_framework import serializers

from webapp.models import *
from phone_verify.serializers import SMSVerificationSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['__all__']

class PhoneSerializer(UserSerializer, SMSVerificationSerializer):
	pass