from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost")

driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("yidishui")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("123456")

driver.find_element_by_css_selector(".inputSub").click()
sleep(3)
driver.find_element_by_link_text("退出").click()
sleep(3)
driver.switch_to.alert.accept()
sleep(3)
driver.quit()