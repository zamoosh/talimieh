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
        user.save()
        return redirect(reverse('client:users'))
