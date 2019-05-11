from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("http://www.51zxw.net/")
sleep(2)
#根据option标签定位下拉元素
driver.find_elements_by_tag_name('option')[1].click()
#根据css定位下拉元素
driver.find_element_by_css_selector("[value='2']").click()
sleep(2)
driver.quit()
