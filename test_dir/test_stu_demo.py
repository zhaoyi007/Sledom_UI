import seldom
from seldom import data_class


@data_class(
    ("keyword", "assert_tile"),
    [("seldom", "seldom_百度搜索"),
     ("python", "python_百度搜索")
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
    seldom.main("test_stu_demo.py", driver_path='../lib/chromedriver.exe')
