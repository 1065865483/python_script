from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
#打开我要自学网页面并截图
driver.get("http://www.51zxw.net/")
driver.get_screenshot_as_file(r'E:\0python_script\four\Webdriver\zxw.jpg')
sleep(2)
#打开百度页面并截图
driver.get("http://www.baidu.com")
driver.get_screenshot_as_file(r'E:\0python_script\four\Webdriver\baidu.png')
sleep(2)

driver.quit()
