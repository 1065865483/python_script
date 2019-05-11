from selenium import webdriver

driver=webdriver.Firefox()

driver.get('https://www.baidu.com/')
driver.find_element_by_xpath(".//*[@id='kw']").send_keys("python")
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("python")
driver.find_element_by_id("su").click()


