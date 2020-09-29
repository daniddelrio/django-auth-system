from django.contrib import admin
from django.urls import path
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('audiences/', audience_view.AudienceList.as_view(), name='audience-list'),
    # path('gcal/events/<int:pk>/', event_auth_view.create_events, name='create_events'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
