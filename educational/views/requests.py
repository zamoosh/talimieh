from .imports import *


def requests(request):
    context = {}
    if request.user.is_superuser:
        context['requests'] = EducationalRequest.objects.all()
    else:
        if request.user.groups.filter(name__contains='ثبت‌نام'):
            context['requests'] = EducationalRequest.objects.filter(step__contains='1')
        elif request.user.groups.filter(name__contains='مالی'):
            context['requests'] = EducationalRequest.objects.filter(Q(financial_status=False) & Q(step__contains='2'))
        elif request.user.groups.filter(name__contains='آموزشی'):
            context['requests'] = EducationalRequest.objects.filter(step__contains='3')
    return render(request, 'educational/requests.html', context)
