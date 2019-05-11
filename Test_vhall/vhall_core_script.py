from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
#get url
driver.get("********嘉宾端url")
#login
driver.find_element_by_name("account").clear()
driver.find_element_by_name("account").send_keys("****嘉宾账号")
driver.find_element_by_name("password").clear()
driver.find_element_by_name("password").send_keys("****密码")
driver.find_element_by_id("account-to-login").click()
sleep(2)

#open the video activity and click button
#display waiting: Test the element every 0.5s but not more than 10s
element=WebDriverWait(driver,10,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,".tostart")))
element.click()
driver.refresh()
sleep(10)
#end
# driver.find_element_by_css_selector(".tostart toend").click()
# driver.find_element_by_id("live-time").click()
# driver.find_element_by_xpath("/html/body/div[4]/div[1]/div[3]/div[2]/div/a[2]").click()
driver.find_element_by_link_text("结束直播").click()
driver.switch_to.alert.accept()
sleep(2)
driver.quit()
