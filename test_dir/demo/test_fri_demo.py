import seldom
from seldom import data_class
from commom.handle_path import chromedriver

"""
data_class传数据方法，参数的映射
"""


@data_class(
    ("keyword", "assert_tile"),
    [("seldom", "seldom_百度搜索"),
     ("python", "测试_百度搜索")
     ])
class YouTest(seldom.TestCase):
    def setUp(self):
        self.open("https://www.baidu.com")

    def test_case(self):
        """a simple test case """

        self.type(id_="kw", text=self.keyword)
        self.click(css="#su")
        self.assertTitle(self.assert_tile)


if __name__ == '__main__':
    seldom.main("test_fri_demo.py", driver_path=chromedriver)
