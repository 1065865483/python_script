from selenium import webdriver
from time import sleep

driver=webdriver.Firefox()
#设置网页文件路径，r代表路径转义
file_path=r'E:\0python_script\four\Webdriver\Frame.html'
#路径转义另一种方法
# file_path='E:\\0python_script\\four\\Webdriver\\Frame.html'
driver.get(file_path)
#切到frame页面内，嵌入页面的id=search
driver.switch_to.frame("search")
#定位到搜索框按钮的关键字
driver.find_element_by_css_selector("#query").send_keys("Python")
driver.find_element_by_css_selector("#stb").click()
sleep(2)
driver.quit()
