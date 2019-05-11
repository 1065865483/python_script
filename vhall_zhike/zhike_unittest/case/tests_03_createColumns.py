from tests_02_createSubjects import *

class Tests_03_CreateColumns(StartEnd):
    #切换至专栏
    def tests_03_changeToColumns(self):
        driver.find_element_by_class_name('v-my-column').click()
        sleep(2)
    #创建专栏
    def tests_04_changeToColumns(self):
        '''创建专栏'''
        for i in range(0,3):
            driver.find_element_by_xpath('/html/body/div[2]/div[5]/ul/li/span').click()
            sleep(0.3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[1]/div[1]/img').click()
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[1]/ul/li[2]/div[1]/img').click()
            sleep(0.3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/a[1]').click()
            sleep(0.3)
            driver.find_element_by_class_name("v-class-name").send_keys('专栏',i)
            sleep(0.3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[3]/div[3]/a[1]').click()
            sleep(0.3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[2]/a[1]').click()
            sleep(0.3)
            driver.find_element_by_xpath('/html/body/div[3]/div/div/div[1]/button').click()
            sleep(0.5)

if __name__=='__main__':
    unittest.main()