from django.contrib.auth.models import Permission
from django.db.models import Q


def is_normal(request):
    p = Permission.objects.filter(Q(name__contains='see') | Q(name__contains='set expert'))
    if not (request.user.is_superuser or request.user.has_perms(p)):
        return True


def is_register_expert(request):
    p = Permission.objects.filter(name__contains='see register request')
    return request.user.has_perms(p)


def is_educational_expert(request):
    p = Permission.objects.filter(name__contains='see educational request')
    return request.user.has_perms(p)


def is_financial_expert(request):
    p = Permission.objects.filter(name__contains='see financial request')
    return request.user.has_perms(p)
