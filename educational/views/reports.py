from .imports import *


def reports(request):
    context = {'request_number': len(Educational_request.objects.all())}
    return render(request, 'educational/reports.html', context=context)
