# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    fio = models.CharField(max_length=255, blank=True)
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    phone = models.CharField(max_length=100, blank=True)

    def __unicode__(self):
        return str(self.user)

    @property
    def shortname(self):
        if self.fio != "":
            pieces = self.fio.split()
            result = pieces[0]
            for r in pieces[1:]:
                result += ' '
                result += r[0] + '. '
            return result
        else:
            return ""


class Profession(models.Model):
    name = models.CharField(max_length=255)
    etks = models.CharField(max_length=100, blank=True)
    category = models.CharField(max_length=100, blank=True)


class Vacancy(models.Model):
    initial_profession = models.ForeignKey(Profession, related_name="vacancies_initial")
    predicted_profession = models.ForeignKey(Profession, related_name="vacancies_predicted", null=True)
    category = models.CharField(null=True, blank=True, max_length=255)
    # region = models.ForeignKey("Region", null=True, blank=True)
    region_code = models.CharField(null=True, blank=True, max_length=255)
    region_name = models.CharField(null=True, blank=True, max_length=255)
    salary_min = models.CharField(null=True, blank=True, max_length=255)
    salary_max = models.CharField(null=True, blank=True, max_length=255)
    job_name = models.TextField(blank=True, default="")
    duty = models.TextField(blank=True, default="")
    education = models.CharField(null=True, blank=True, max_length=255)


class Region(models.Model):
    region_code = models.CharField(null=True, blank=True, max_length=255)
    region_name = models.CharField(null=True, blank=True, max_length=255)


class ClassOkso(models.Model):
    name = models.CharField(null=True, blank=True, max_length=512)
    professions = models.ManyToManyField(Profession, blank=True)


@receiver(post_save, sender=User)
def create_userprofile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
