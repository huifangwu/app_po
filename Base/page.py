from Page.search_page import SearchPage
from Page.setting_page import SettingPage
from Page.xianshi_page import XianshiPage


class Page:
    """返回所有页面实例化对象"""

    @classmethod
    def get_SettingPage(cls):
        """返回设置页面类实例化对象"""
        return SettingPage()

    @classmethod
    def get_XianshiPage(cls):
        """返回显示页面类实例化对象"""
        return XianshiPage()

    @classmethod
    def get_SearchPage(cls):
        """返回搜索页面类实例化对象"""
        return SearchPage()
