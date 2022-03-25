from .imports import *


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
            )
        elif request.user.user_permissions.filter(name__icontains='financial'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) &
                ((Q(financial_status=False) & Q(register_status=True)) | Q(financial_status=True))
            )
        elif request.user.user_permissions.filter(name__icontains='educational'):
            context['requests'] = EducationalRequest.objects.filter(
                Q(reject=False) &
                (
                        (Q(educational_status=False) &
                         Q(financial_status=True) &
                         Q(register_status=True)) | Q(educational_status=True)
                )
            )
    return render(request, 'educational/requests.html', context)
