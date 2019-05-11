from selenium import webdriver
from time import sleep

driver=webdriver.Chrome()
driver=webdriver.Firefox()
# driver.get("http://www.baidu.com/")
sleep(1)

driver.find_element_by_id("kw").clear()
driver.find_element_by_id("kw").send_keys("aa")
driver.find_element_by_id("su").click()