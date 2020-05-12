from poium import Page, PageElement


class BaiduPage(Page):
    """baidu page"""
    search_input = PageElement(id_="kw")
    search_button = PageElement(id_="su")