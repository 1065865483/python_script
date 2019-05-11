#测试环境：PC端登录并同时发送多条聊天消息
from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()
# <<<<<<< HEAD
driver.get("***********url")
# =======
driver.get("http://t.e.vhall.com/926816197")
# >>>>>>> 1beb509dcd0779600ea530b8e6ba719326a7d999

driver.find_element_by_css_selector(".to-login").click()
driver.find_element_by_css_selector("#username").clear()
driver.find_element_by_css_selector("#username").send_keys("****")
driver.find_element_by_css_selector("#pwd").clear()
driver.find_element_by_css_selector("#pwd").send_keys("****")
driver.find_element_by_id("to-login-common").click()
sleep(3)

for num in range(0,50000):
	# sleep(1)
	driver.find_element_by_id("mywords").send_keys(num)
	driver.find_element_by_css_selector(".send").click()
