#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from django.shortcuts import HttpResponse, render


class StarkHandler(object):
    def __init__(self, model_class, prev):
        self.model_class = model_class
        self.prev = prev

    def changelist_view(self, request):
        """
        列表页面
        :param request:
        :return:
        """
        # 访问http://127.0.0.1:8000/stark/app01/depart/list/； self.model_class = app01.models.Depart
        # 访问http://127.0.0.1:8000/stark/app01/userinfo/list/； self.model_class = app01.models.UserInfo
        # 访问http://127.0.0.1:8000/stark/app02/role/list/； self.model_class = app02.models.Role
        # 访问http://127.0.0.1:8000/stark/app02/host/list/； self.model_class =app02.models.Host
        # self.models_class
        data_list = self.model_class.objects.all()
        return render(request, 'stark/changelist.html', {'data_list': data_list})

    def add_view(self, request):
        """
        添加页面
        :param request:
        :return:
        """
        # self.models_class
        return HttpResponse('添加页面')

    def change_view(self, request, pk):
        """
        编辑页面
        :param request:
        :param pk:
        :return:
        """
        # self.models_class
        return HttpResponse('编辑页面')

    def delete_view(self, request, pk):
        """
        删除页面
        :param request:
        :param pk:
        :return:
        """
        # self.models_class
        return HttpResponse('删除页面')

    def get_urls(self):
        app_label, model_name = self.model_class._meta.app_label, self.model_class._meta.model_name
        if self.prev:
            patterns = [
                url(r'^list/$', self.changelist_view, name='%s_%s_%s_list' % (app_label, model_name, self.prev)),
                url(r'^add/$', self.add_view, name='%s_%s_%s_add' % (app_label, model_name, self.prev)),
                url(r'^change/(\d+)/$', self.change_view, name='%s_%s_%s_change' % (app_label, model_name, self.prev)),
                url(r'^delete/(\d+)/$', self.delete_view, name='%s_%s_%s_delete' % (app_label, model_name, self.prev)),
            ]
        else:
            patterns = [
                url(r'^list/$', self.changelist_view, name='%s_%s_list' % (app_label, model_name,)),
                url(r'^add/$', self.add_view, name='%s_%s_add' % (app_label, model_name,)),
                url(r'^change/(\d+)/$', self.change_view, name='%s_%s_change' % (app_label, model_name,)),
                url(r'^delete/(\d+)/$', self.delete_view, name='%s_%s_delete' % (app_label, model_name,)),
            ]
        patterns.extend(self.extra_urls()) # extend 在列表末尾一次性追加另一个序列中的多个值。# 返回urls对象
        print(patterns)  # [<RegexURLPattern app01_depart_list ^list/$>,.....   ]
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
        self._registry.append({'model_class': model_class, 'handler': handler_class(model_class, prev), 'prev': prev})

    def get_urls(self):
        patterns = []
        for item in self._registry:
            model_class = item['model_class']
            handler = item['handler']
            prev = item['prev']
            app_label, model_name = model_class._meta.app_label, model_class._meta.model_name
            if prev:  # 如果有url前缀
                patterns.append(url(r'^%s/%s/%s/' % (app_label, model_name, prev,), (handler.get_urls(), None, None)))
            else:
                patterns.append(url(r'%s/%s/' % (app_label, model_name,), (handler.get_urls(), None, None)))

        return patterns

    @property
    def urls(self):
        return self.get_urls(), self.app_name, self.namespace


site = StarkSite()
