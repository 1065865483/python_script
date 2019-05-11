from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get("http://www.baidu.com")
driver.find_element_by_css_selector("#kw").send_keys("python")

#键盘操作：Ctrl+A
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"a")
#键盘操作：Ctrl+C
# driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"c")
#键盘操作：Ctrl+X
driver.find_element_by_css_selector("#kw").send_keys(Keys.CONTROL,"x")
driver.get("http://hao.360.cn/?1004")
#键盘操作：Ctrl+V
driver.find_element_by_id("search-kw").send_keys(Keys.CONTROL,"v")
driver.find_element_by_id("search-btn").click()
sleep(3)
driver.quit()
