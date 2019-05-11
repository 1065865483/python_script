from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net/")

# 使用层 级和属性结合定位--输入用户名和密码
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[1]").send_keys("yidishui339")
driver.find_element_by_xpath("//form[@id='loginForm']/ul/input[2]").send_keys("chenxl339")
#使用逻辑运算组合定位--输入用户名和密码
# driver.find_element_by_xpath("//input[@type='text' and @name='username']").send_keys("yidishui339")
# driver.find_element_by_xpath("//input[@type='password' and @name='password']").send_keys("chenxl339")

sleep(3)
driver.quit()
