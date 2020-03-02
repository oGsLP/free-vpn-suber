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

[stamp, seed] = str(time.time()).split('.')


def random_email(letter=True, digit=10, kind=None):
    prefix = chr(ord('a') + int(seed) % 26) + stamp[0:digit] if letter else stamp[0:digit]
    postfix = kind if kind else emails[int(seed) % len(emails)]
    return prefix + "@" + postfix


def random_password(length=8):
    if length < 8:
        length = 8
    d_cycle = (length - 2) // 3
    l_cycle = length - d_cycle * 3
    letter = chr(ord('a') + (int(seed)-10) % 26)
    return chr(ord(letter) - 33) + letter * (l_cycle - 1) + stamp[-3:] * d_cycle


def random_name(length=6):
    if length < 6:
        length = 6
    d_len = length - 4
    name = stamp[-d_len:]

    name = (chr(ord('a')+(int(seed)+7) % 26)+chr(ord('a')+int(stamp[-2:]) % 26))*2 + name
    return name
