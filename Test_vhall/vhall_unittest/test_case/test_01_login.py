from StartEnd import *
from selenium import webdriver

from Test_vhall.vhall_unittest.sendMsg import Test_StartEnd

driver= webdriver.Firefox()
class Test_01_login(Test_StartEnd):
    def test_01_login(self):
        '''登录'''
        driver.get("****登录界面url")
        driver.find_element_by_xpath("//input[@type='text' and @name='account']").clear()
        driver.find_element_by_xpath("//input[@type='text' and @name='account']").send_keys("****账号")
        driver.find_element_by_xpath("//input[@type='password' and @name='password']").clear()
        driver.find_element_by_xpath("//input[@type='password' and @name='password']").send_keys("****密码")
        driver.find_element_by_id("account-to-login").click()

if __name__=='__main__':
	unittest.main()