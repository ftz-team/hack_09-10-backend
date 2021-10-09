
from django.urls import path, include
from django.conf.urls import url
from rest_framework.generics import CreateAPIView
from .views import *

api_urls = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    # path('user/data/', GetUserDataView.as_view(), name='get_users_data'),
]