from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case_02_createVideoC import *


class Test_case_03_toolsC(Test_StartEnd):
    #开始直播
    def test_03_startVideo(self):
        '''开始直播'''
        driver.find_element_by_css_selector(".start-webinar").click()
        sleep(2)
        windows = driver.window_handles
        driver.switch_to.window(windows[1])
        element = WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".tostart")))
        sleep(10)
        element.click()
        sleep(5)

    #添加文档
    def test_04_addDocument(self):
        '''添加文档'''
        driver.find_element_by_css_selector(".doc-fun-btn").click()
        sleep(5)
        # driver.find_element_by_css_selector(".newhost-addDoc").click()
        # sleep(5)
        # driver.find_element_by_xpath("/html/body/div[7]/div/ul/li[2]/div[4]").click()
        # sleep(5)

    # 插件-抽奖
    def test_05_lottery(self):
        '''抽奖'''
        above=driver.find_element_by_css_selector(".funlist-plugin")
        ActionChains(driver).move_to_element(above).perform()
        sleep(1)
        driver.find_element_by_css_selector(".sublist-lottery").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div[1]/a").click()
        sleep(2)

    #插件-签到
    def test_06_lottery(self):
        '''签到'''
        above=driver.find_element_by_css_selector(".funlist-plugin")
        ActionChains(driver).move_to_element(above).perform()
        sleep(1)
        driver.find_element_by_css_selector(".sublist-sign").click()
        sleep(1)
        driver.find_element_by_css_selector(".start-sign-in")
        sleep(5)
        driver.find_element_by_xpath("/html/body/div[19]/a").click()
        sleep(2)

    #插件-问卷
    def test_07_questionnaire(self):
        '''问卷'''
        above=driver.find_element_by_css_selector(".funlist-plugin")
        ActionChains(driver).move_to_element(above).perform()
        sleep(1)
        driver.find_element_by_css_selector(".sublist-ques").click()
        sleep(1)
        driver.find_element_by_xpath("/html/body/div[9]/div/ul/li[2]/a[4]")
        sleep(2)
        driver.find_element_by_xpath("/html/body/div[9]/a").click()
        sleep(2)

if __name__ == '__main__':
    unittest.main()