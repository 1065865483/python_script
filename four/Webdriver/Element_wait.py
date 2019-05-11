from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.baidu.com/")
driver.find_element_by_css_selector("#kw").send_keys("我要自学网selenium")
sleep(2)
#显示等待---判断搜索按钮是否存在:不超过5s每隔0.5秒检测一次，直到id=su的元素出现
element=WebDriverWait(driver,5,0.1).until(EC.presence_of_element_located((By.ID,"su")))
element.click()
sleep(3)
driver.quit()

