from Base.base import Base
from Page.page_elements import PageElements


class SearchPage(Base):
    """搜索页面"""

    def __init__(self):
        super().__init__()

    def input_search_text(self, text):
        """输入搜索输入框方法"""
        self.send_ele(PageElements.search_input_id, text)

    def get_search_result(self):
        """获取搜索结果方法"""
        results = self.find_eles(PageElements.search_result_ids)
        return [i.text for i in results]
