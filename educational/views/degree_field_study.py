from .imports import *


@login_required()
def degree_field_study(request):
    context = {}
    context['degree_field_studys'] = DegreeFieldStudy.objects.filter(status=True).order_by('-id')
    if request.method == "POST":
        context['req'] = {}
        context['req']['title'] = request.POST.get('title', '').strip()
        context['req']['doc'] = request.POST.get('doc', '').strip()
        degree_field_study = DegreeFieldStudy()
        degree_field_study.title = context['req']['title']
        degree_field_study.document = context['req']['doc']
        degree_field_study.status = True
        degree_field_study.parent = DegreeFieldStudy.objects.get(id=request.POST.get('section'))
        degree_field_study.save()
    if 'remove' in request.GET:
        context['rmYear'] = DegreeFieldStudy.objects.get(id=int(request.GET.get('remove')))
        context['rmYear'].status = 0
        context['rmYear'].save()
        context['remove'] = True
    return render(request, 'educational/degree_field_study.html', context)
