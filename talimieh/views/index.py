from django.shortcuts import redirect
from django.contrib.auth.models import Group, Permission, ContentType


def index(request):
    if not (Group.objects.filter(name='normal student').exists()):
        c = ContentType.objects.create(app_label='educational', model='User')
        p = Permission.objects.create(name='normal student', content_type=c)
        p.save()
        g = Group.objects.create(name='normal student')
        g.permissions.add(p)
        g.save()
    if not (Group.objects.filter(name='site admins').exists()):
        c = ContentType.objects.create(app_label='client', model='User')
        p = Permission.objects.create(name='site admin', content_type=c)
        p.save()
        g = Group.objects.create(name='site admin')
        g.permissions.add(p)
        g.save()
    return redirect('/accounts/dashboard/')
