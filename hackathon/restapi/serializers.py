# -*- coding: utf-8 -*-

from rest_framework import serializers
from django.contrib.auth.models import User
from hackathon.models import *


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    profile = UserProfileSerializer(many=False)
    class Meta:
        model = User
        fields = ('id', 'username', 'profile')
