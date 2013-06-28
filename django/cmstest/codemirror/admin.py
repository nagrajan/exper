# -*- coding: utf-8 -*-

from django.contrib import admin
from django.db import models
from codemirror.widgets import CodeMirrorTextarea

class CodeMirrorAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CodeMirrorTextarea},
    }