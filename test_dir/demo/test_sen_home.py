import seldom
from seldom import data, Seldom
from seldom import excel_to_list, json_to_list
from commom.handle_config import URL
from commom.handle_path import chromedriver
from pageobject.home_page import login


class home_test(seldom.TestCase):
    def setup(self):
        pass

    @data(json_to_list(file='../../data/home.json', key="login"))
    def test_login(self, username, password, exp):

        self.page = login(Seldom.driver)
        self.page.get("https://www.testerhome.com")
        self.page.login_door.click()
        self.page.username_input = username
        self.page.password_input = password
        self.page.login_click.click()
        self.assertText(exp)

    def tearDown(self):
        try:
            self.select(self.page.login_select, value="退出")
        except:
            pass


if __name__ == "__main__":
    seldom.main(debug=True, driver_path=chromedriver)
