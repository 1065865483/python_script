from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case_02_createVideoB import *

#
class Test_case_03_test(Test_StartEnd):
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
        sleep(5)


            # sleep(2)

    #     # 结束直播
    # def test_04_endVideo(self):
    #     '''结束直播'''
    #     driver.find_element_by_css_selector(".toend").click()
    #     sleep(2)
    #     driver.switch_to.alert.accept()  # 确定结束直播
    #     sleep(3)
    #     current_window = driver.current_window_handle
    #     # all_window=driver.window_handles
    #     print(current_window)
    #     # print(all_window)
    #     # print(driver.title)
    #     driver.find_element_by_xpath("/html/body/div[22]/div[2]/p[2]/a[1]").click()


if __name__ == '__main__':
    unittest.main()