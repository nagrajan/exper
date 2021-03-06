# -*- coding: utf-8 -*-
#
# Created:    2010/09/09
# Author:         alisue
#
import json, re
from itertools import chain
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

# set default settings
CODEMIRROR_PATH = getattr(settings, 'CODEMIRROR_PATH', 'codemirror')
if CODEMIRROR_PATH.endswith('/'):
    CODEMIRROR_PATH = CODEMIRROR_PATH[:-1]
CODEMIRROR_MODE = getattr(settings, 'CODEMIRROR_MODE', 'python')
CODEMIRROR_THEME = getattr(settings, 'CODEMIRROR_THEME', 'default')
CODEMIRROR_CONFIG = getattr(settings, 'CODEMIRROR_CONFIG',
                            {'lineNumbers': True,
                             'indentUnit':4,
                             'lineWrapping':True,
                             })

THEME_CSS_FILENAME_RE = re.compile(r'[\w-]+')

cm_js_files = (
    "/static/%s/lib/codemirror.js" % CODEMIRROR_PATH,
    "/static/%s/mode/%s/%s.js" % (CODEMIRROR_PATH, CODEMIRROR_MODE, CODEMIRROR_MODE),
)

theme = CODEMIRROR_THEME
theme_css_filename = THEME_CSS_FILENAME_RE.search(theme).group(0)
if theme_css_filename == 'default':
    theme_css = []
else:
    theme_css = [theme_css_filename]

cm_css_files = (("/static/%s/lib/codemirror.css" % CODEMIRROR_PATH,) +
        tuple("/static/%s/theme/%s.css" % (CODEMIRROR_PATH, theme_css_filename)
                        for theme_css_filename in theme_css))

option_dict = dict(chain(
            CODEMIRROR_CONFIG.items(),
            [('mode', CODEMIRROR_MODE), ('theme', CODEMIRROR_THEME)]))

cm_option_json = json.dumps(option_dict)
cm_option_json_ro = json.dumps(dict(chain(
            option_dict.items(), [('readOnly', True),])))

class CodeMirrorTextarea(forms.Textarea):
    u"""Textarea widget render with `CodeMirror`

    CodeMirror:
        http://codemirror.net/
    """

    @property
    def media(self):
        return forms.Media(css = {
                'all': cm_css_files,
            },
            js = cm_js_files,)

    def __init__(self, attrs=None, mode=None, theme=None, config=None, **kwargs):
        u"""Constructor of CodeMirrorTextarea

        Attribute:
            path          - CodeMirror directory URI (DEFAULT = settings.CODEMIRROR_PATH)
            mode          - Name of language or a modal configuration object as described in CodeMirror docs.
                            Used to autoload an appropriate language plugin js file according to filename conventions.
                            (DEFAULT = settings.CODEMIRROR_MODE)
            theme         - Name of theme. Also autoloads theme plugin css according to filename conventions.
                            (DEFAULT = settings.CODEMIRROR_THEME)
            config        - The rest of the options passed into CodeMirror as a python map.
                            (updated from settings.CODEMIRROR_CONFIG)

        Example:
            *-------------------------------*
            + static
              + codemirror
                + lib
                  - codemirror.js
                  - codemirror.css
                + mode
                  + python
                    - python.js
                + theme
                  + cobalt.css
            *-------------------------------*
            CODEMIRROR_PATH = "codemirror"

            codemirror = CodeMirrorTextarea(mode="python", theme="cobalt", config={ 'fixedGutter': True })
            document = forms.TextField(widget=codemirror)
        """
        super(CodeMirrorTextarea, self).__init__(attrs=attrs, **kwargs)

    def render(self, name, value, attrs=None):
        u"""Render CodeMirrorTextarea"""
        output = [super(CodeMirrorTextarea, self).render(name, value, attrs),
            '<script type="text/javascript">CodeMirror.fromTextArea(document.getElementById(%s), %s);</script>' %
                ('"id_%s"' % name, cm_option_json)]
        return mark_safe('\n'.join(output))

