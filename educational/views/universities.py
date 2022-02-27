from .imports import *
from client.models import *


def universities(request):
    context = {}
    context['universitys'] = Universities.objects.filter(status=True).order_by('-id')
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
            university.save()
            context['create'] = True
    if 'remove' in request.GET:
        try:
            u = Universities.objects.get(id=Universities.objects.get(id=int(request.GET.get('remove'))))
            u.delete()
            context['remove'] = True
        except (Universities.DoesNotExist, Exception):
            return render(request, 'educational/universities.html', context)
        # context['rmuniversity'] = Universities.objects.get(id=int(request.GET.get('remove')))
        # context['rmuniversity'].status = 0
        # context['rmuniversity'].save()
        # context['remove'] = True
    return render(request, 'educational/universities.html', context)
