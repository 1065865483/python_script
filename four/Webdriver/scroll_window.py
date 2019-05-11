from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get('http://www.51zxw.net/')
sleep(2)
#webdriver不能操作的方法可通过js实现
#将滚动条拖到底部-
js="var action=document.documentElement.scrollTop=10000"
driver.execute_script(js)
sleep(2)

#将滚动条拖到顶部
js="var action=document.documentElement.scrollTop=0"
driver.execute_script(js)
sleep(2)
driver.quit()