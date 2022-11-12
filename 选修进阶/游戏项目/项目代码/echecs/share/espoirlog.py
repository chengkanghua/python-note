# coding=utf-8

"""

"""

__all__ = [
    'getLogger',
    'DEBUG',
    'INFO',
    'WARN',
    'ERROR',
    'FATAL']

import time
import logging
import logging.handlers
import os
from logging import getLogger, INFO, WARN, DEBUG, ERROR, FATAL, WARNING, CRITICAL
from firefly.server.globalobject import GlobalObject

LOG_FILE_MAX_BYTES = 31457280
LOG_FILE_BACKUP_COUNT = 1000
LOG_LEVEL = logging.DEBUG

MODULE_NAME = GlobalObject().json_config.get("name", '')
LOG_DIR = GlobalObject().json_config.get("log_dir", './logs')
if not os.path.exists(LOG_DIR):
    os.system("mkdir -p %s" % LOG_DIR)

# DATE_FORMAT = time.strftime('%Y-%m-%d', time.localtime(time.time()))

FORMAT = '[%(asctime)s]-%(levelname)-8s<%(name)s> {%(filename)s:%(lineno)s} -> %(message)s'
formatter = logging.Formatter(FORMAT)


def get_normal_log(module_name, date_format):
    file_name = '{0}/{1}_{2}.log'.format(LOG_DIR, module_name, date_format)
    normal_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=LOG_FILE_MAX_BYTES,
                                                          backupCount=LOG_FILE_BACKUP_COUNT)
    normal_handler.setFormatter(formatter)
    normal_log = getLogger(module_name)
    normal_log.setLevel(LOG_LEVEL)
    normal_log.addHandler(normal_handler)
    return normal_log


def get_error_log(module_name, date_format):
    file_name = '{0}/ERROR_{1}_{2}.log'.format(LOG_DIR, module_name, date_format)
    error_handler = logging.handlers.RotatingFileHandler(file_name, maxBytes=LOG_FILE_MAX_BYTES,
                                                         backupCount=LOG_FILE_BACKUP_COUNT)
    error_handler.setFormatter(formatter)
    error_log = getLogger(module_name+'_error')
    error_log.setLevel(LOG_LEVEL)
    error_log.addHandler(error_handler)
    return error_log

class EspoirLog(object):

    def __init__(self, module_name):
        self._normal = None
        self._error = None
        self.name = module_name
        self.last_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))   # 存放上一次打印日志的时间(字符串)

    @property
    def normal_log(self):
        cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if not self._normal or self.last_date != cur_date:
            self.last_date = cur_date
            self._normal = get_normal_log(self.name, self.last_date)
        return self._normal

    @property
    def error_log(self):
        cur_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        if not self._error or self.last_date != cur_date:
            self.last_date = cur_date
            self._error = get_error_log(self.name, self.last_date)
        return self._error

    def set_name(self, name):
        self.name = name

    def setLevel(self, level):
        self.normal_log.setLevel(level)

    def _backup_print(self, msg, *args, **kwargs):
        return
        if args:
            msg = "{0}/{1}".format(msg, str(args))
        if kwargs:
            msg = "{0}/{1}".format(msg, str(kwargs))
        print(msg)

    def debug(self, msg, *args, **kwargs):
        if self.normal_log.isEnabledFor(DEBUG):
            self.normal_log._log(DEBUG, msg, args, **kwargs)
            self._backup_print(msg, args, kwargs)

    def info(self, msg, *args, **kwargs):
        if self.normal_log.isEnabledFor(INFO):
            self.normal_log._log(INFO, msg, args, **kwargs)
            self._backup_print(msg, args, kwargs)

    def warning(self, msg, *args, **kwargs):
        if self.normal_log.isEnabledFor(WARN):
            self.normal_log._log(WARNING, msg, args, **kwargs)

    def warn(self, msg, *args, **kwargs):
        if self.normal_log.isEnabledFor(WARN):
            self.normal_log._log(WARN, msg, args, **kwargs)

    def error(self, msg, *args, **kwargs):
        if self.error_log.isEnabledFor(ERROR):
            self.normal_log._log(ERROR, msg, args, **kwargs)
            self.error_log._log(ERROR, msg, args, **kwargs)
        print(msg, args, kwargs)

    def critical(self, msg, *args, **kwargs):
        if self.error_log.isEnabledFor(CRITICAL):
            self.normal_log._log(CRITICAL, msg, args, **kwargs)
            self.error_log._log(CRITICAL, msg, args, **kwargs)

    def fatal(self, msg, *args, **kwargs):
        if self.error_log.isEnabledFor(FATAL):
            self.normal_log._log(FATAL, msg, args, **kwargs)
            self.error_log._log(FATAL, msg, args, **kwargs)


logger = EspoirLog(MODULE_NAME)
