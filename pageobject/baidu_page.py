from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")
    login_in = PageElement(class_name="s-top-login-btn c-btn c-btn-primary c-btn-mini lb", describe="进入登陆")
    # login_door = PageElement(id_="TANGRAM__PSP_10__footerULoginBtn")
    input_username = PageElement(id_="TANGRAM__PSP_10__userName", describe="输入用户名")
    input_password = PageElement(id_="TANGRAM__PSP_10__password", describe="输入密码")
    login_button = PageElement(id_="TANGRAM__PSP_10__submit", describe="点击登陆")
