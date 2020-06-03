#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020-06-01 9:37
# @Author  : zhaoyi
import time

import seldom
from seldom import Seldom, data
from pageobject.SAAS_oprate import Saas_oprate
from lib.handle_config import URL
from lib.handle_path import chromedriver


class Sass(seldom.TestCase):

    def setUp(self) -> None:
        self.open(URL)
        self.max_window()

    @data([("15600000000", "a123456"), ("15600000000", ""), ("", "a123456")])
    @seldom.skip()
    def test_login_fail(self, *params):
        Saas_oprate().do_login(*params)
        self.assertText(text="账号密码登录")

    @data([("15600000000", "a123456.")])
    def test_login_sucess(self, *params):
        Saas_oprate().do_login(*params)
        self.assertInUrl(url="http://testagent.graspyun.com/Agent/NewHome")

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    seldom.main(debug=True, driver_path=chromedriver)
