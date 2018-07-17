# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1531805870.029641
_enable_loop = True
_template_filename = 'themes/maupassant/templates/index.tmpl'
_template_uri = 'index.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content', 'content_header']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='index_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('pagination', context._clean_inheritance_tokens(), templateuri='pagination_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'pagination')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        front_index_header = context.get('front_index_header', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content_header():
            return render_content_header(context._locals(__M_locals))
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        permalink = context.get('permalink', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
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
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        index_file = context.get('index_file', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        permalink = context.get('permalink', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if posts and (permalink == '/' or permalink == '/' + index_file):
            __M_writer('        <link rel="prefetch" href="')
            __M_writer(str(posts[0].permalink()))
            __M_writer('" type="text/html">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        front_index_header = context.get('front_index_header', UNDEFINED)
        site_has_comments = context.get('site_has_comments', UNDEFINED)
        helper = _mako_get_namespace(context, 'helper')
        def content_header():
            return render_content_header(context)
        nextlink = context.get('nextlink', UNDEFINED)
        pagekind = context.get('pagekind', UNDEFINED)
        comments = _mako_get_namespace(context, 'comments')
        author_pages_generated = context.get('author_pages_generated', UNDEFINED)
        current_page = context.get('current_page', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        def content():
            return render_content(context)
        _link = context.get('_link', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        page_links = context.get('page_links', UNDEFINED)
        prevlink = context.get('prevlink', UNDEFINED)
        index_teasers = context.get('index_teasers', UNDEFINED)
        pagination = _mako_get_namespace(context, 'pagination')
        prev_next_links_reversed = context.get('prev_next_links_reversed', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content_header'):
            context['self'].content_header(**pageargs)
        

        __M_writer('\n')
        if 'main_index' in pagekind:
            __M_writer('    ')
            __M_writer(str(front_index_header))
            __M_writer('\n')
        if page_links:
            __M_writer('    ')
            __M_writer(str(pagination.page_navigation(current_page, page_links, prevlink, nextlink, prev_next_links_reversed)))
            __M_writer('\n')
        for post in posts:
            __M_writer('    <div class="post">\n        <h2 class="post-title"><a href="')
            __M_writer(str(post.permalink()))
            __M_writer('" >')
            __M_writer(filters.html_escape(str(post.title())))
            __M_writer('</a></h2>\n        <div class="post-meta">\n            ')
            __M_writer(filters.html_escape(str(post.formatted_date(date_format))))
            __M_writer('\n        </div>\n        <div class="post-meta">\n')
            if author_pages_generated:
                __M_writer('                <a href="')
                __M_writer(str(_link('author', post.author())))
                __M_writer('">')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('</a>\n')
            else:
                __M_writer('                ')
                __M_writer(filters.html_escape(str(post.author())))
                __M_writer('\n')
            __M_writer('        </div>\n        <div class="post-content">\n')
            if index_teasers:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=True)))
                __M_writer('\n')
            else:
                __M_writer('                ')
                __M_writer(str(post.text(teaser_only=False)))
                __M_writer('\n')
            if not post.meta('nocomments') and site_has_comments:
                __M_writer('                <p class="commentline">')
                __M_writer(str(comments.comment_link(post.permalink(), post._base_path)))
                __M_writer('\n')
            __M_writer('        </div>\n    </div>\n')
        __M_writer(str(helper.html_pager()))
        __M_writer('\n')
        __M_writer(str(comments.comment_link_script()))
        __M_writer('\n')
        __M_writer(str(helper.mathjax_script(posts)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content_header(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content_header():
            return render_content_header(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/maupassant/templates/index.tmpl", "uri": "index.tmpl", "source_encoding": "utf-8", "line_map": {"23": 2, "26": 3, "29": 4, "35": 0, "65": 2, "66": 3, "67": 4, "68": 5, "73": 12, "78": 50, "84": 7, "94": 7, "95": 8, "96": 8, "97": 9, "98": 10, "99": 10, "100": 10, "106": 14, "130": 14, "135": 15, "136": 16, "137": 17, "138": 17, "139": 17, "140": 19, "141": 20, "142": 20, "143": 20, "144": 22, "145": 23, "146": 24, "147": 24, "148": 24, "149": 24, "150": 26, "151": 26, "152": 29, "153": 30, "154": 30, "155": 30, "156": 30, "157": 30, "158": 31, "159": 32, "160": 32, "161": 32, "162": 34, "163": 36, "164": 37, "165": 37, "166": 37, "167": 38, "168": 39, "169": 39, "170": 39, "171": 41, "172": 42, "173": 42, "174": 42, "175": 44, "176": 47, "177": 47, "178": 48, "179": 48, "180": 49, "181": 49, "187": 15, "198": 187}}
__M_END_METADATA
"""
