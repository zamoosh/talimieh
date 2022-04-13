from django import template

register = template.Library()


@register.filter(name='is_student')
def is_student(user):
    if user.educationalrequest_set.filter(step__icontains='7'):
        return True
    return False
