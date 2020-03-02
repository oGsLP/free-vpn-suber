#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: main.py
@time: 2020/03/02
@function: 
"""
import lib.v2aky as v2aky
import lib.zaizai as zz
import time


def run():
    v2aky.get_sub()
    print()
    time.sleep(0.1)
    zz.get_sub()
    print()
    input("请按回车后退出...")


if __name__ == '__main__':
    run()
