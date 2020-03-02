#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: log.py
@time: 2020/03/03
@function: 
"""


def log_step(idx, info):
    print(str(idx) + ". " + info + " ...", end="")


def log_info(opt, val=None):
    if val:
        print("  + " + opt + ": " + val)
    else:
        print("  + " + opt)


def log_success():
    print("  √")
