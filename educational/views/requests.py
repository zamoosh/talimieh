from .imports import *


@login_required
def requests(request):
    context = {}
    if request.session.get('message'):
        del request.session['message']
        context['message'] = True
    context['reject_requests'] = EducationalRequest.objects.filter(reject=True)
    if request.user.is_superuser:
        context['requests'] = EducationalRequest.objects.filter(reject=False)
        return render(request, 'educational/requests.html', context)
    else:
        if request.user.user_permissions.filter(name__icontains='register'):
            context['requests'] = EducationalRequest.objects.filter(reject=False)
        if request.user.user_permissions.filter(name__icontains='educational'):
            context['requests'] = EducationalRequest.objects.filter(Q(reject=False) & ~Q(step__contains='1'))
        if request.user.user_permissions.filter(name__icontains='financial'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) & ~Q(step__icontains='1') & ~Q(step__icontains='2'))
        if request.user.user_permissions.filter(name__icontains='normal'):
            context['requests'] = EducationalRequest.objects.filter(user=request.user, reject=False)
            context['reject_requests'] = EducationalRequest.objects.filter(reject=True, user=request.user)
            context['person_con'] = True
    return render(request, 'educational/requests.html', context)
