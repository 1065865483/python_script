from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case_02_createVideoB import *

class Test_case_03_toolsAB(Test_StartEnd):
    # 开播视频
    def test_03_startVideo(self):
        '''开始直播'''
        driver.find_element_by_css_selector(".start-webinar").click()
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        sleep(2)
        driver.find_element_by_link_text("发起直播").click()
        driver.switch_to.window(windows[1])
        # 显示等待---
        element = WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tostart")))
        element.click()
        sleep(15)
        driver.find_element_by_css_selector(".tostart").click()
        sleep(32)

        # 发起问卷
    @unittest.skip("skip test_04_questionnaire")
    def test_04_questionnaire(self):
        '''发起问卷'''
        driver.find_element_by_css_selector(".mnsurvey").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[12]/div/ul/li[2]/a[4]").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[11]/a").click()
        print("问卷ok")
        sleep(2)


        # # 发起签到
    # @unittest.skip("skip test_05_signIn")
    def test_05_signIn(self):
        '''发起签到'''
        driver.find_element_by_css_selector(".csignin").click()
        sleep(1)
        driver.find_element_by_css_selector(".start-sign-in").click()
        sleep(3)
        driver.find_element_by_xpath("/html/body/div[22]/a").click()

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

        # 开启抽奖
    # @unittest.skip("skip test_07_lottery")
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

    # def test_08_chat(self):
    #     '''直播时聊天'''
    #     driver.find_element_by_css_selector(".active-new").click()
    #     sleep(2)
    #     for num in range(0, 10):
    #         driver.find_element_by_name("xword").send_keys(num)
    #         driver.find_element_by_id("sendBt").click()
    #     sleep(2)

        # 结束直播
    def test_09_endVideo(self):
        '''结束直播'''
        driver.find_element_by_css_selector(".toend").click()
        sleep(2)
        driver.switch_to.alert.accept()  # 确定结束直播
        sleep(3)
        current_window = driver.current_window_handle
        # all_window=driver.window_handles
        print(current_window)
        # print(all_window)
        # print(driver.title)
        driver.find_element_by_xpath("/html/body/div[22]/div[2]/p[2]/a[1]").click()


if __name__ == '__main__':
    unittest.main()