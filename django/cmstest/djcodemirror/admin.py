from django.contrib import admin
from django.db import models
from .widgets import CodeMirrorTextarea
from .models import CodeArea

class CodeAreaAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CodeMirrorTextarea},
    }

admin.site.register(CodeArea, CodeAreaAdmin)
