from .imports import *


@login_required
def requests(request):
    context = {}
    context['reject_requests'] = EducationalRequest.objects.filter(reject=True)
    if request.user.is_superuser:
        context['requests'] = EducationalRequest.objects.filter(reject=False)
        return render(request, 'educational/requests.html', context)
    else:
        if request.user.user_permissions.filter(name__icontains='register'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) &
                (Q(register_status=False) | Q(register_status=True))
            ).order_by('-id')
        if request.user.user_permissions.filter(name__icontains='educational'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) &
                (
                        (Q(educational_status=False) &
                         Q(register_status=True)) | Q(educational_status=True)
                )
            ).order_by('-id')
        if request.user.user_permissions.filter(name__icontains='financial'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) &
                (
                        (Q(financial_status=False) &
                         Q(educational_status=True) &
                         Q(register_status=True)) | Q(financial_status=True)
                )
            ).order_by('-id')
        if request.user.user_permissions.filter(name__icontains='normal'):
            context['requests'] = EducationalRequest.objects.filter(user=request.user).order_by('-id')
            context['reject_requests'] = EducationalRequest.objects.filter(reject=True, user=request.user)
    return render(request, 'educational/requests.html', context)
