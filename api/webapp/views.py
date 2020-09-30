from django.shortcuts import render

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from phone_verify.api import VerificationViewSet
from phone_verify import serializers as phone_serializer
from . import services, serializers

from webapp.models import *
from webapp.services import create_user_account, send_verification_email

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from phone_verify.serializers import SMSVerificationSerializer
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

@api_view()
def activate(request, uidb64, token):
    try:
        # uid = force_text(urlsafe_base64_decode(uidb64))
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    user.is_active = True
    user.save()

    response = {
        'email': user.email,
        'phone_number': user.phone_number,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }

    return Response(response)

class UserViewSet(VerificationViewSet):
    # permission_classes = [TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny], serializer_class=SMSVerificationSerializer)
    def login(self, request):
        phone_number = request.data.get('phone_number', None)

        if not User.objects.filter(phone_number=phone_number).exists():
            return Response({ "message": "User with phone number does not exist" }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(phone_number=phone_number).first()
        if not user.is_active:
            return Response({ "message": "User has not activated their email." }, status=status.HTTP_400_BAD_REQUEST)

        serializer = SMSVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'phone_number': user.phone_number,
        }, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny], serializer_class=serializers.PhoneSerializer)
    def verify_and_register(self, request):

        serializer = phone_serializer.SMSVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_serializer = serializers.UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)

        user_data = {
            'email': user_serializer.validated_data.get('email', None),
            'password': 'test',
            'first_name': user_serializer.validated_data.get('first_name', None),
            'last_name': user_serializer.validated_data.get('last_name', None),
            'phone_number': user_serializer.validated_data.get('phone_number', None),
        }
        user = services.create_user_account(**user_data)
        send_verification_email(user, user.email)

        return Response(user_serializer.data)
