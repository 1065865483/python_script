from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get('http://www.51zxw.net/')
#完全匹配搜索
driver.find_element_by_link_text('网页设计').click()
#局部匹配搜索
driver.find_element_by_partial_link_text('勾勒').click()
sleep(3)
driver.quit()
