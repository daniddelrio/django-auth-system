from django.shortcuts import render

from rest_framework import status, viewsets, permissions
from rest_framework.decorators import action, api_view
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from phone_verify.api import VerificationViewSet
from phone_verify import serializers as phone_serializer
from . import services, serializers

from webapp.models import *
from webapp.services import create_user_account

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

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

    return Response(user)

class UserViewSet(VerificationViewSet):
    # permission_classes = [TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny], serializer_class=serializers.PhoneSerializer)
    def verify_and_register(self, request):

        serializer = phone_serializer.SMSVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user_serializer = serializers.UserSerializer(data=request.data)
        # user_serializer = serializers.UserSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)

        user_data = {
            'email': user_serializer.validated_data.get('email', None),
            'password': user_serializer.validated_data.get('password', None),
            'first_name': user_serializer.validated_data.get('first_name', None),
            'last_name': user_serializer.validated_data.get('last_name', None),
            'phone_number': user_serializer.validated_data.get('phone_number', None),
        }
        user = services.create_user_account(**user_data)
        # user = services.create_user_account(email=email, password=password, first_name=first_name, last_name=last_name, phone_number=phone_number)

        return Response(user_serializer.data)