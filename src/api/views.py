from django.shortcuts import render
from django.db.models import query
from django.http import request
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import filters

from core.models import *
from .serializers import *


class CreateDatasetView(generics.CreateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [AllowAny]


class UpdateDatasetView(generics.UpdateAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]


class GetDatasetsView(generics.ListAPIView):
    queryset = Dataset.objects.all()
    serializer_class = GetDatasetSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['type', 'owner', 'status', 'id']
    search_fields = ['name', 'description']


class DeleteDatasetView(generics.DestroyAPIView):
    queryset = Dataset.objects.all()
    serializer_class = DatasetSerializer
    permission_classes = [IsAuthenticated]


class GetTagsView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]


class GetCompaniesView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]