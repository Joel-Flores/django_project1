from django import template
from django.shortcuts import render
from django.urls import reverse
from django.utils.safestring import mark_safe

register = template.Library()

def resolve_url(url : str, id : [int, None]):
    if id:
        url = reverse(url, args=[id])
    else:
        url = reverse(url)
    return url

def render_html(template : str, context : [dict,None]):
    return mark_safe(
        render(
            request=None,
            template_name=template,
            context=context
        ).content.decode('utf-8')
    )