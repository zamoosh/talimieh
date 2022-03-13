from django.contrib import admin
from .models import *


class EducationalRequestAdmin(admin.ModelAdmin):
    list_display = ['average', 'former_field_study', 'former_university', 'selected_semester', 'status', 'sent']


class OwnerDocumentAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'image', 'id']


admin.site.register(EducationalRequest, EducationalRequestAdmin)
admin.site.register(OwnerDocument, OwnerDocumentAdmin)
