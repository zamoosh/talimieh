from .imports import *
from django.shortcuts import get_object_or_404, redirect
from client.models import User


def make_staff(request, u_id):
    if request.method == 'POST':
        u = get_object_or_404(User, id=u_id)
        if u.is_staff:
            u.is_staff = False
        else:
            u.is_staff = True
        u.save()
    return redirect('/accounts/create-new-user/')
