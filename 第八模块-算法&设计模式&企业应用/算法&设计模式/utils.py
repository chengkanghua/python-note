import time
import functools

def Cal_time(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        stop_time = time.time()
        print('%s runtime: %s'% (func.__name__,stop_time-start_time))
    return inner



