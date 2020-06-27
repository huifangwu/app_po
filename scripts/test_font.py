from Base.driver import Driver
from Base.page import Page


class TestSetFont:
    def teardown_class(self):
        Driver.quit_app_driver()

    def test_set_font(self):
        Page.get_SettingPage().click_xianshi_btn()
        Page.get_XianshiPage().choise_font()
        assert '普通' in Page.get_XianshiPage().get_summary_list()
