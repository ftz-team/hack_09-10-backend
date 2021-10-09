
from django.urls import path, include
from django.conf.urls import url
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .views import *

api_urls = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('datasets/get/', GetDatasetsView.as_view(), name='get_datasets'),
    path('datasets/update/<int:pk>/', UpdateDatasetView.as_view(), name='update_dataset'),
    path('datasets/delete/<int:pk>/', DeleteDatasetView.as_view(), name='delete_dataset'),
    path('datasets/create/', CreateDatasetView.as_view(), name='create_dataset'),
]