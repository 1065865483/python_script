from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import unittest
from StartEnd import *


# class Test_StartEnd(unittest.pms):
#     def setUp(self):
#         print("Test is start")
#     def tearDown(self):
#         print("Test is end")
from Test_vhall.vhall_unittest.sendMsg import Test_StartEnd

driver = webdriver.Firefox()

class Test_case_01(Test_StartEnd):
#登录
    def test_01_login(self):
        '''登录'''
        driver.get("http://t.e.vhall.com/auth/login")
        driver.find_element_by_xpath("//input[@type='text' and @name='account']").clear()
        driver.find_element_by_xpath("//input[@type='text' and @name='account']").send_keys("v16417554")
        driver.find_element_by_xpath("//input[@type='password' and @name='password']").clear()
        driver.find_element_by_xpath("//input[@type='password' and @name='password']").send_keys("123456")
        driver.find_element_by_id("account-to-login").click()

#创建单视频活动
    def test_02_createVideoA(self):
        '''创建单视频活动'''
        driver.get("****单视频活动url")
        driver.find_element_by_id("event-title").send_keys("单视频活动")
        sleep(2)
        driver.find_element_by_id("event-introduce").clear()
        driver.find_element_by_id("event-introduce").send_keys("123456")
        sleep(3)
        # driver.find_element_by_xpath("/html/body/section/div/form/div[2]/div[11]/button").click()
        driver.find_element_by_css_selector(".savebtn").click()
        sleep(2)

#活动开始
    def test_03_startVideoA(self):
        '''开始'''
        driver.find_element_by_css_selector(".start-webinar").click()
        windows=driver.window_handles
        driver.switch_to.window(windows[1])
        sleep(2)
        driver.find_element_by_link_text("发起").click()
        driver.switch_to.window(windows[1])
        # 显示等待---
        element = WebDriverWait(driver, 15, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tostart")))
        element.click()
        # driver.find_element_by_css_selector(".tostart").click()
        sleep(12)
        # sleep(32)

#发起问卷--可以跳过此方法
    @unittest.skip("test_04_questionnaire")
    def test_04_questionnaire(self):
        '''发起问卷'''
        driver.find_element_by_css_selector(".mnsurvey").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[11]/div/ul/li[2]/a[4]").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[11]/a").click()
        print("问卷ok")
        sleep(2)
        # # 发起签到
    def test_05_signIn(self):
        '''发起签到'''
        driver.find_element_by_css_selector(".csignin").click()
        sleep(1)
        driver.find_element_by_css_selector(".start-sign-in").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[21]/a").click()
        print("签到ok")
        sleep(2)
        # # 开启问答
    def test_06_QandA(self):
        '''开启问答'''
        driver.find_element_by_css_selector(".QandA").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[26]/div/div[2]/button").click()
        sleep(2)
        print("问答ok")
#开启抽奖
    def test_07_lottery(self):
        '''开启抽奖'''
        driver.find_element_by_css_selector(".lottery").click()
        # driver.find_element_by_xpath("/html/body/div[1]/div[2]/p[3]/input").send_keys("1")
        # driver.find_element_by_xpath("/html/body/div[1]/div[2]/div[3]/a")
        # sleep(1)
        # driver.find_element_by_css_selector(".lottery-end").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/a").click()
        print("抽奖ok")
        sleep(5)

    def test_08_chat(self):
        '''直播时聊天'''
        driver.find_element_by_css_selector(".active-new").click()
        sleep(2)
        for num in range(0,10):
            driver.find_element_by_name("xword").send_keys(num)
            driver.find_element_by_id("sendBt").click()
        sleep(2)

#结束直播
    def test_09_endVideoA(self):
        '''结束直播'''
        driver.find_element_by_css_selector(".toend").click()
        sleep(2)
        driver.switch_to.alert.accept()  #确定结束直播
        sleep(3)
        current_window=driver.current_window_handle
        # all_window=driver.window_handles
        print(current_window)
        # print(all_window)
        # print(driver.title)
        driver.find_element_by_xpath("/html/body/div[22]/div[2]/p[2]/a[1]").click()


if __name__=='__main__':
	unittest.main()