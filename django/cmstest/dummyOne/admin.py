from django.contrib import admin
from codemirror2.admin import CodeMirrorAdmin
from dummyOne.models import CodeArea

class CodeAreaAdmin(CodeMirrorAdmin):
    pass

admin.site.register(CodeArea, CodeAreaAdmin)
