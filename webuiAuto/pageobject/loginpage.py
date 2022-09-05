from time import sleep

from selenium import webdriver

from common.basepage import BasePage

from logs.log import log


class Login(BasePage):
    """ 登录页面"""

    def __init__(self, driver):
        BasePage.__init__(self, driver)

    def login(self, username, checkcode):
        """用户名、验证码测试"""

        self.input_text(username,*self.user)
        sleep(2)
        if checkcode:
            self.click(*self.verify)
            sleep(2)
            if self.exist_element(*self.login_alert):
                log.info(f'用户名输入错误')
                return self.get_text(*self.login_alert)
            else:
                self.click(*self.load)
                sleep(2)
                login_url = self.get_url()
                log.info(f'登录成功，进入页面url:{login_url}')
                return login_url
        else:
            self.click(*self.load)
            sleep(1)
            verify_text = self.get_text(*self.checkcode)
            log.info(f'验证码测试提示：请输入验证码')
            return verify_text



        #         self.click(*self.verify)
        #         sleep(2)                self.click(*self.load)
        #         sleep(3)                self.input_text(username, *self.user)
        #         sleep(2)
        #         if username:
        #             if checkcode:                        if self.get_text(*self.userwrong):
        #
        #
        #
        #             log.info(f'用户名错误')
        #             return self.get_text(*self.userwrong)
        #         else:
        #             login_url=self.get_url()
        #
        #
        #             log.info(f'登录成功，进入页面url:{login_url}')
        #             return login_url
        #     else:
        #         self.click(*self.load)
        #         sleep(1)
        #         verify_text=self.get_text(*self.checkcode)
        #         return verify_text
        # else:
        #     self.click(*self.verify)
        #     sleep(1)
        #     phone_text=self.get_text(*self.phone)
        #     log.info(f'phone_text:{phone_text}')
        #     log.info(f'用户名空提示：请输入手机号')
        #     return phone_text







if __name__ == '__main__':
   pass
