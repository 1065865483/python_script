from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get('http://www.51zxw.net/')
#定位标签名为input的元素
# driver.find_element_by_tag_name('input').send_keys('Selenium')
#寻获取页面所有标签名为"input"的标签
driver.find_elements_by_tag_name('input')[0].send_keys('Selenium')
sleep(3)
driver.quit()
