#!/usr/bin/env python
# -*- coding:utf-8 -*-
import functools
from types import FunctionType
from django.conf.urls import re_path
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.shortcuts import HttpResponse, render, redirect
from django.http import QueryDict
from django import forms
from django.db.models import Q
from django.db.models import ForeignKey, ManyToManyField
from django.utils.safestring import mark_safe
from stark.utils.pagination import Pagination
from django.db.models import ForeignKey, ManyToManyField


def get_choice_text(title, field, style=''):
    """
    对于Stark组件中定义列时，choice如果想要显示中文信息，调用此方法即可。
    :param title: 希望页面显示的表头
    :param field: 字段名称
    :return:
    """

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title
        method = "get_%s_display" % field
        field_td = '<span style="%s">%s</span>' % (style, getattr(obj, method)())
        return mark_safe(field_td)

    return inner


def get_datetime_text(title, field, time_format='%Y-%m-%d'):
    """
    对于Stark组件中定义列时，定制时间格式的信息。
    :param title: 希望页面显示的表头
    :param field: 字段名称
    :param time_format: 时间格式化
    :return:
    """

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title
        datetime_obj = getattr(obj, field)
        return datetime_obj.strftime(time_format)

    return inner


def get_m2m_text(title, field):
    """
    对于Stark组件中定义列时，获取m2m的数据
    :param title: 希望页面显示的表头
    :param field: 字段名称
    :param time_format: 时间格式化
    :return:
    """

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title
        query_set = getattr(obj, field).all()
        text_list = [str(row) for row in query_set]
        return ' , '.join(text_list)

    return inner


def get_another_text(title, field, style=''):
    """
    对于Stark组件中定义列时，字段自定义标题或者样式，调用此方法即可。
    :param title: 希望页面显示的表头
    :param field: 字段名称
    :param style: 样式
    :return:
    """

    def inner(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return title
        field_td = '<span style="%s">%s</span>' % (style, getattr(obj, field))
        return mark_safe(field_td)

    return inner


class SearchGroupRow(object):
    def __init__(self, title, queryset_or_tuple, option, query_dict):
        """
        :param title: 组合搜索列名称
        :param queryset_or_tuple: 组合搜索的数据
        :param option: 配置
        :param query_dict: url的参数
        """
        self.title = title
        self.queryset_or_tuple = queryset_or_tuple
        self.option = option
        self.query_dict = query_dict

    def __iter__(self):
        yield '<div class="whole">%s</div>' % self.title
        yield '<div class="others">'
        total_query_dict = self.query_dict.copy()
        total_query_dict._mutable = True
        orign_value_list = self.query_dict.getlist(self.option.field)
        if orign_value_list:
            total_query_dict.pop(self.option.field)
            yield "<a href='?%s'>全部</a>" % total_query_dict.urlencode()
        else:
            yield "<a href='?%s' class='active'>全部</a>" % total_query_dict.urlencode()

        for item in self.queryset_or_tuple:
            text = self.option.get_text(item)
            # 获取对应的值
            value = str(self.option.get_value(item))
            query_dict = self.query_dict.copy()
            query_dict._mutable = True

            if not self.option.is_multi:  # 单选
                query_dict[self.option.field] = value
                if value in orign_value_list:
                    query_dict.pop(self.option.field)
                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)
            else:  # 多选
                multi_value_list = query_dict.getlist(self.option.field)
                if value in multi_value_list:
                    multi_value_list.remove(value)
                    query_dict.setlist(self.option.field, multi_value_list)
                    yield "<a href='?%s' class='active'>%s</a>" % (query_dict.urlencode(), text)
                else:
                    multi_value_list.append(value)
                    query_dict.setlist(self.option.field, multi_value_list)
                    yield "<a href='?%s'>%s</a>" % (query_dict.urlencode(), text)

            # print(text, value, self.query_dict, orign_value_list)

        yield "</div>"


class Option(object):
    def __init__(self, field, is_multi=False, db_condition=None, text_func=None, value_func=None):
        """
        :param field: 组合搜索关联的字段
        :param is_multi: 是否支持多选
        :param db_condition: 数据库关联查询时的条件
        :param text_func: 显示用户指定文本
        """
        self.field = field
        self.is_multi = is_multi
        if not db_condition:
            db_condition = {}
        self.db_condition = db_condition
        self.text_func = text_func
        self.value_func = value_func
        self.is_choice = False

    def get_db_condition(self, request, *args, **kwargs):
        return self.db_condition

    def get_queryset_or_tuple(self, model_class, request, *args, **kwargs):
        """
        根据字段去获取数据库关联的数据
        :return:
        """
        # 根据gender或depart字符串，去自己对应的Model类中找到 字段对象
        field_object = model_class._meta.get_field(self.field)
        title = field_object.verbose_name
        # 获取关联数据
        # print(field_object, type(field_object))
        if isinstance(field_object, ForeignKey) or isinstance(field_object, ManyToManyField):
            # FK和M2M,应该去获取其关联表中的数据
            db_condition = self.get_db_condition(request, *args, **kwargs)
            # print(self.field, field_object.remote_field.model.objects.filter(**db_condition), db_condition)
            return SearchGroupRow(title, field_object.remote_field.model.objects.filter(**db_condition), self,
                                  request.GET)
        else:
            # 获取choice中的数据
            # print(self.field, field_object.choices)
            self.is_choice = True
            return SearchGroupRow(title, field_object.choices, self, request.GET)

    def get_text(self, field_object):
        if self.text_func:
            return self.text_func(field_object)
        if self.is_choice:
            return field_object[1]
        return str(field_object)

    def get_value(self, field_object):
        if self.value_func:
            return self.text_func(field_object)
        if self.is_choice:
            return field_object[0]
        return field_object.pk


class StarkModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StarkModelForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StarkForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(StarkForm, self).__init__(*args, **kwargs)
        # 统一给ModelForm生成字段添加样式
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StarkHandler(object):
    change_list_template = None  # 定义个类变量，可以给change页面拓展自定义模板页面

    list_display = []

    def display_checkbox(self, obj=None, is_header=None, *args, **kwargs):
        """
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "选择"
        return mark_safe('<input type="checkbox" name="pk" value="%s" />' % obj.pk)

    def display_edit(self, obj=None, is_header=None, *args, **kwargs):
        """
        自定义页面显示的列（表头和内容）
        :param obj:
        :param is_header:
        :return:
        """
        if is_header:
            return "编辑"
        return mark_safe('<a href="%s">编辑</a>' % self.reverse_change_url(pk=obj.pk))

    def display_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return "删除"
        return mark_safe('<a href="%s">删除</a>' % self.reverse_delete_url(pk=obj.pk))

    def display_edit_del(self, obj=None, is_header=None, *args, **kwargs):
        if is_header:
            return "操作"
        tpl = '<a href="%s">编辑</a>   <a href="%s">删除</a>' % (
            self.reverse_change_url(pk=obj.pk), self.reverse_delete_url(pk=obj.pk))
        return mark_safe(tpl)

    def get_list_display(self, request, *args, **kwargs):
        """
        获取页面上应该显示的列，预留的自定义扩展，例如：以后根据用户的不同显示不同的列
        :return:
        """
        value = []
        value.extend(self.list_display)
        value.append(type(self).display_edit_del)  # 当前对象的类
        return value

    per_page_count = 10

    has_add_btn = True

    def get_add_btn(self, request, *args, **kwargs):
        if self.has_add_btn:
            return "<a class='btn btn-primary' href='%s'>添加</a>" % self.reverse_add_url(*args, **kwargs)
        return None

    model_form_class = None

    def get_model_form_class(self, is_add, request, *args, **kwargs):
        """
        定制添加和编辑页面
        """
        if self.model_form_class:
            return self.model_form_class

        class DynamicModelForm(StarkModelForm):
            class Meta:
                model = self.model_class
                fields = "__all__"

        return DynamicModelForm

    order_list = []

    def get_order_list(self):
        return self.order_list or ['-id', ]

    search_list = []

    def get_search_list(self):
        return self.search_list

    action_list = []

    def get_action_list(self):
        return self.action_list

    def action_multi_delete(self, request, *args, **kwargs):
        """
        批量删除（如果想要定制执行成功后的返回值，那么就为action函数设置返回值即可。）
        :return:
        """
        pk_list = request.POST.getlist('pk')
        self.model_class.objects.filter(id__in=pk_list).delete()

    action_multi_delete.text = "批量删除"

    search_group = []

    def get_search_group(self):
        return self.search_group

    def get_search_group_condition(self, request):
        """
        获取组合搜索
        """
        # print("request.GET", request.GET, type(request.GET.get('gender')), request.GET.getlist('gender'))
        condition = {}
        for option in self.get_search_group():
            if option.is_multi:
                values_list = request.GET.getlist(option.field)
                if not values_list:
                    continue
                condition['%s__in' % option.field] = values_list
            else:
                value = request.GET.get(option.field)
                if not value:
                    continue
                condition[option.field] = value
        return condition

    def __init__(self, site, model_class, prev):
        self.site = site
        self.model_class = model_class
        self.prev = prev
        self.request = None

    def get_queryset(self, request, *args, **kwargs):
        return self.model_class.objects

    def changelist_view(self, request, *args, **kwargs):
        """
        列表页面
        :param request:
        :return:
        """
        # ########## 1. 处理Action ##########
        action_list = self.get_action_list()
        action_dict = {func.__name__: func.text for func in action_list}  # {'multi_delete':'批量删除','multi_init':'批量初始化'}

        if request.method == 'POST':
            action_func_name = request.POST.get('action')
            if action_func_name and action_func_name in action_dict:
                action_response = getattr(self, action_func_name)(request, *args, **kwargs)
                if action_response:
                    return action_response

        # ########## 2. 获取排序 ##########
        search_list = self.get_search_list()
        search_value = request.GET.get('q', '')
        conn = Q()
        conn.connector = 'OR'
        if search_value:
            for item in search_list:
                conn.children.append((item, search_value))

        # ########## 3. 获取排序 ##########
        order_list = self.get_order_list()
        search_group_condition = self.get_search_group_condition(request)
        prev_queryset = self.get_queryset(request, *args, **kwargs)
        queryset = prev_queryset.filter(conn).filter(**search_group_condition).order_by(*order_list)

        # ########## 4. 处理分页 ##########
        all_count = queryset.count()

        query_params = request.GET.copy()
        query_params._mutable = True

        pager = Pagination(
            current_page=request.GET.get('page'),
            all_count=all_count,
            base_url=request.path_info,
            query_params=query_params,
            per_page=self.per_page_count,
        )

        data_list = queryset[pager.start:pager.end]

        # ########## 5. 处理表格 ##########
        list_display = self.get_list_display(request, *args, **kwargs)
        # 5.1 处理表格的表头
        header_list = []
        if list_display:
            for key_or_func in list_display:
                if isinstance(key_or_func, FunctionType):
                    verbose_name = key_or_func(self, obj=None, is_header=True)
                else:
                    verbose_name = self.model_class._meta.get_field(key_or_func).verbose_name
                header_list.append(verbose_name)
        else:
            header_list.append(self.model_class._meta.model_name)

        # 5.2 处理表的内容

        body_list = []
        for row in data_list:
            tr_list = []
            if list_display:
                for key_or_func in list_display:
                    if isinstance(key_or_func, FunctionType):
                        tr_list.append(key_or_func(self, row, is_header=False, *args, **kwargs))
                    else:
                        tr_list.append(getattr(row, key_or_func))  # obj.gender
            else:
                tr_list.append(row)
            body_list.append(tr_list)

        # ########## 6. 添加按钮 #########
        add_btn = self.get_add_btn(request, *args, **kwargs)

        # ########## 7. 组合搜索 #########
        search_group = self.get_search_group()  # ['gender', 'depart']
        search_group_row_list = []
        for option_object in search_group:
            row = option_object.get_queryset_or_tuple(self.model_class, request, *args, **kwargs)
            search_group_row_list.append(row)

        return render(
            request,
            self.change_list_template or 'stark/changelist.html',
            {
                'data_list': data_list,
                'header_list': header_list,
                'body_list': body_list,
                'pager': pager,
                'add_btn': add_btn,
                'search_list': search_list,
                'search_value': search_value,
                'action_dict': action_dict,
                'search_group_row_list': search_group_row_list,
            }
        )

    def save(self, requet, form, is_update, *args, **kwargs):
        """
        在使用ModelForm保存数据之前预留的钩子方法
        :param form:
        :param is_update:
        :return:
        """
        form.save()

    def add_view(self, request, *args, **kwargs):
        """
        添加页面
        :param request:
        :return:
        """
        model_form_class = self.get_model_form_class(True, request, *args, **kwargs)
        if request.method == 'GET':
            form = model_form_class()
            return render(request, 'stark/change.html', {'form': form})
        form = model_form_class(data=request.POST)
        if form.is_valid():
            response = self.save(request, form, False, *args, **kwargs)
            # 在数据库保存成功后，跳转回列表页面(携带原来的参数)。
            return response or redirect(self.reverse_list_url(*args, **kwargs))
        return render(request, 'stark/change.html', {'form': form})

    def get_change_object(self, request, pk, *args, **kwargs):
        """修改页面，取对象"""
        return self.model_class.objects.filter(pk=pk).first()

    def change_view(self, request, pk, *args, **kwargs):
        """
        编辑页面
        :param request:
        :param pk:
        :return:
        """
        current_change_object = self.get_change_object(request, pk, *args, **kwargs)
        if not current_change_object:
            return HttpResponse('要修改的数据不存在，请重新选择！')

        model_form_class = self.get_model_form_class(False, request, *args, **kwargs)
        if request.method == 'GET':
            form = model_form_class(instance=current_change_object)
            return render(request, 'stark/change.html', {'form': form})
        form = model_form_class(data=request.POST, instance=current_change_object)
        if form.is_valid():
            response = self.save(request, form, True, *args, **kwargs)
            # 在数据库保存成功后，跳转回列表页面(携带原来的参数)。
            return response or redirect(self.reverse_list_url(*args, **kwargs))
        return render(request, 'stark/change.html', {'form': form})

    def get_delete_object(self, request, pk, *args, **kwargs):
        # 删除自定制
        self.model_class.objects.filter(pk=pk).delete()

    def delete_view(self, request, pk, *args, **kwargs):
        """
        删除页面
        :param request:
        :param pk:
        :return:
        """
        origin_list_url = self.reverse_list_url(*args, **kwargs)
        if request.method == 'GET':
            return render(request, 'stark/delete.html', {'cancel': origin_list_url})

        response = self.get_delete_object(request, pk, *args, **kwargs)
        return response or redirect(origin_list_url)

    def get_url_name(self, param):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        if self.prev:
            return '%s_%s_%s_%s' % (app_label, model_name, self.prev, param,)
        return '%s_%s_%s' % (app_label, model_name, param,)

    @property
    def get_list_url_name(self):
        """
        获取列表页面URL的name
        :return:
        """
        return self.get_url_name('list')

    @property
    def get_add_url_name(self):
        """
        获取添加页面URL的name
        :return:
        """
        return self.get_url_name('add')

    @property
    def get_change_url_name(self):
        """
        获取修改页面URL的name
        :return:
        """
        return self.get_url_name('change')

    @property
    def get_delete_url_name(self):
        """
        获取删除页面URL的name
        :return:
        """
        return self.get_url_name('delete')

    def reverse_common_url(self, name, *args, **kwargs):
        """
        生成带有原搜索条件的添加URL
        :return:
        """
        name = "%s:%s" % (self.site.namespace, name)
        base_url = reverse(name, args=args, kwargs=kwargs)
        if not self.request.GET:
            add_url = base_url
        else:
            param = self.request.GET.urlencode()
            new_query_dict = QueryDict(mutable=True)
            new_query_dict['_filter'] = param
            add_url = "%s?%s" % (base_url, new_query_dict.urlencode())
        return add_url

    def reverse_add_url(self, *args, **kwargs):
        """
        生成带有原搜索条件的添加URL
        :return:
        """
        return self.reverse_common_url(self.get_add_url_name, *args, **kwargs)

    def reverse_change_url(self, *args, **kwargs):
        """
        生成带有原搜索条件的编辑URL
        :param args:
        :param kwargs:
        :return:
        """
        return self.reverse_common_url(self.get_change_url_name, *args, **kwargs)

    def reverse_delete_url(self, *args, **kwargs):
        """
        生成带有原搜索条件的删除URL
        :param args:
        :param kwargs:
        :return:
        """
        return self.reverse_common_url(self.get_delete_url_name, *args, **kwargs)

    def reverse_list_url(self, *args, **kwargs):
        """
        跳转回列表页面时，生成URL
        :return:
        """
        name = "%s:%s" % (self.site.namespace, self.get_list_url_name,)
        base_url = reverse(name, args=args, kwargs=kwargs)
        param = self.request.GET.get('_filter')
        if not param:
            return base_url
        return "%s?%s" % (base_url, param,)

    def wrapper(self, func):
        @functools.wraps(func)
        def inner(request, *args, **kwargs):
            self.request = request
            return func(request, *args, **kwargs)

        return inner

    def get_urls(self):
        patterns = [
            re_path(r'^list/$', self.wrapper(self.changelist_view), name=self.get_list_url_name),
            re_path(r'^add/$', self.wrapper(self.add_view), name=self.get_add_url_name),
            re_path(r'^change/(?P<pk>\d+)/$', self.wrapper(self.change_view), name=self.get_change_url_name),
            re_path(r'^delete/(?P<pk>\d+)/$', self.wrapper(self.delete_view), name=self.get_delete_url_name),
        ]

        patterns.extend(self.extra_urls())
        return patterns

    def extra_urls(self):
        return []


class StarkSite(object):
    def __init__(self):
        self._registry = []
        self.app_name = 'stark'
        self.namespace = 'stark'

    def register(self, model_class, handler_class=None, prev=None):
        """

        :param model_class: 是models中的数据库表对应的类。 models.UserInfo
        :param handler_class: 处理请求的视图函数所在的类
        :param prev: 生成URL的前缀
        :return:
        """
        """
        self._registry = [
            {'prev':None, 'model_class':models.Depart,'handler': DepartHandler(models.Depart,prev)对象中有一个model_class=models.Depart   },
            {'prev':'private', 'model_class':models.UserInfo,'handler':  StarkHandler(models.UserInfo,prev)对象中有一个model_class=models.UserInfo   }
            {'prev':None, 'model_class':models.Host,'handler':  HostHandler(models.Host,prev)对象中有一个model_class=models.Host   }
        ]
        """
        if not handler_class:
            handler_class = StarkHandler
        self._registry.append(
            {'model_class': model_class, 'handler': handler_class(self, model_class, prev), 'prev': prev})

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler']
            prev = item['prev']
            app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
            if prev:
                patterns.append(
                    re_path(r'^%s/%s/%s/' % (app_label, model_name, prev,), (handler.get_urls(), None, None)))
            else:
                patterns.append(re_path(r'%s/%s/' % (app_label, model_name,), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
