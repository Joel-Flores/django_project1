from utils.templatetags import register, resolve_url, render_html

@register.simple_tag()
def aside_title(name : str):
    context = {
        'title' : name
    }
    return render_html('components/aside/title.html', context)

@register.simple_tag()
def aside_principal_menu(title : str):
    context = {
        'title' : title
    }
    return render_html('components/aside/principal_menu.html', context)

@register.simple_tag()
def aside_li_simple(url : str, title : str):
    context = {
        'url' : resolve_url(url, None),
        'title' : title,
    }
    return render_html('components/aside/li_simple.html', context)

@register.simple_tag()
def aside_button(url : str, title : str):
    context = {
        'url' : resolve_url(url, None),
        'title' : title,
    }
    return render_html('components/aside/button.html', context)

#para el menu despleglabel aun no implementado del componente li_nav
@register.simple_tag()
def aside_li_button(title : str):
    context = {
        'title' : title,
    }
    return render_html('components/aside/li_button.html', context)

@register.simple_tag()
def aside_li_option(url : str, id : [str,None], title : str):
    context = {
        'url' : resolve_url(url, id),
        'title' : title
    }
    return render_html('components/aside/li_button.html', context)