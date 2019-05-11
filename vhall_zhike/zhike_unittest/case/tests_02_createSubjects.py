import unittest

from tests_01_login import *


@unittest.skip("skip Tests_02_CreateSubjects")
class Tests_02_CreateSubjects(StartEnd):
    # 此界面元素无其他属性，暂用xpath定位元素
    def tests_02_createSubjects(self):
        '''创建课程'''
        for i in range(0,3):
            driver.find_element_by_xpath("/html/body/div[2]/div[5]/ul/li/span").click()
            sleep(0.5)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[1]/ul/li[1]/div[1]/img").click()
            sleep(0.3)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[2]/div[2]/a[1]").click()
            sleep(0.3)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/div[3]/a[1]").click()
            sleep(0.3)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[4]/div[2]/a[1]").click()
            sleep(0.3)
            driver.find_element_by_xpath("/html/body/div[3]/div/div/div[1]/button").click()


if __name__=='__main__':
    unittest.main()


