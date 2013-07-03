from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.safestring import mark_safe

from djcodemirror.widgets import cm_css_files, cm_js_files, cm_option_json, cm_option_json_ro

class CMSCodeRunnerPlugin(CMSPluginBase):
    name = "Coderunner"
    render_template = "coderunner.html"

    def render(self, context, instance, placeholder):
        media = {}
        media['js'] = cm_js_files
        media['css'] = cm_css_files
        media['opjson'] = mark_safe(cm_option_json)
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'media': media,
        })
        return context

plugin_pool.register_plugin(CMSCodeRunnerPlugin)
