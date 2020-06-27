from Base.base import Base
from Page.page_elements import PageElements


class XianshiPage(Base):
    """显示页面"""
    def __init__(self):
        super().__init__()

    def choise_font(self):
        """选择字体"""
        # 点击字体大小
        self.click_ele(PageElements.xianshi_set_font_btn_xpath)
        # 点击普通
        self.click_ele(PageElements.xianshi_choice_font_xpath)

    def get_summary_list(self):
        """获取描述信息"""
        # 获取所有描述信息
        results = self.find_eles(PageElements.xianshi_font_results_id)
        return [i.text for i in results]
