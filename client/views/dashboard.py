from educational.models import *
from .imports import *


@login_required()
def dashboard(request):
    context = {
        'registered': len(User.objects.filter(is_active=True, is_staff=False)),
        'year': YearSemester.objects.last(),
        'uni': len(Universities.objects.filter(status=True))
    }
    return render(request, 'client/dashboard.html', context)
