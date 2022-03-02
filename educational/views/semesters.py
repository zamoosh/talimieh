from django.db.models import Q

from .imports import *
from educational.models import *


def semesters(request):
    context = {}
    context['semesters'] = Semester.objects.filter(status=True).values_list('university', flat=True).distinct()
    context['uni_semesters'] = Universities.objects.filter(id__in=context['semesters'])
    return render(request, 'educational/semesters.html', context)


def new_semester(request):
    context = {}
    context['degree_fields'] = DegreeFieldStudy.objects.filter(status=True)
    if request.method == 'POST':
        context['request'] = {}
        context['request']['uni'] = request.POST.get('uni', '').strip()
        context['request']['degree_list'] = request.POST.getlist('degree_list')
        request.session['degrees'] = context['request']
        return HttpResponseRedirect(reverse('educational:submit_semester'))
    return render(request, 'educational/new_semester.html', context)


def submit_semester(request):
    context = {}
    if 'degrees' in request.session:
        context = request.session['degrees']
        context['degree_list'] = context['degree_list']
        context['uni'] = context['uni']
        context['university'] = Universities.objects.get(id=context['uni'])
        context['degree_fields'] = DegreeFieldStudy.objects.filter(id__in=context['degree_list'])
        context['year'] = YearSemester.objects.get(yearsemester__status=True)
        context['term'] = YearSemester.objects.get(parent=context['year'], status=True)
        if request.method == "POST":
            detail = {}
            for i in request.POST.items():
                if 'entrance_price_' in i[0]:
                    if i[0][len('entrance_price_'):] not in detail:
                        detail[i[0][len('entrance_price_'):]] = {}
                    if 'scholarship' not in detail[i[0][len('entrance_price_'):]]:
                        detail[i[0][len('entrance_price_'):]]['scholarship'] = False
                    detail[i[0][len('entrance_price_'):]]['entrance_price'] = i[1]
                if 'scholarship_' in i[0]:
                    if i[0][len('scholarship_'):] not in detail:
                        detail[i[0][len('scholarship_'):]] = {}
                    detail[i[0][len('scholarship_'):]]['scholarship'] = True
                if 'expert_price_' in i[0]:
                    if i[0][len('expert_price_'):] not in detail:
                        detail[i[0][len('expert_price_'):]] = {}
                    if 'scholarship' not in detail[i[0][len('expert_price_'):]]:
                        detail[i[0][len('expert_price_'):]]['scholarship'] = False
                    detail[i[0][len('expert_price_'):]]['expert_price'] = i[1]
            for i in context['degree_fields']:
                if str(i.id) in detail:
                    if i.semester_set.filter(~Q(university=None)):
                        for item in i.semester_set.filter(~Q(university=None)):
                            if item.university.id == context['uni']:
                                item.expert_price = detail[str(i.id)]['expert_price']
                                item.entrance_price = detail[str(i.id)]['entrance_price']
                                item.scholarship = detail[str(i.id)]['scholarship']
                                item.save()
                            else:
                                uni = Universities.objects.get(id=context['uni'])
                                semester = Semester()
                                semester.university_id = context['university'].id
                                semester.degree_field_study_id = i.id
                                semester.year_semester_id = context['term'].id
                                semester.status = True
                                semester.expert_price = detail[str(i.id)]['expert_price']
                                semester.entrance_price = detail[str(i.id)]['entrance_price']
                                semester.scholarship = detail[str(i.id)]['scholarship']
                                semester.university.status = True
                                uni.status = True
                                uni.save()
                                semester.save()
                    else:
                        uni = Universities.objects.get(id=context['uni'])
                        semester = Semester()
                        semester.university_id = context['university'].id
                        semester.degree_field_study_id = i.id
                        semester.year_semester_id = context['term'].id
                        semester.status = True
                        semester.expert_price = detail[str(i.id)]['expert_price']
                        semester.entrance_price = detail[str(i.id)]['entrance_price']
                        semester.scholarship = detail[str(i.id)]['scholarship']
                        semester.university.status = True
                        uni.status = True
                        uni.save()
                        semester.save()
            return HttpResponseRedirect(reverse('educational:semesters'))
    return render(request, 'educational/submit_semester.html', context)
