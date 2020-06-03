#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-01 12:27
# @Author  : zhaoyi

import seldom
from seldom import Seldom

from locator.SAAS_page import Saas_login_Page


class Saas_oprate:
    """saas oprate"""
    def __init__(self):
        self.page = Saas_login_Page(Seldom.driver)

    def do_login(self, username, password):
        self.page.input_username = username
        self.page.input_password = password
        self.page.button_login.click()
