from django.shortcuts import redirect
from django.contrib.auth.models import Group


def primary_groups():
    group, created = Group.objects.get_or_create(name='site admin')
    if created:
        group.save()
    group, created = Group.objects.get_or_create(name='normal student')
    if created:
        group.save()


def index(request):
    primary_groups()
    return redirect('/accounts/dashboard/')
