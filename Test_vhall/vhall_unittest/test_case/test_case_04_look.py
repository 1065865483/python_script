# import urllib
from test_case_03_test import *
from selenium import webdriver

#概述：从链接1中获取数字，并与连接2拼接
#从主持人链接中获取活动id，并将活动id与固定链接拼接成观看端链接
driver2 = webdriver.Chrome()
# driver2 = webdriver.Firefox()
class Test_case_04_look(Test_StartEnd):

#观看端启动浏览器2进入观看活动
    def test_06_getLookUrl(self):
        print("观看端")
        host_url=driver.current_url
    #方法1-从主持人链接中获取id，然后连接成观看端链接
        # look_id=host_url.split('/')[5:]  #截取host_url中第五个“/”后边的内容,注意截取后是个1个数字的数组
        # look_url='https://t.e.vhall.com/'
        # look_url += look_id[0]   #取数组中的第一个元素（也是唯一元素）

     # 方法2-从主持人链接中获取id，然后连接成观看端链接：
        look_id = host_url.split('/')  #截取host_url，通过“/”截取，注意截取后是个数组，数组中元素个数为：“/”个数+1
        look_url = 'https://t.e.vhall.com/'
        look_url += look_id[len(look_id) - 1] #取look_id中最后一个元素

        print(host_url)
        print(look_url)
        sleep(5)
        driver2.get(look_url)

#观看端登录
    def test_07_lookLogin(self):
        driver2.find_element_by_css_selector(".to-login").click()
        driver2.find_element_by_id("username").send_keys("****观看端账号")
        driver2.find_element_by_id("pwd").send_keys("****对应密码")
        driver2.find_element_by_id("to-login-common").click()
        sleep(2)


    # def test_08_lookSignin(self):
    #     elementSignin = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
    #     print()
    #     if elementSignin:
    #         elementSignin.click()
    #         print("已点击")
    #     else:
    #         print("未弹出签到")


if __name__ == '__main__':
    unittest.main()
