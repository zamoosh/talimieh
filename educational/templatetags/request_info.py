from .imports import *


@register.filter(name='can_reject')
def can_reject(r):
    if int(r.step[1]) < 6 and r.reject is False:
        return True
    return False


@register.filter(name='get_request_current_coast')
def get_request_current_coast(r):
    total_coast = 0
    if r.selectedoption_set.all().exists():
        for s_o in r.selectedoption_set.all():
            total_coast += int(s_o.option.price)
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.expert_price)
        total_coast += int(sem.semester.entrance_price)
    return f'{total_coast}  تومان'


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


@register.filter(name='has_option')
def has_option(r, o):
    if len(r.selectedoption_set.filter(option=o)) == 1:
        return True
    return False


@register.filter(name='has_register_confirm')
def has_register_confirm(r):
    if int(r.step[1]) > 1:
        return True
    return False


@register.filter(name='has_educational_confirm_1')
def has_educational_confirm_1(r):
    if int(r.step[1]) > 2:
        return True
    return False


@register.filter(name='has_financial_confirm_1')
def has_financial_confirm_1(r):
    if int(r.step[1]) > 3:
        return True
    return False


@register.filter(name='has_educational_confirm_2')
def has_educational_confirm_2(r):
    if int(r.step[1]) > 4:
        return True
    return False


@register.filter(name='has_financial_confirm_2')
def has_financial_confirm_2(r):
    if int(r.step[1]) > 5:
        return True
    return False


@register.filter(name='has_educational_confirm_3')
def has_educational_confirm_3(r):
    if int(r.step[1]) > 6:
        return True
    return False
