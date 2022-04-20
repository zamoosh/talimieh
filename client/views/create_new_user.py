from .imports import *
from client.models import User
from django.shortcuts import redirect


def create_new_user(request):
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST['cellphone'],
                                        cellphone=request.POST['cellphone'],
                                        password=request.POST['cellphone'],
                                        first_name=request.POST['name'],
                                        last_name=request.POST['last_name'])
        p = Permission.objects.get(name__icontains='normal')
        user.user_permissions.add(p)
        user.save()
        return redirect(reverse('client:users'))
