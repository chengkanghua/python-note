from django.conf.urls import url
from app01 import views

class StarkSite(object):
    def __init__(self):
        self._registry = []

    def get_urls(self):
        patterns = []
        for app in self._registry:
           patterns.append(url('^%s/' % app,views.index))

        return patterns
    @property
    def urls(self):
        return (self.get_urls(),None,None)


site = StarkSite()