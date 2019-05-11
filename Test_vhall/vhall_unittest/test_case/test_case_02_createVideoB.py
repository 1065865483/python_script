from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from test_01_login import *

#创建视频文档直播
class Test_case_02_createVideoB(Test_StartEnd):
    def test_02_createVideoB(self):
        '''创建视频文档活动'''
        driver.get("****视频文档活动url")
        driver.find_element_by_id("event-title").send_keys("视频文档活动")
        sleep(2)
        driver.find_element_by_id("event-introduce").clear()
        driver.find_element_by_id("event-introduce").send_keys("123456")
        sleep(2)
        driver.find_element_by_css_selector(".video-doc").click()
        # driver.find_element_by_xpath("/html/body/section/div/form/div[2]/div[11]/button").click()
        driver.find_element_by_css_selector(".savebtn").click()
        sleep(2)

    # def test_03_startVideo(self):
    #     '''开始直播'''
    #     driver.find_element_by_css_selector(".start-webinar").click()
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[1])
    #     sleep(2)
    #     driver.find_element_by_link_text("发起直播").click()
    #     driver.switch_to.window(windows[1])
    #     # 显示等待---
    #     element = WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tostart")))
    #     element.click()
    #     sleep(15)

if __name__=='__main__':
	unittest.main()