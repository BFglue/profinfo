# -*- coding: utf-8 -*-

from models import UserProfile


def profile(request):
    if request.user.is_anonymous():
        return { 'profile': None, 'creator_profile': None }
    else:
        profile, created = UserProfile.objects.get_or_create(user=request.user)
        if created:
            profile.first_name = request.user.first_name
            profile.last_name = request.user.last_name
            profile.save()
        return {
            'profile': profile
        }
