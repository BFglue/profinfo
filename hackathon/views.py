# -*- coding: utf-8 -*-

import json
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth import logout as django_logout, authenticate, login as django_login
from django.contrib.auth.decorators import login_required

from django.conf import settings
from django.contrib.auth.models import User


def login(request):
    if request.method == 'POST':
        if request.POST.get('username'):
            username = request.POST['username']
            password = request.POST['password']
            username = username.replace(' ', '')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                django_login(request, user)
                next = request.GET.get('next', '/vuz/')
                response = HttpResponseRedirect(next)
                return response
            else:
                user_exists = User.objects.filter(username=username, is_active=False)
                if user_exists:
                    return HttpResponseRedirect('/login/?not_active=1&username=' + username)
                else:
                    return HttpResponseRedirect('/login/?invalid=1&username=' + username)
        else:
            return HttpResponse("No username provided", status=403)
    else:
        return render(request, 'registration/login.html')


@login_required
def logout(request):
    django_logout(request)
    return HttpResponseRedirect('/login/')


# @group_required('managers', raise_exception=True)
@login_required
def app(request):
    context = {}
    return render(request, 'hackathon/templates/app.html', context)


def index(request):
    context = {}
    return render(request, 'hackathon/templates/index.html', context)

@login_required
def vuz(request):
    context = {}
    return render(request, 'hackathon/templates/vuz.html', context)


def abiturient(request):
    context = {}
    return render(request, 'hackathon/templates/abiturient.html', context)


# # Redirect to page depends on user group
# @login_required
# def router(request):
#     # ...
#     user = request.user
#     if user.groups.filter(name='managers').exists():
#         return HttpResponseRedirect('/manager/')
#     if user.groups.filter(name='logists').exists():
#         return HttpResponseRedirect('/logist/order/')
#     if user.groups.filter(name='accountants').exists():
#         return HttpResponseRedirect('/accountant/pending/')

#     return HttpResponseRedirect('/admin/')

