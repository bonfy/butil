# -*- coding:utf-8 -*-
import time
import functools


def timer(f):

    @functools.wraps(f)
    def function_timer(*args, **kwargs):
        print(f'Function {f} begin run...')
        t0 = time.time()
        result = f(*args, **kwargs)
        t1 = time.time()
        td = t1 - t0
        print(f'Function {f} finish')
        print(f'Function {f} total run time: {td} seconds')
        return result

    return function_timer
