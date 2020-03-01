#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: util.py
@time: 2020/03/02
@function: 
"""

import time

emails = ["gamil.com", "qq.com", "outlook.com", "163.com", "126.com", "yeah.net", "foxmail.com"]


def random_email(letter=True, digit=10, kind=None):
    [stamp, seed] = str(time.time()).split('.')
    stamp = stamp[0:digit]
    prefix = chr(ord('a') + int(seed) % 26) + stamp if letter else stamp
    postfix = kind if kind else emails[int(seed) % len(emails)]
    return prefix + "@" + postfix


def random_password(length=8):
    if length < 8:
        length = 8
    seed = int(str(time.time()).split('.')[0])
    d_cycle = (length - 2) // 3
    l_cycle = length - d_cycle * 3
    letter = chr(ord('a') + seed % 26)
    return chr(ord(letter)-33)  +letter * (l_cycle-1) + str(seed)[-3:] * d_cycle
