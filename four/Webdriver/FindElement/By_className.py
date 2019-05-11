from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get('http://www.baidu.com/')
driver.find_element_by_class_name('s_ipt').send_keys('Selenium')
driver.find_element_by_class_name('bg s_btn').click()

driver.quit()