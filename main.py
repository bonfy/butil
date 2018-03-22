# -*- coding:utf-8 -*-
###
# Author: bonfy
# Email: foreverbonfy@163.com
# Created Date: 2018-03-22
###

import butil
import time

@butil.timer
def hello(name):
    time.sleep(3)
    print(f'hello {name}')


@butil.timer
def hello_return(name):
    time.sleep(2)
    print(f'hello_return {name}')
    return name

@butil.timer
def hello_ex(name):
    print(f'hello_ex {name}')
    raise Exception('hello exception')

def main():
    r1 = hello('bonfy')
    print(r1)

    r2 = hello_return('bohis')
    print(r2)

    r3 = hello_ex('bonfy')
    print(r3)


if __name__ == '__main__':
    main()