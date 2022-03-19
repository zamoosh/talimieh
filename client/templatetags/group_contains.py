from django import template

register = template.Library()


@register.filter(name='groups_contains')
def group_contains(user, group):
    return user.groups.filter(name__contains=group).exists()
