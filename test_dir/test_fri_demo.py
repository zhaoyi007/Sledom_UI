"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""
import unittest

import seldom
from seldom import Seldom, data
from lib.hadle_seldom import json_to_lsit
from lib.handle_config import URL
from lib.handle_path import chromedriver
from locator.baidu_page import BaiduPage
from seldom import testdata


class BaiduTest(seldom.TestCase):
    """Baidu test case"""

    def setUp(self) -> None:
        self.page = BaiduPage(Seldom.driver)
        self.open("https://www.baidu.com")
        self.max_window()

    @data(json_to_lsit(file='baidu.json', key="searchkey"))
    def test_baidu(self, search_key, exp):
        """
         used parameterized test
        :param search_key: search keyword
        :return:
        """
        self.page.search_input = search_key
        self.page.search_button.click()
        self.assertInTitle(exp)


if __name__ == '__main__':
    seldom.main(debug=True, driver_path=chromedriver)
