#线上环境：PC端登录并同时发送多条聊天消息
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
driver.get("*****观看端url")

driver.find_element_by_css_selector(".to-login").click()
driver.find_element_by_css_selector("#username").clear()
driver.find_element_by_css_selector("#username").send_keys("****观看端账号")
driver.find_element_by_css_selector("#pwd").clear()
driver.find_element_by_css_selector("#pwd").send_keys("****对应密码")
driver.find_element_by_id("to-login-common").click()
sleep(3)

for num in range(0,1000):
	# sleep(1)
	driver.find_element_by_id("mywords").send_keys(num)
	driver.find_element_by_css_selector(".send").click()
