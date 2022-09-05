import yaml

from config import file_path


class BasePage:
    """元素定位公共方法"""

    def __init__(self, driver):
        self.driver = driver
        self.path = file_path.get_path('pagele.yaml')
        with open(self.path, 'r', encoding='utf-8') as f:
            file_dt = yaml.load(f, Loader=yaml.FullLoader)[self.__class__.__name__]
        for key in file_dt:
            self.__setattr__(key, file_dt[key])

    # 判断元素是否存在
    def exist_element(self, *selector):
        return self.driver.find_element(*selector)

    # 输入文本
    def input_text(self, text, *selector):
        self.driver.find_element(*selector).send_keys(text)

    # 获取页面标题
    def get_title(self):
        return self.driver.title

    # 获取页面url
    def get_url(self):
        return self.driver.current_url

    # 获取文本
    def get_text(self, *selector):
        return self.driver.find_element(*selector).text

    # 点击
    def click(self, *selector):
        self.driver.find_element(*selector).click()


if __name__ == '__main__':
    from selenium import webdriver

    driver = webdriver.Chrome()
    mn = BasePage(driver)
