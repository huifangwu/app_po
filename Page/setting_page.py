from Base.base import Base
from Page.page_elements import PageElements


class SettingPage(Base):
    """设置页面"""

    def __init__(self):
        super().__init__()

    def click_xianshi_btn(self):
        """点击显示按钮"""
        self.click_ele(PageElements.setting_xianshi_btn_xpath)

    def click_search_btn(self):
        """点击搜索按钮"""
        self.click_ele(PageElements.search_btn_id)
