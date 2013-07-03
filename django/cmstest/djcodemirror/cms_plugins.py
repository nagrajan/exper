from .models import CodeArea
from .admin import CodeAreaAdmin
from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.safestring import mark_safe

from .widgets import cm_css_files, cm_js_files, cm_option_json_ro

class CMSCodeAreaPlugin(CMSPluginBase, CodeAreaAdmin):
    model = CodeArea
    name = "Codearea"
    render_template = "codearea.html"

    def render(self, context, instance, placeholder):
        media = {}
        media['js'] = cm_js_files
        media['css'] = cm_css_files
        media['opjson'] = mark_safe(cm_option_json_ro)
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'media': media,
        })
        return context

plugin_pool.register_plugin(CMSCodeAreaPlugin)
