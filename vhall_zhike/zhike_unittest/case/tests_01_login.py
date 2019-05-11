from StartEnd import *
from selenium import webdriver
from time import sleep

from zhike_unittest.case.StartEnd import StartEnd

driver = webdriver.Firefox()
class Test_01_login(StartEnd):
    def test_01_login(self):
        '''登录'''
        driver.get('*******知客地址')
        driver.find_element_by_xpath("//input[@type='text' and @class='v-input']").clear()
        driver.find_element_by_xpath("//input[@type='text' and @class='v-input']").send_keys('****知客账号')
        driver.find_element_by_xpath("//input[@type='password' and @class='v-input']").clear()
        driver.find_element_by_xpath("//input[@type='password' and @class='v-input']").send_keys('****知客密码')
        driver.find_element_by_class_name('v-btn').click()
        sleep(3)

#     def test_01_login(self,username,passsword):
#         '''登录'''
#         driver.get('http://t-zhike.vhall.com/admin/login')
#         driver.find_element_by_xpath("//input[@type='text' and @class='v-input']").send_keys(username)
#         driver.find_element_by_xpath("//input[@type='password' and @class='v-input']").send_keys(passsword)
#         driver.find_element_by_class_name('v-btn').click()
#         sleep(1)
# Test_01_login().test_01_login(driver,'18210379813','123456')

if __name__=='__main__':
    unittest.main()