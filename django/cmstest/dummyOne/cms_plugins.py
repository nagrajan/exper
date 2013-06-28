from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import CodeArea
from codemirror2.admin import CodeMirrorAdmin

class CMSCodeAreaPlugin(CMSPluginBase, CodeMirrorAdmin):
    model = CodeArea
    name = "Codearea"

plugin_pool.register_plugin(CMSCodeAreaPlugin)

