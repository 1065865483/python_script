from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')
#获取cookie全部内容
cookie=driver.get_cookies()
print(cookie)
print(cookie[1])
#增加一条cookie
driver.add_cookie({'name':'aaa51zxw','value':'www.51zxw.net'})
for cookie in driver.get_cookies():
    print("%s--%s" %(cookie['name'],cookie['value']))
driver.quit()