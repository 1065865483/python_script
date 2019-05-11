from test_case_05_testTools import *
import time

now = time.strftime("%Y-%m-%d %H_%M_%S")
class Test_case_06_accept(Test_StartEnd):
    # now = time.strftime("%Y-%m-%d %H_%M_%S")
    def test_01_lookSignin(self):
        print("等待开始",now)
        elementSignin = WebDriverWait(driver, 20, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
        print("等待结束",now)
        if elementSignin:
            elementSignin.click()
            print("已点击")
        else:
            print("未弹出签到")
        driver.quit()

if __name__ == '__main__':
    unittest.main()