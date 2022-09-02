# coding=utf-8

from twisted.internet import reactor


class TimerTask(object):
    @classmethod
    def call_later(cls, interval, callback_func, *args, **kwargs):
        return reactor.callLater(interval, callback_func, *args, **kwargs)
