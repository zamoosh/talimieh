from educational.models import *
from .imports import *


@login_required()
def dashboard(request):
    context = {}
    u = User.objects.get(id=request.user.id)
    context['my_request_num'] = u.educationalrequest_set.all().__len__()
    if u.is_superuser or u.user_permissions.filter(name__icontains='see'):
        context['request_num'] = EducationalRequest.objects.all().__len__()
    if u.educationalrequest_set.all():
        context['alert_requests'] = u.educationalrequest_set.filter(Q(step__icontains='4') | Q(step__icontains='5') |
                                                                    Q(step__icontains='6') | Q(step__icontains='7'))
        context['my_reject_requests_num'] = u.educationalrequest_set.filter(reject=True).__len__()
        if u.educationalrequest_set.filter(final_status=True):
            context['confirmed_request'] = u.educationalrequest_set.filter(final_status=True)
            context['confirmed_request_num'] = u.educationalrequest_set.filter(final_status=True).__len__()
    context['registered'] = len(User.objects.filter(is_active=True, is_staff=False))
    context['year'] = YearSemester.objects.last()
    context['uni'] = len(Universities.objects.filter(status=True))
    return render(request, 'client/dashboard.html', context)
