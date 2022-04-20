from .imports import *


@register.filter(name='can_reject')
def can_reject(r):
    if int(r.step[1]) < 6 and r.reject is False:
        return True
    return False


@register.filter(name='get_request_remaining_coast')
def get_request_remaining_coast(r):
    total_coast = 0
    total_coast += get_request_total_coast(r, True) - get_request_current_paid(r, True)
    if total_coast == 0:
        return 'تمامی هزینه‌ها پرداخت شده‌اند'
    return f'{total_coast}  تومان'


@register.filter(name='get_request_total_coast')
def get_request_total_coast(r, num=False):
    total_coast = 0
    if r.selectedoption_set.all().exists():
        for select_option in r.selectedoption_set.all():
            total_coast += int(select_option.option.price)
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.expert_price)
        total_coast += int(sem.semester.entrance_price)
    if num:
        return total_coast
    return f'{total_coast}  تومان'


@register.filter(name='get_request_current_paid')
def get_request_current_paid(r, num=False):
    total_coast = 0
    if int(r.step[1]) > 3:
        total_coast += get_request_expert_coast(r, True)
    if int(r.step[1]) > 5:
        total_coast += get_request_entrance_coast(r, True)
    if request_has_option(r):
        total_coast += get_request_options_coast(r, True)
    if num:
        return total_coast
    return f'{total_coast}  تومان'


@register.filter(name='get_request_expert_coast')
def get_request_expert_coast(r, num=False):
    total_coast = 0
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.expert_price)
    if num:
        return total_coast
    return f'{total_coast}  تومان'


@register.filter(name='get_request_entrance_coast')
def get_request_entrance_coast(r, num=False):
    total_coast = 0
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.entrance_price)
    if num:
        return total_coast
    return f'{total_coast}  تومان'


@register.filter(name='request_has_option')
def request_has_option(r):
    if r.selectedoption_set.all().exists():
        return True
    return False


@register.filter(name='get_request_options_coast')
def get_request_options_coast(r, num=False):
    total_coast = 0
    if r.selectedoption_set.all().exists():
        for select_option in r.selectedoption_set.all():
            total_coast += int(select_option.option.price)
    if num:
        return total_coast
    return f'{total_coast}  تومان'


# for single semester selection
@register.filter(name='get_request_uni')
def get_request_uni(r):
    if r == '':
        return ''
    if r.selectedsemester_set.all().exists():
        return r.selectedsemester_set.all()[0].semester.university
    return 'ندارد'


# for single semester selection
@register.filter(name='get_request_entrance')
def get_request_entrance(r):
    if r == '':
        return ''
    if r.selectedsemester_set.all().exists():
        return f'{r.selectedsemester_set.all()[0].semester.entrance_price} تومان'
    return '0 تومان'


# for single semester selection
@register.filter(name='get_request_expert')
def get_request_expert(r):
    if r == '':
        return ''
    if r.selectedsemester_set.all().exists():
        return f'{r.selectedsemester_set.all()[0].semester.expert_price} تومان'
    return '0 تومان'


# for single semester selection
@register.filter(name='get_request_section')
def get_request_section(r):
    if r == '':
        return ''
    if r.selectedsemester_set.all().exists():
        return r.selectedsemester_set.all()[0].semester.degree_field_study.parent
    return 'ندارد'


# for single semester selection
@register.filter(name='get_request_degree_field_study')
def get_request_degree_field_study(r):
    if r == '':
        return ''
    if r.selectedsemester_set.all().exists():
        return r.selectedsemester_set.all()[0].semester.degree_field_study
    return 'ندارد'


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
