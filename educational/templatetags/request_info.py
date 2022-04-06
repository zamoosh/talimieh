from .imports import *


@register.filter(name='can_reject')
def can_reject(r):
    if int(r.step[1]) < 6 and r.reject is False:
        return True
    return False


@register.filter(name='get_request_current_coast')
def get_request_current_coast(r):
    total_coast = 0
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.expert_price)
        total_coast += int(sem.semester.entrance_price)
    return f'{total_coast} هزار تومان'


# for single semester selection
@register.filter(name='get_request_uni')
def get_request_uni(r):
    return r.selectedsemester_set.all()[0].semester.university


# for single semester selection
@register.filter(name='get_request_section')
def get_request_section(r):
    return r.selectedsemester_set.all()[0].semester.degree_field_study.parent


# for single semester selection
@register.filter(name='get_request_degree_field_study')
def get_request_degree_field_study(r):
    return r.selectedsemester_set.all()[0].semester.degree_field_study


