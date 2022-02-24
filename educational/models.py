from django.db import models
from .imports import *
from client.models import *


class Universities(models.Model):
    uni_name = models.CharField(max_length=50, null=True, blank=True)
    comment = models.TextField(null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)


class Year_semester(models.Model):
    title = models.CharField(max_length=4)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    status = models.BooleanField(default=True)


class Degree_field_study(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    document = models.TextField(null=True, blank=True)
    status = models.BooleanField(default=True)


class Semester(models.Model):
    university = models.ForeignKey(Universities, on_delete=models.CASCADE)
    degree_field_study = models.ForeignKey(Degree_field_study, on_delete=models.CASCADE)
    year_semester = models.ForeignKey(Year_semester, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    scholarship = models.BooleanField(default=True)
    expert_price = models.CharField(max_length=25)
    entrance_price = models.CharField(max_length=25)


class Educational_request(models.Model):
    average = models.CharField(max_length=10, blank=True, null=True)
    field_study = models.CharField(max_length=25, blank=True, null=True)
    former_university = models.CharField(max_length=25, blank=True, null=True)
    college = models.ForeignKey(Semester, on_delete=models.CASCADE)
    document = models.ForeignKey(Owner_document, on_delete=models.CASCADE)
