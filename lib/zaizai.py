#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: zaizai.py
@time: 2020/03/02
@function: 
"""

import requests
from lib.util.random import *
from lib.util.log import *
import re

api = "https://zaizaicloud.pw/"

email = ""
password = ""
username = ""
# email = "g1583167636@outlook.com"
# password = "Fg636636"
# username = "gkgk36"

cookies = None


def register():
    global email, password, username
    email = random_email()
    password = random_password()
    username = random_name()

    log_step(1, "register")

    form_data = {
        'email': email,
        'name': username,
        'passwd': password,
        'repasswd': password,
        'code': 0
    }

    res = requests.post(api + "auth/register", params=form_data)

    log_success()
    log_info("username", username)
    log_info("account", email)
    log_info("password", password)

    res.close()


def login():
    global cookies

    log_step(2, "login")
    form_data = {
        'email': email,
        'passwd': password,
        'code': "",
        'remember_me': 1
    }
    res = requests.post(api + "auth/login", params=form_data)
    print("  √")
    cookies = res.cookies.get_dict()
    res.close()


def resolve():
    log_step(3, "resolve")

    res = requests.get(api + "user", cookies=cookies)

    sub_url = res.text.split("oneclickImport('ssr','")[1].split("')")[0]
    print("  √")
    log_info("get ssr subscription url (from https://zaizaicloud.pw)")
    log_info(sub_url)
    res.close()

    return sub_url


def get_sub():
    register()
    login()
    return resolve()


if __name__ == '__main__':
    get_sub()
