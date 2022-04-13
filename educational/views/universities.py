from .imports import *


def universities(request):
    context = {'universities': Universities.objects.filter(status=True).order_by('-id')}
    if request.method == "POST":
        context['req'] = {}
        context['req']['university'] = request.POST.get('university', '').strip()
        context['req']['uni_comment'] = request.POST.get('uni_comment', '').strip()
        context['req']['uni_doc'] = request.POST.get('uni_doc', '').strip()
        university = Universities()
        if Universities.objects.filter(uni_name=context['req']['university'], status=True).exists():
            context['error'] = True
        else:
            university.uni_name = context['req']['university']
            university.document = context['req']['uni_doc']
            university.comment = context['req']['uni_comment']
            university.status = True
            university.save()
            context['create'] = True
    if 'remove' in request.GET:
        try:
            # u = Universities.objects.get(id=request.GET.get('remove'))
            # u.status = False
            # u.save()
            u = Universities.objects.get(id=Universities.objects.get(id=int(request.GET.get('remove'))))
            u.delete()
            context['remove'] = True
        except (Universities.DoesNotExist, Exception):
            return render(request, 'educational/universities.html', context)
    return render(request, 'educational/universities.html', context)
