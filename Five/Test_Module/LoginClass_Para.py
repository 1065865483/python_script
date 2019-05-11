from selenium import webdriver
from time import sleep

class Login():
    def user_login(self,driver,username,password):
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys(username)
        driver.find_element_by_name("password").clear()
        driver.find_element_by_name("password").send_keys(password)
        driver.find_element_by_css_selector(".inputSub").click()

    def user_logot(self,driver):
        driver.find_element_by_link_text("退出").click()
        sleep(2)
        driver.switch_to.alert.accept()
        sleep(2)
        # driver.quit()

# if __name__=='__main__':
#     driver = webdriver.Firefox()
#     driver.get("http://localhost")
#     driver.implicitly_wait(10)  #隐式等待10s
#
#     Login().user_login(driver,)
#     Login().user_logot(driver)
