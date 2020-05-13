"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""
import seldom
from seldom import Seldom, data, json_to_list

from pageobject.baidu_page import BaiduPage
from seldom import testdata


class BaiduTest(seldom.TestCase):
    """Baidu test case"""

    def setUp(self):

        self.page = BaiduPage(Seldom.driver)
        self.page.get("https://www.baidu.com")
        self.page.window_scroll(width=600, height=400)


    @seldom.skip()
    def test_demo(self):
        """
        A simple test
        """
        self.word = testdata.get_word()
        self.page.search_input = self.word
        self.page.search_button.click()
        self.assertTitle("%s_百度搜索" % self.word)

    # @data([
    #     (1, 'seldom'),
    #     (2, 'selenium'),
    #     (3, 'unittest'),
    # ])
    @data(json_to_list(file='../../data/baidu.json', key="searchkey"))
    def test_baidu(self, search_key):
        """
         used parameterized test
        :param name: case name
        :param search_key: search keyword
        :return:
        """
        self.page.search_input = search_key
        self.page.search_button.click()
        self.assertInTitle(search_key)

    @data(json_to_list(file='../../data/baidu.json', key="login"))
    @seldom.skip()
    def test_baidulogin(self, username, password, exp):

        self.page.login_in.click()
        self.page.input_username = username
        self.page.input_password = password
        self.page.login_button.click()
        self.assertText(exp)


if __name__ == '__main__':
    seldom.main(debug=True, driver_path="../../lib/chromedriver.exe")
