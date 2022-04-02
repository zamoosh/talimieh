from .imports import *


def create_degree_section(request):
    if request.method == 'POST':
        section = DegreeFieldStudy.objects.create(title=request.POST.get('section'))
        section.save()
    return redirect(reverse('educational:degree_field_study'))
