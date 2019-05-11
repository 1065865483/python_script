from selenium import webdriver
from time import sleep

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time



driver=webdriver.Firefox()
# driver2=webdriver.Chrome()

# driver1.get("http://news.baidu.com/")
# sleep(3)
# driver2.get("https://www.baidu.com/")

driver.get("https://t.e.vhall.com/319544395")
driver.find_element_by_css_selector(".to-login").click()
driver.find_element_by_id("username").send_keys("v16417541")
driver.find_element_by_id("pwd").send_keys("123456")
driver.find_element_by_id("to-login-common").click()
now1 = time.strftime("%Y-%m-%d %H_%M_%S")
# sleep(5)
# now2 = time.strftime("%Y-%m-%d %H_%M_%S")
print(now1)
# print(now2)







# element1 = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))

# while 1:
#     element1 = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
#
#     if element1:
#         element1.click()
#         print("已点击123")
#     else:
#         driver.quit()
#         print("未弹出签到123")
#     sleep(3)
# try:
#     element1 = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
#     element1.click()
#     print("已点击123")
# except TimeoutException :
#     print("未弹出签到123")

n2=20
for num in range(0,n2):
    try:
        # driver.find_element_by_id("popup-btn-yes").click()
        element1 = WebDriverWait(driver, 1, 0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
        element1.click()
        print("查找1")

    except:
        sleep(1)
        print("休眠1")
else:
    print("未找到1")
    driver.quit()
    print("已结束")

# for num in range(0,20):
#
#     try:
#         element = driver.find_element_by_id("popup-btn-yes")
#         sleep(1)
#         print("未找到")
#     except:
#         print("jixu")
#     # element = driver.find_element_by_id("popup-btn-yes").click()
#     # sleep(1)
#     # print("未找到")
# else:
#     element.click()



# while element1:
#     print("已点击 1")
#     element1 = WebDriverWait(driver, 10, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".popup-btn-yes")))
#     element1.click()
#     print("已点击")
# else:
#     print("未弹出签到")

