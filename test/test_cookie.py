from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()

driver.get('http://www.baidu.com')
#手动添加cookie
driver.add_cookie({'name':'BAIDUID','value':'6'})
driver.add_cookie({'name':'BDUSS','value':''})
sleep(3)
# driver.refresh()
# sleep(2)
driver.quit()