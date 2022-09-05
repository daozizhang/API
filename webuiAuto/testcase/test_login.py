import unittest
import warnings

from ddt import ddt,file_data
from selenium import webdriver
from time import sleep
from pageobject.loginpage import Login
from testdata.file_path import get_path
from logs.log import log




@ddt
class UtLogin(unittest.TestCase):
    """用户登录测试"""

    def setUp(self):
        warnings.simplefilter('ignore',ResourceWarning)
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    def tearDown(self):
        sleep(2)
        self.driver.quit()

    @file_data(get_path('login.yaml'))
    def test_login(self,**kwargs):
        """登录测试"""

        for key in kwargs:
            self.__setattr__(key,kwargs[key])
        self.driver.get(self.url)
        actual='None'
        try:
            actual=Login(self.driver).login(self.username,self.checkcode)
        except BaseException as e:
            log.error(f'登录异常错误\n', e)
        self.assertEqual(self.expect, actual, msg=f'【{self.testcase}】测试--FAIL\n')
        log.info(f'【{self.testcase}】测试用例--PASS\n')


if __name__ == '__main__':
    unittest.main()

