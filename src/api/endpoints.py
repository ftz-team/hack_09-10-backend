
from django.urls import path, include
from django.conf.urls import url
from rest_framework.generics import CreateAPIView
from .views import *

api_urls = [
    # path('user/data/', GetUserDataView.as_view(), name='get_users_data'),
]