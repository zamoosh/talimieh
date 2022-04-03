import educational.models
from django import template

register = template.Library()


@register.filter(name='get_semester_entrance_price')
def get_semester_entrance_price(uni: educational.models.Universities, degree_field_study):
    if uni.semester_set.filter(degree_field_study=degree_field_study):
        sem = uni.semester_set.get(degree_field_study=degree_field_study)
        return sem.entrance_price
    return ''


@register.filter(name='get_semester_expert_price')
def get_semester_expert_price(uni: educational.models.Universities, degree_field_study):
    if uni.semester_set.filter(degree_field_study=degree_field_study):
        sem = uni.semester_set.get(degree_field_study=degree_field_study)
        return sem.expert_price
    return ''


@register.filter(name='has_scholarship')
def has_scholarship(uni: educational.models.Universities, degree_field_study):
    if uni.semester_set.filter(degree_field_study=degree_field_study):
        sem = uni.semester_set.get(degree_field_study=degree_field_study)
        return sem.scholarship
    return ''
