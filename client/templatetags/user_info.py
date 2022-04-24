from django import template

register = template.Library()


@register.filter(name='is_student')
def is_student(user):
    if user.educationalrequest_set.filter(step__icontains='7'):
        return True
    return False


@register.filter(name='get_whatsapp_number')
def get_whatsapp_number(user):
    wh_number = user.whatsapp
    if len(wh_number) < 10:
        return wh_number
    while len(wh_number) != 10:
        wh_number = wh_number.replace(wh_number[0], '', 1)
    return wh_number


@register.filter(name='whatsapp_contains')
def whatsapp_contains(wh_number, pre_code):
    if not wh_number:
        return ''
    if pre_code in wh_number:
        return True
    return False
