from selenium import webdriver
from time import sleep

#加载浏览器驱动
driver=webdriver.Firefox()
# driver=webdriver.Chrome()
# driver=webdriver.Ie()

#打开我要自学网页面，打印网页标题，等待3s
driver.get("http://www.51zxw.net")
print(driver.title)
sleep(5)

driver.get("http://www.baidu.com")
print(driver.title)
sleep(5)

driver.get("http://e.vhall.com/")
print(driver.title)
sleep(3)

#退出浏览器
# driver.quit()

