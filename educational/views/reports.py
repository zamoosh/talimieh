from .imports import *


def reports(request):
    if EducationalRequest.objects.all().exists():
        context = {'request_number': len(EducationalRequest.objects.all())}
    context = {'request_number': 0}
    return render(request, 'educational/reports.html', context=context)
