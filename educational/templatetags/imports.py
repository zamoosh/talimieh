from educational.models import YearSemester
from django.http import JsonResponse
from django import template
from educational.models import Universities
import json

register = template.Library()
