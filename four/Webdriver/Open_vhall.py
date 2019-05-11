from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

#打开微吼主页
driver.get("http://www.baidu.com/")
driver.maximize_window()
print(driver.title)
sleep(2)

#打开微吼子页面
driver.get("http://map.baidu.com/")
driver.set_window_size(800,500)
print(driver.title)
driver.refresh()
print("had refresh")
sleep(3)

driver.back()
print("had back")
sleep(2)