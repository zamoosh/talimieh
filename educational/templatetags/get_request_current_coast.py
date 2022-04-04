from .imports import *

register = template.Library()


@register.filter(name='get_request_current_coast')
def get_request_current_coast(r):
    total_coast = 0
    for sem in r.selectedsemester_set.all():
        total_coast += int(sem.semester.expert_price)
        total_coast += int(sem.semester.entrance_price)
    return total_coast
