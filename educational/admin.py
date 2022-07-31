from django.contrib import admin
from .models import *


class EducationalRequestAdmin(admin.ModelAdmin):
    list_display = ['average', 'former_field_study', 'former_university', 'paid']


class OwnerDocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'file', 'id']


admin.site.register(EducationalRequest, EducationalRequestAdmin)
admin.site.register(OwnerDocument, OwnerDocumentAdmin)
