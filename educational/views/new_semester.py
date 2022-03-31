from .imports import *


def new_semester(request):
    if not (request.user.user_permissions.filter(name__contains='see') or request.user.is_superuser):
        return render(request, '404_page.html')
    context = {'degree_fields': DegreeFieldStudy.objects.filter(status=True)}
    if request.method == 'POST':
        context['request'] = {}
        context['request']['uni'] = request.POST.get('uni', '').strip()
        context['request']['degree_list'] = request.POST.getlist('degree_list')
        request.session['degrees'] = context['request']
        return HttpResponseRedirect(reverse('educational:submit_semester'))
    return render(request, 'educational/new_semester.html', context)
