from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
path1 = r'https://roms-admin-test.ifyou.net/#/login'

driver.get(path1)
print(driver.title)
driver.implicitly_wait(3)
sleep(2)
#输入用户民
name=driver.find_element('xpath','//input[@placeholder="请输入手机号"]').send_keys('13021200001')
print(name)
#登录
# driver.find_element('xpath',"//span[text()='登录']").click()
sleep(2)
# text=driver.find_element('xpath','//div[text()="手机号不能为空!"]').text
# print(text)
driver.close()


