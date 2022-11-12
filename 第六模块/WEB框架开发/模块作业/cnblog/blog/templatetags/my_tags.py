

from django import template
from django.db.models import Count
from blog import models
register=template.Library()


@register.simple_tag   # 注册的自定义tag 可以在模板里{% multi_tag | 2 3 %} 调用
def multi_tag(x,y):
    return x*y


@register.inclusion_tag("classification.html")
def get_classification_style(username):

    user = models.UserInfo.objects.filter(username=username).first()
    blog = user.blog

    cate_list=models.Category.objects.filter(blog=blog).values("pk").annotate(c=Count("article__title")).values_list("title","c")

    tag_list=models.Tag.objects.filter(blog=blog).values("pk").annotate(c=Count("article")).values_list("title","c")

    date_list=models.Article.objects.filter(user=user).extra(select={"y_m_date":"date_format(create_time,'%%Y/%%m')"}).values("y_m_date").annotate(c=Count("nid")).values_list("y_m_date","c")


    return {"blog":blog,"cate_list":cate_list,"date_list":date_list,"tag_list":tag_list,'username':username}  #返回给classification.html,在模板里调用会返回渲染好的classification.html