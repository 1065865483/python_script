from test_case_04_look import *

class Test_case_05_testTools(Test_StartEnd):

    def test_01_signIn(self):
        '''发起签到'''
        driver.find_element_by_css_selector(".csignin").click()
        sleep(1)
        driver.find_element_by_css_selector(".start-sign-in").click()
        sleep(1)
        # driver.find_element_by_xpath("/html/body/div[21]/a").click()
        print("签到ok")

if __name__ == '__main__':
    unittest.main()