from django import template

register = template.Library()


@register.filter("mobile_fmt")
def mobile_fmt(content):
    return content[:3] + "*****" + content[-3:]
