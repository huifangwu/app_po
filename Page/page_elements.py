from selenium.webdriver.common.by import By


class PageElements:
    """管理所有页面元素"""

    # ----搜索页面元素----
    # 定位搜索按钮
    search_btn_id = (By.ID, 'com.android.settings:id/search')
    # 定位搜索输入框
    search_input_id = (By.ID, 'android:id/search_src_text')
    # 定位搜素结果
    search_result_ids = (By.ID, 'com.android.settings:id/title')

    # ----设置页面元素----
    # 显示
    setting_xianshi_btn_xpath = (By.XPATH, '//*[contains(@text, "显示")]')

    # ----显示页面元素----
    # 字体大小
    xianshi_set_font_btn_xpath = (By.XPATH, '//*[contains(@text, "字体大小")]')
    # 选择字体 -普通
    xianshi_choice_font_xpath = (By.XPATH, '//*[contains(@text, "普通")]')
    # 描述信息
    xianshi_font_results_id = (By.ID, 'android:id/summary')
