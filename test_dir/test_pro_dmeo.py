"""
page object model
Using the poium Library
https://github.com/SeldomQA/poium
```
> pip install poum
```
"""
import seldom
from seldom import Seldom

from pageobject.baidu_page import BaiduPage
from seldom import testdata

class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""
    def setUp(self):
        self.word = testdata.get_word()
        self.page = BaiduPage(Seldom.driver)
        self.page.get("https://www.baidu.com")

    def test_case(self):
        """
        A simple test
        """

        self.page.search_input = self.word
        self.page.search_button.click()
        self.assertTitle("%s_百度搜索"%self.word)




if __name__ == '__main__':
    seldom.main(debug=True, driver_path="../lib/chromedriver.exe")