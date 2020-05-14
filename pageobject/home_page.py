from poium import Page, PageElement



class login(Page):
    # login_door = PageElement(xpath="//*[@id='main-page']/div[1]/nav/div/ul[1]/li[2]/a", describe="进入登录页面")
    login_door = PageElement(link_text="登录", describe="进入登录页面")
    username_input = PageElement(name="user[login]", describe="输入用户名")
    password_input = PageElement(id_="user_password", describe="输入密码")
    login_click = PageElement(name="commit", describe="点击登录")
    login_select = PageElement(class_name="dropdown-toggle" , describe="下拉框")