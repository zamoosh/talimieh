from django.contrib import admin
from .models import *


class EducationalRequestAdmin(admin.ModelAdmin):
    list_display = ['average', 'field_study', 'former_university', 'college', 'status', 'sent']


admin.site.register(EducationalRequest, EducationalRequestAdmin)
