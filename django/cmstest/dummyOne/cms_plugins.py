from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import CodeArea
from codemirror.admin import CodeMirrorAdmin
import json
from itertools import chain
from django.utils.safestring import mark_safe

from codemirror.widgets import CODEMIRROR_PATH, CODEMIRROR_THEME,\
     THEME_CSS_FILENAME_RE, CODEMIRROR_CONFIG, CODEMIRROR_MODE

js = (
    "/static/%s/lib/codemirror.js" % CODEMIRROR_PATH,
    "/static/%s/mode/%s/%s.js" % (CODEMIRROR_PATH, CODEMIRROR_MODE, CODEMIRROR_MODE),
)

theme = CODEMIRROR_THEME
theme_css_filename = THEME_CSS_FILENAME_RE.search(theme).group(0)
if theme_css_filename == 'default':
    theme_css = []
else:
    theme_css = [theme_css_filename]

css = (("/static/%s/lib/codemirror.css" % CODEMIRROR_PATH,) +
        tuple("/static/%s/theme/%s.css" % (CODEMIRROR_PATH, theme_css_filename)
                        for theme_css_filename in theme_css))

options_json = json.dumps(dict(chain(
    CODEMIRROR_CONFIG.items(),
    [('mode', CODEMIRROR_MODE),
     ('theme', CODEMIRROR_THEME),
     ('readOnly', True),
     ])))


class CMSCodeAreaPlugin(CMSPluginBase, CodeMirrorAdmin):
    model = CodeArea
    name = "Codearea"
    render_template = "codearea.html"

    def render(self, context, instance, placeholder):
        media = {}
        media['js'] = js
        media['css'] = css
        media['opjson'] = mark_safe(options_json)
        context.update({
            'object': instance,
            'placeholder': placeholder,
            'media': media,
        })
        return context

plugin_pool.register_plugin(CMSCodeAreaPlugin)

