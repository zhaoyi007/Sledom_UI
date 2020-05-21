"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""
import seldom
from seldom import Seldom, data

from commom.hadle_csv_result import Utility
from commom.hadle_seldom import json_to_lsit
from commom.handle_config import URL
from commom.handle_path import chromedriver
from pageobject.baidu_page import BaiduPage
from seldom import testdata


class BaiduTest(seldom.TestCase):
    """Baidu test case"""

    def setUp(self) -> None:
        self.page = BaiduPage(Seldom.driver)
        self.open(URL)
        self.max_window()

    @seldom.skip()
    def test_demo(self):
        """
        A simple test
        """
        self.word = testdata.get_word()
        self.page.search_input = self.word
        self.page.search_button.click()
        self.assertTitle("%s_百度搜索" % self.word)

    @data(json_to_lsit(file='baidu.json', key="searchkey"))
    def test_baidu(self, search_key, exp):
        """
         used parameterized test
        :param search_key: search keyword
        :return:
        """
        self.page.search_input = search_key
        self.page.search_button.click()
        self.assertInTitle(exp, Utility.write_result("搜素测试", [search_key, exp]))

    @data(json_to_lsit(file='baidu.json', key="login"))
    @seldom.skip()
    def test_login(self, username, password, exp):
        self.page.login_in.click()
        self.page.input_username = username
        self.page.input_password = password
        self.page.login_button.click()
        self.assertText(exp)


if __name__ == '__main__':
    seldom.main(debug=True, driver_path=chromedriver)
