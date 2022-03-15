from django import template
from educational.models import EducationalRequest

register = template.Library()


@register.simple_tag
def have_educational_request():
    if EducationalRequest.objects.all().exists():
        return True
    return False
