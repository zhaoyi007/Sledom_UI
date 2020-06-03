#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-01 10:09
# @Author  : zhaoyi
from poium import Page, PageElement, PageElements
import seldom
from seldom import Seldom, data

from lib.handle_config import URL


class Saas_login_Page(Page):
    """SAAS page"""
    input_username = PageElement(name="user", describe="输入用户名")
    input_password = PageElement(name="txtpassword", describe="输入密码")
    button_login = PageElement(xpath="/html/body/div[1]/div[2]/div[2]/div/div[4]/div[4]/button", describe="点击登录")



