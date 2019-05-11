from tkinter import Image

from selenium import webdriver
from time import sleep


driver=webdriver.Firefox()
# driver=webdriver.Chrome()

##陈新利
driver.maximize_window()
driver.get('')
driver.find_element_by_name('email').clear()
driver.find_element_by_name('email').send_keys('')
driver.find_element_by_name('password').clear()
driver.find_element_by_name('password').send_keys('XXX')

#清空验证码输入框
driver.find_element_by_name('code').clear()
#截图存放位置
screenImg="F:\cxl\script\0python_script\MeiCai\screenImg\screen.png"
#截图
driver.get_screenshot_as_file(r'F:\cxl\script\0python_script\MeiCai\screenImg\screen.png')
# 定位验证码位置及大小
location=driver.find_element_by_id('yw0').location
size=driver.find_element_by_id('yw0').size

left = location['x']
top = location['y']
right = location['x'] + size['width']
bottom = location['y'] + size['height']

# 从文件读取截图，截取验证码位置再次保存

img = Image.open(screenImg).crop((left, top, right, bottom))
#下面对图片做了一些处理，能更好识别一些，相关处理再百度看吧
img = img.convert('RGBA')  # 转换模式：L | RGB
img = img.convert('L')  # 转换模式：L | RGB
# img = ImageEnhance.Contrast(img)  # 增强对比度
img = img.enhance(2.0)  # 增加饱和度
img.save(screenImg)
# 再次读取识别验证码
img = Image.open(screenImg)
code = pytesseract.image_to_string(img)
    #打印识别的验证码
    #print(code.strip())

####
driver.quit()
