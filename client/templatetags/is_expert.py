from django import template

register = template.Library()


@register.filter(name='is_expert')
def has_group(user):
    return user.groups.filter(name__contains='کارشناس').exists()
