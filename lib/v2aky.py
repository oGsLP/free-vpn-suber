#!usr/bin/env python
# -*- coding:utf-8 -*-
"""
@author: lenovo by XYF
@file: v2aky.py
@time: 2020/03/02
@function: 
"""

import requests
import json
from lib.util.random import random_password, random_email
from lib.util.log import *

api = "https://v2aky.com/api/v1/"

session = ""
email = ""
password = ""


# headers = {
#     'accept': '*/*',
#
#     'origin': "https://v2aky.com",
#     'content-type': 'application/x-www-form-urlencoded',
#     'sec-fetch-mode': 'cors',
#     'sec-fetch-site': 'same-origin',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#
# }


def register():
    global email, password
    email = random_email()
    password = random_password(8)
    log_step(1, "register")
    form_data = {
        'email': email,
        'password': password,
        'invite_code': "",
        'email_code': ""
    }
    res = requests.post(api + "passport/auth/register", params=form_data)
    log_success()
    log_info("account", email)
    log_info("password", password)
    # print(json.loads(res.content.decode(encoding='utf-8', errors='strict')))
    res.close()


def login():
    global session
    log_step(2, "login")
    form_data = {
        'email': email,
        'password': password
    }
    res = requests.post(api + "passport/auth/login", params=form_data)
    log_success()
    # token = json.loads(res.content.decode(encoding='utf-8', errors='strict'))['data']['token']
    session = res.cookies["v2board_session"]
    # print('token')
    # print(token)
    res.close()


def order():
    global session
    log_step(3, "order")

    form_data = {
        'plan_id': 1,
        'cycle': 'year_price'
    }
    res = requests.post(api + "user/order/save", params=form_data, cookies={"v2board_session": session})
    session = res.cookies["v2board_session"]

    trade_no = json.loads(res.content.decode(encoding='utf-8', errors='strict'))['data']
    log_success()
    # print(trade_no)
    res.close()
    return trade_no


def checkout(trade_no):
    log_step(4, "checkout")
    form_data = {
        'trade_no': trade_no,
        'method': 5
    }
    res = requests.post(api + "user/order/checkout", params=form_data, cookies={"v2board_session": session})
    log_success()
    # print(res2.status_code)
    res.close()
    # res3 = requests.get(api + "user/order/check", params={'trade_no': trade_no}, cookies={"v2board_session": session})
    # print(json.loads(res1.content.decode(encoding='utf-8', errors='strict'))['data'])
    # session = res3.cookies["v2board_session"]


def subscribe():
    log_step(5, "subscribe")
    res = requests.get(api + "user/getSubscribe", cookies={"v2board_session": session})
    log_success()
    sub_url = json.loads(res.content.decode(encoding='utf-8', errors='strict'))['data']['subscribe_url']
    log_info("get v2Ray subscription url (from https://v2aky.com)")
    log_info(sub_url)
    res.close()
    return sub_url


def get_sub():
    register()
    login()
    checkout(order())
    return subscribe()


if __name__ == '__main__':
    get_sub()
