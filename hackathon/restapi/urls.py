# -*- coding: utf-8 -*-

from django.conf.urls import include, url

from rest_framework import routers
from hackathon.restapi import views
from hackathon.api import *

restapi_router = routers.DefaultRouter()
restapi_router.register(r'users', views.UserViewSet, base_name='users')


urlpatterns = [
    url(r'^profile/$', profile),
    url(r'^abiturient/profession/$', abiturient_profession),
    url(r'^', include(restapi_router.urls)),
]