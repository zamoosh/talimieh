from .imports import *


def create_degree_section(request):
    if request.method == 'POST':
        title = request.POST.get('section').strip()
        if DegreeFieldStudy.objects.filter(title=title):
            request.session['section_exists'] = True
        else:
            section = DegreeFieldStudy.objects.create(title=title)
            section.save()
    return redirect(reverse('educational:degree_field_study'))
