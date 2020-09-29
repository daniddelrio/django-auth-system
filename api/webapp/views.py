from django.shortcuts import render

from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from phone_verify.api import VerificationViewSet
from phone_verify import serializers as phone_serializer
from . import services, serializers

class UserViewSet(VerificationViewSet):

    @action(detail=False, methods=['POST'], permission_classes=[AllowAny], serializer_class=serializers.PhoneSerializer)
    def verify_and_register(self, request):

        serializer = phone_serializers.SMSVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user_serializer = serializers.UserSerializer(data=request.data)
        user_serializer.is_valid(raise_exception=True)
        user = services.create_user_account(**user_serializer.validated_data)

        return Response(user_serializer.data)