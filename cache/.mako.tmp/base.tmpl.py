# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1531805869.8837252
_enable_loop = True
_template_filename = 'themes/maupassant/templates/base.tmpl'
_template_uri = 'base.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'sourcelink', 'extra_js']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('base', context._clean_inheritance_tokens(), templateuri='base_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'base')] = ns

    ns = runtime.TemplateNamespace('notes', context._clean_inheritance_tokens(), templateuri='annotation_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'notes')] = ns

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        set_locale = _import_ns.get('set_locale', context.get('set_locale', UNDEFINED))
        notes = _mako_get_namespace(context, 'notes')
        def extra_js():
            return render_extra_js(context._locals(__M_locals))
        def sourcelink():
            return render_sourcelink(context._locals(__M_locals))
        momentjs_locales = _import_ns.get('momentjs_locales', context.get('momentjs_locales', UNDEFINED))
        blog_url = _import_ns.get('blog_url', context.get('blog_url', UNDEFINED))
        template_hooks = _import_ns.get('template_hooks', context.get('template_hooks', UNDEFINED))
        annotations = _import_ns.get('annotations', context.get('annotations', UNDEFINED))
        logo_url = _import_ns.get('logo_url', context.get('logo_url', UNDEFINED))
        search_form = _import_ns.get('search_form', context.get('search_form', UNDEFINED))
        blog_title = _import_ns.get('blog_title', context.get('blog_title', UNDEFINED))
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        lang = _import_ns.get('lang', context.get('lang', UNDEFINED))
        js_date_format = _import_ns.get('js_date_format', context.get('js_date_format', UNDEFINED))
        base = _mako_get_namespace(context, 'base')
        content_footer = _import_ns.get('content_footer', context.get('content_footer', UNDEFINED))
        date_fanciness = _import_ns.get('date_fanciness', context.get('date_fanciness', UNDEFINED))
        body_end = _import_ns.get('body_end', context.get('body_end', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer(str(set_locale(lang)))
        __M_writer('\n')
        __M_writer(str(base.html_headstart()))
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n')
        __M_writer(str(template_hooks['extra_head']()))
        __M_writer('\n</head>\n<body>\n<div class="body_container">\n    <div id="header">\n        <div class="site-name">\n')
        if logo_url:
            __M_writer('            <a id="logo" href="')
            __M_writer(str(blog_url))
            __M_writer('"><img src="')
            __M_writer(str(logo_url))
            __M_writer('" alt="')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('"></a>\n')
        else:
            __M_writer('                <h1>')
            __M_writer(filters.html_escape(str(blog_title)))
            __M_writer('</h1>\n')
        __M_writer('        </div>\n\n        <div id="nav-menu">\n            <div class="bitcron_nav_container">\n                <div class="bitcron_nav">\n                    <div class="site_nav_wrap">\n                        <ul class="site_nav sm sm-base">\n                            ')
        __M_writer(str(base.html_navigation_links()))
        __M_writer('\n                            ')
        __M_writer(str(template_hooks['menu']()))
        __M_writer('\n                        </ul>\n                        <div class="clear clear_nav_inline_end"></div>\n                    </div>\n                </div>\n                <div class="clear clear_nav_end"></div>\n            </div>\n        </div>\n    </div>\n    <div id="layout">\n        <div class="pure-g">\n            <div class=" pure-u-24-24 pure-u-sm-24-24 pure-u-md-18-24 pure_cell">\n                <div class="content_container">\n                    <!--Body content-->\n                    <div class="row">\n                        ')
        __M_writer(str(template_hooks['page_header']()))
        __M_writer('\n                        ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n                </div>\n                <!--End of body content-->\n                <div style="clear:both;height:0;"></div>\n            </div>\n        </div>\n\n        <!-- Sidebar -->\n\n        <div class=" pure-u-6-24 pure_cell">\n            <div id="sidebar">\n                <div class="widget">\n                    <div id="search_bar">\n')
        if search_form:
            __M_writer('                        ')
            __M_writer(str(search_form))
            __M_writer('\n')
        __M_writer('                    </div>\n                </div>\n            </div>\n        </div>\n    </div>\n    <div id="footer">\n        ')
        __M_writer(str(content_footer))
        __M_writer('\n        ')
        __M_writer(str(template_hooks['page_footer']()))
        __M_writer('\n    </div>\n\n    <!--FIXME: put these somewhere                            -->\n    <!--%if len(translations) > 1:-->\n    <!--<li>')
        __M_writer(str(base.html_translations()))
        __M_writer('</li>-->\n    <!--%endif-->\n    <!--% if show_sourcelink:-->\n    <!--')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'sourcelink'):
            context['self'].sourcelink(**pageargs)
        

        __M_writer('-->\n    <!--%endif-->\n    <link href="/assets/css/duoshuo.css" type="text/css" rel="stylesheet"/>\n    ')
        __M_writer(str(base.late_load_js()))
        __M_writer('\n    <script>$(\'a.image-reference:not(.islink) img:not(.islink)\').parent().colorbox({rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true});</script>\n    <!-- fancy dates -->\n    <script>\n    moment.locale("')
        __M_writer(str(momentjs_locales[lang]))
        __M_writer('");\n    fancydates(')
        __M_writer(str(date_fanciness))
        __M_writer(', ')
        __M_writer(str(js_date_format))
        __M_writer(');\n    </script>\n    <!-- end fancy dates -->\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_js'):
            context['self'].extra_js(**pageargs)
        

        __M_writer('\n')
        if annotations and post and not post.meta('noannotations'):
            __M_writer(str(notes.code()))
            __M_writer('\n')
        elif not annotations and post and post.meta('annotations'):
            __M_writer(str(notes.code()))
            __M_writer('\n')
        __M_writer(str(body_end))
        __M_writer('\n')
        __M_writer(str(template_hooks['body_end']()))
        __M_writer('\n</body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        __M_writer = context.writer()
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_sourcelink(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def sourcelink():
            return render_sourcelink(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_js(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'base')._populate(_import_ns, ['*'])
        _mako_get_namespace(context, 'notes')._populate(_import_ns, ['*'])
        def extra_js():
            return render_extra_js(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/base.tmpl", "uri": "base.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 0, "61": 2, "62": 3, "63": 4, "64": 4, "65": 5, "66": 5, "71": 8, "72": 9, "73": 9, "74": 15, "75": 16, "76": 16, "77": 16, "78": 16, "79": 16, "80": 16, "81": 16, "82": 17, "83": 18, "84": 18, "85": 18, "86": 20, "87": 27, "88": 27, "89": 28, "90": 28, "91": 43, "92": 43, "97": 44, "98": 57, "99": 58, "100": 58, "101": 58, "102": 60, "103": 66, "104": 66, "105": 67, "106": 67, "107": 72, "108": 72, "113": 75, "114": 78, "115": 78, "116": 82, "117": 82, "118": 83, "119": 83, "120": 83, "121": 83, "126": 86, "127": 87, "128": 88, "129": 88, "130": 89, "131": 90, "132": 90, "133": 92, "134": 92, "135": 93, "136": 93, "142": 6, "151": 6, "157": 44, "171": 75, "185": 86, "199": 185}}
__M_END_METADATA
"""
