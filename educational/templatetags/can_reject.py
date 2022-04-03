from django import template
from educational.models import EducationalRequest

register = template.Library()


@register.filter(name='can_reject')
def can_reject(request: EducationalRequest):
    if int(request.step[1]) < 4 and request.reject is False:
        return True
    return False
