import pytest
from Base.driver import Driver
from Base.page import Page


class TestSearch:

    def teardown_class(self):
        Driver.quit_app_driver()

    @pytest.fixture(scope='class', autouse=True)
    def click_search_btn(self):
        Page.get_SettingPage().click_search_btn()

    @pytest.mark.parametrize('search_data, search_result', [('1', '休眠'), ('i', 'IP地址'), ('m', 'MAC地址')])
    def test_input_search(self, search_data, search_result):
        Page.get_SearchPage().input_search_text(search_data)
        assert search_result in Page.get_SearchPage().get_search_result()
