from selenium import webdriver
from time import sleep

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")

#绝对路径定位
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/div[1]/div/form/span[1]/input").send_keys("51zxw")

# a.根据input标签中的id属性定位元素
driver.find_element_by_xpath("//input[@id='kw']").send_keys("51zxw")
# b.根据input标签中name属性定位元素
driver.find_element_by_xpath("//input[@name='wd']").send_keys("51zxw")
# c.根据input标签中class属性定位元素
driver.find_element_by_xpath("//*[@class='s_ipt']").send_keys("51zxw")

driver.find_element_by_id("su").click()
sleep(3)
driver.quit()
