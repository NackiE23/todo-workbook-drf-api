from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from . import api
from .views import *

urlpatterns = [
    path('', main, name="main"),
    # API
    path('api/drf-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token-auth', obtain_auth_token),
    path('api/tasks', api.TaskListAPIView.as_view(), name="api_tasks"),
    path('api/user_tasks/<user_pk>', api.TaskUserAPIView.as_view(), name="api_tasks"),
    path('api/users', api.UserAPIView.as_view(), name='api_users')
]
