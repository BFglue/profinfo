# -*- coding: utf-8 -*-

import json
import requests
from operator import itemgetter
from decimal import Decimal
from django.db.models import F
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.conf import settings
from requests.auth import HTTPBasicAuth

from hackathon.models import *
# from hackathon.restapi.serializers import UserProfileSerializer


@login_required
def profile(request):
    groups_items = request.user.groups.all()
    groups = []
    for gi in groups_items:
        groups.append(gi.name)
    result = {
        'fio': request.user.profile.fio,
        'phone': request.user.profile.phone,
        'is_staff': request.user.is_staff,
        'groups': groups
    }
    return JsonResponse(result)


def abiturient_profession(request):
    result = {
        "test": True
    }
    return JsonResponse(result, safe=False)