from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select

driver=webdriver.Firefox()
driver.get("http://www.51zxw.net")

#利用select类定位：
select=Select(driver.find_element_by_css_selector("[name='CookieDate']"))

#通过索引选择
select.select_by_index(1)
# 通过可见文字选择
select.select_by_visible_text("留一月")
# 通过value
select.select_by_value('3')

sleep(2)
driver.quit()