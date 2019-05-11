from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
sleep(3)
# driver.find_element_by_id('kw').send_keys('Selenium我要自学网')
driver.find_element_by_name('wd').send_keys('Selenium我要自学网')
sleep(3)

driver.find_element_by_id('su').click()
sleep(3)

driver.quit()
