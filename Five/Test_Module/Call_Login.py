from Login_Class import *  #*代表导入所有方法 #也可以单独导入某个方法
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)

Login().user_login(driver)
sleep(3)
Login().user_logot(driver)
sleep(3)
driver.quit()