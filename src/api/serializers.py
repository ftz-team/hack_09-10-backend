from django.db.models import fields
from rest_framework import serializers

from core.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('pk', 'name')


class DatasetSerializer(serializers.ModelSerializer):
    owner = CompanySerializer()
    tags = TagSerializer(many=True)
    class Meta:
        model = Dataset
        fields = '__all__'