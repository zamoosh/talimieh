from .imports import *


def reports(request):
    context = {'request_number': len(EducationalRequest.objects.all())}
    return render(request, 'educational/reports.html', context=context)
