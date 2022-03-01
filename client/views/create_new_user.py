from django.urls import reverse

from .imports import *
from client.models import User
from django.shortcuts import redirect


def create_new_user(request):
    if request.method == 'POST':
        first_name, last_name = request.POST['name'], request.POST['last_name']
        cellphone = request.POST['cellphone']
        user = User.objects.create(username=cellphone, cellphone=cellphone)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        return redirect(reverse('client:users'))
