from educational.models import YearSemester
from django.http import JsonResponse
from django import template
from educational.models import *
import json

register = template.Library()
