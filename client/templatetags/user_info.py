from django import template

register = template.Library()


@register.filter(name='is_student')
def is_student(user):
    if user.educationalrequest_set.filter(step__icontains='7'):
        return True
    return False


@register.filter(name='get_whatsapp_number')
def get_whatsapp_number(user):
    return user.whatsapp[:-11:-1][::-1]


@register.filter(name='whatsapp_contains')
def whatsapp_contains(wh_number, pre_code):
    if not wh_number:
        return ''
    if pre_code in wh_number:
        return True
    return False
