import seldom
from seldom import data


class BaiduTest(seldom.TestCase):
    """Baidu serach test case"""

    @data([
        (1, 'seldom'),
        (2, 'selenium'),
        (3, 'unittest'),
    ])
    def test_baidu(self, name, search_key):
        """
         used parameterized test
        :param name: case name
        :param search_key: search keyword
        :return:
        """
        self.open("https://www.baidu.com")
        self.type(id_="kw", text=search_key)
        self.click(css="#su")
        self.assertInTitle("seldom")



if __name__ == '__main__':
    seldom.main("test_frist_demo.py", driver_path='../lib/chromedriver.exe')