


from django import template


register=template.Library()


@register.filter      # 自定义过滤器
def multi_fliter(x,y):

    return x*y


@register.simple_tag    # 自定义标签
def multi_tag(x,y):

    return x*y

