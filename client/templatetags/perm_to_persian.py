from django import template

register = template.Library()


@register.filter(name='perm_to_persian')
def perm_to_persian(perm):
    if 'can see educational request' in perm.name:
        return 'کارشناس آموزشی'
    elif 'can see financial request' in perm.name:
        return 'کارشناس مالی'
    elif 'can see register request' in perm.name:
        return 'کارشناس ثبت‌نام'
    elif 'can set expert' in perm.name:
        return 'مدیریت کارشناسان'
