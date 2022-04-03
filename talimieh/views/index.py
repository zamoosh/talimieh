from django.shortcuts import redirect
from django.contrib.auth.models import Group


def primary_groups():
    group, created = Group.objects.get_or_create(name='مدیر کل')
    if created:
        group.save()
    group, created = Group.objects.get_or_create(name='دانش‌آموز ساده')
    if created:
        group.save()
    group, created = Group.objects.get_or_create(name='کارشناس آموزشی')
    if created:
        group.save()
    group, created = Group.objects.get_or_create(name='کارشناس ثبت‌نام')
    if created:
        group.save()
    group, created = Group.objects.get_or_create(name='کارشناس مالی')
    if created:
        group.save()


def index(request):
    primary_groups()
    return redirect('/accounts/dashboard/')
