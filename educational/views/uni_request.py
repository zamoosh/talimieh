from .imports import *


@login_required
def uni_request(request):
    context = {'educational_request': EducationalRequest.objects.all()}
    if request.method == 'POST':
        context['request'] = {}
        context['request']['moadel'] = request.POST.get('moadel', '').strip()
        context['request']['reshte'] = request.POST.get('reshte', '').strip()
        context['request']['old_uni'] = request.POST.get('old_uni', '').strip()
        context['request']['collage'] = request.POST.get('collage', '').strip()
        context['request']['study'] = request.POST.get('study', '').strip()
        context['request']['degree'] = request.POST.get('degree', '').strip()
        request.session['e_request'] = context['request']
        return HttpResponseRedirect(reverse('educational:uni_request_submit'))
    return render(request, 'educational/uni_request.html', context)


@login_required
def uni_request_submit(request):
    context = {}
    if 'e_request' in request.session:
        context = request.session['e_request']
        context['uni_dic'] = Universities.objects.get(id=context['collage']).document
    # context['unis'] = Universities.objects.filter(semester__in=Semester.objects.all())
    context['semesters'] = Semester.objects.filter(status=True)
    return render(request, 'educational/uni_request_submit.html', context)
