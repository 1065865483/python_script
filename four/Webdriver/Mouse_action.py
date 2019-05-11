from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
driver.get("https://www.baidu.com/")
driver.maximize_window()
driver.find_element_by_id("kw").send_keys("python")
element=driver.find_element_by_id("kw")
#双击操作
ActionChains(driver).double_click(element).perform()
sleep(2)
#右击鼠标操作
ActionChains(driver).context_click(element).perform()
sleep(2)
#鼠标悬停
above=driver.find_element_by_css_selector(".pf")
ActionChains(driver).move_to_element(above).perform()

sleep(2)
driver.quit()
