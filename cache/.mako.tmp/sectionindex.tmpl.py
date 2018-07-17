# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1531806319.680188
_enable_loop = True
_template_filename = '/Users/CJ/anaconda/lib/python3.6/site-packages/nikola/data/themes/base/templates/sectionindex.tmpl'
_template_uri = 'sectionindex.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('feeds_translations', context._clean_inheritance_tokens(), templateuri='feeds_translations_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'feeds_translations')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'index.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content():
            return render_content(context._locals(__M_locals))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        section = _import_ns.get('section', context.get('section', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        def extra_head():
            return render_extra_head(context)
        section = _import_ns.get('section', context.get('section', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n    ')
        __M_writer(str(feeds_translations.head(section)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'feeds_translations')._populate(_import_ns, ['*'])
        def content():
            return render_content(context)
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        feeds_translations = _mako_get_namespace(context, 'feeds_translations')
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        section = _import_ns.get('section', context.get('section', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n<div class="sectionindex">\n    <header>\n        <h2><a href="')
        __M_writer(str(_link('section_index', section)))
        __M_writer('">')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('</a></h2>\n        ')
        __M_writer(str(feeds_translations.feed_link(section)))
        __M_writer('\n    </header>\n    ')
        __M_writer(str(parent.content()))
        __M_writer('\n</div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/CJ/anaconda/lib/python3.6/site-packages/nikola/data/themes/base/templates/sectionindex.tmpl", "uri": "sectionindex.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "29": 0, "45": 2, "46": 3, "51": 8, "56": 18, "62": 5, "73": 5, "74": 6, "75": 6, "76": 7, "77": 7, "83": 10, "96": 10, "97": 13, "98": 13, "99": 13, "100": 13, "101": 14, "102": 14, "103": 16, "104": 16, "110": 104}}
__M_END_METADATA
"""
