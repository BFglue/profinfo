# -*- coding: utf-8 -*-
import datetime
from django.db import models
from hackathon.models import Profession

EDUCATION_CHOICES = (
    ('Среднее', "Среднее общее"),
    ('Среднее специальное', "Среднее специальное"),
    ('Высшее', "Высшее")
)


class Region(models.Model):
    name = models.CharField(max_length=100)


class ProfInfoRegional(models.Model):
    date = models.DateField(default=datetime.date.today)
    profession = models.ForeignKey(Profession)
    region = models.ForeignKey(Region)
    actuality = models.PositiveIntegerField()
    avg_salary = models.PositiveIntegerField()
    min_education = models.CharField(max_length=100, choices=EDUCATION_CHOICES)


class ProfInfoGlobal(models.Model):
    date = models.DateField(default=datetime.date.today)
    profession = models.ForeignKey(Profession)
    actuality = models.PositiveIntegerField()
    avg_salary = models.PositiveIntegerField()
    min_education = models.CharField(max_length=100, choices=EDUCATION_CHOICES)

