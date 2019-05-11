from LoginClass_Para import *
from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://localhost")
driver.implicitly_wait(10)
Login().user_login(driver,'yidishui','123456')
sleep(3)
Login().user_logot(driver)
sleep(2)
Login().user_login(driver,'yidishuitest','123456')
sleep(2)
Login().user_logot(driver)
sleep(2)
driver.quit()