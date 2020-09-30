from rest_framework import serializers

from webapp.models import *
from phone_verify.serializers import SMSVerificationSerializer

class UserSerializer(serializers.ModelSerializer):
    session_token = serializers.CharField(max_length=255)
    security_code = serializers.CharField(max_length=6)

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'phone_number',
            'session_token',
            'security_code'
        ]

class LoginSerializer(serializers.ModelSerializer):
    session_token = serializers.CharField(required=True, max_length=255)
    security_code = serializers.CharField(required=True, max_length=6)

    class Meta:
        model = User
        fields = [
            'phone_number',
            'session_token',
            'security_code'
        ]

    def validate(self, data):
        password = data['password']

        if not email:
            raise Validation('An email must exist.')

        # making sure that this email exists
        user = User.objects.filter(
                Q(email=email)
            ).distinct()


        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise ValidationError('This username is not valid.')

        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError('Incorrect credentials please try again.')
            
        data['token'] = 'SOME RANDOM TOKEN'


        return data

class PhoneSerializer(UserSerializer, SMSVerificationSerializer):
	pass