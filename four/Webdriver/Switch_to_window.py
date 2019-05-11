from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net/list.aspx?cid=615")
sleep(2)
#获取课程主页的窗口句柄
selenium_index=driver.current_window_handle
driver.find_element_by_partial_link_text("2-1").click()
sleep(2)
#跳转到课程主页窗口
driver.switch_to.window(selenium_index)
sleep(3)
driver.find_element_by_partial_link_text("3-1").click()
driver.quit()