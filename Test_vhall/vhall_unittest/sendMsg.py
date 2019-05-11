#测试环境：PC端登录并同时发送多条聊天消息
from selenium import webdriver
from time import sleep
import unittest

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("Test is start")
    def tearDown(self):
        print("Test is end")

driver = webdriver.Firefox()
class Test_sendChat(Test_StartEnd):
	def test_01_login(self):
		driver.get("******活动url")
		driver.find_element_by_css_selector(".to-login").click()
		driver.find_element_by_css_selector("#username").clear()
		driver.find_element_by_css_selector("#username").send_keys("****观看端账号")
		driver.find_element_by_css_selector("#pwd").clear()
		driver.find_element_by_css_selector("#pwd").send_keys("****对应密码")
		driver.find_element_by_id("to-login-common").click()
	sleep(5)
	def test_02_send(self):
		sleep(2)
		for num in range(0,500):
			driver.find_element_by_id("mywords").send_keys(num)
			driver.find_element_by_css_selector(".send").click()

if __name__=='__main__':
	unittest.main
