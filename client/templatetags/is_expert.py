from django import template

register = template.Library()


@register.filter(name='is_expert')
def has_group(user):
    return user.user_permissions.filter(name__contains='see').exists()
