from .imports import *


@login_required()
def degree_field_study(request):
    context = {}
    context['degree_field_studys'] = DegreeFieldStudy.objects.filter(status=True).order_by('-id')
    if request.session.get('section_exists'):
        context['section_exists'] = True
        del request.session['section_exists']
    if request.method == "POST":
        if not (DegreeFieldStudy.objects.filter(parent__isnull=True).exists()):
            context['degree_error'] = True
            return redirect(reverse('educational:degree_field_study', args=context))
        context['req'] = {}
        context['req']['title'] = request.POST.get('title', '').strip()
        context['req']['doc'] = request.POST.get('doc', '').strip()
        if DegreeFieldStudy.objects.filter(title=context['req']['title']):
            context['degree_exists'] = True
        else:
            degree = DegreeFieldStudy()
            degree.title = context['req']['title']
            degree.document = context['req']['doc']
            degree.status = True
            degree.parent = DegreeFieldStudy.objects.get(id=request.POST.get('section'))
            degree.save()
    if 'remove' in request.GET:
        context['rmYear'] = DegreeFieldStudy.objects.get(id=int(request.GET.get('remove')))
        context['rmYear'].status = 0
        context['rmYear'].save()
        context['remove'] = True
    return render(request, 'educational/degree_field_study.html', context)
