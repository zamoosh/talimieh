from .imports import *


def reports(request):
    context = {'request_number': 0}
    if EducationalRequest.objects.all().exists():
        context = {}
        context['request_number'] = len(EducationalRequest.objects.all())
        context['accepted'] = len(EducationalRequest.objects.filter(status=True))
        context['rejected'] = len(EducationalRequest.objects.filter(status=False))
    return render(request, 'educational/reports.html', context=context)
