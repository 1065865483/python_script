from time import sleep
from test_01_login import *

#创建视频模式活动
class Test_case_02(Test_StartEnd):
    def test_02_createVideoC(self):
        driver.get("****视频模式活动url")
        driver.find_element_by_id("event-title").send_keys("视频模式活动")
        sleep(2)
        driver.find_element_by_id("event-introduce").clear()
        driver.find_element_by_id("event-introduce").send_keys("123456")
        sleep(2)
        driver.find_element_by_css_selector(".newTab ").click()
        #线上环境创建按钮的xpath
        driver.find_element_by_xpath("/html/body/section/div/form/div[2]/div[11]/button").click()
        #测试创建按钮xpath
        # driver.find_element_by_xpath("/html/body/section/div/form/div[2]/div[10]/button").click()

        sleep(2)

if __name__=='__main__':
	unittest.main()
