from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter
from webapp.views import *

default_router = DefaultRouter(trailing_slash=False)
default_router.register('phone', UserViewSet, basename='phone')

urlpatterns = [
    # path('audiences/', audience_view.AudienceList.as_view(), name='audience-list'),
    # path('gcal/events/<int:pk>/', event_auth_view.create_events, name='create_events'),
]

urlpatterns += default_router.urls
