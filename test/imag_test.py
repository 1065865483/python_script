# -*- coding: utf-8 -*-
# python+selenium识别验证码
#
import re
import requests
import pytesseract
from selenium import webdriver
from PIL import Image,Image
import time

#
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://higo.flycua.com/hp/html/login.html")
driver.implicitly_wait(30)
# 下面用户名和密码涉及到我个人信息，所以隐藏
driver.find_element_by_name('memberId').send_keys('xxxxxx')
driver.find_element_by_name('password').send_keys('xxxxxx')
# 因为验证码不能一次就正确识别，我加了循环，一直识别，直到登录成功
while True:
       # 清空验证码输入框，因为可能已经识别过一次了，里面有之前识别的错的验证码
    driver.find_element_by_name("verificationCode").clear()
    # 截图或验证码图片保存地址
    screenImg = "H:\screenImg.png"
    # 浏览器页面截屏
    driver.get_screenshot_as_file(screenImg)
    # 定位验证码位置及大小
    location = driver.find_element_by_name('authImage').location
    size = driver.find_element_by_name('authImage').size
       # 下面四行我都在后面加了数字，理论上是不用加的，但是不加我这截的不是验证码那一块的图，可以看保存的截图，根据截图修改截图位置
    left = location['x'] + 530
    top = location['y'] + 175
    right = location['x'] + size['width'] + 553
    bottom = location['y'] + size['height'] + 200
    # 从文件读取截图，截取验证码位置再次保存
    img = Image.open(screenImg).crop((left, top, right, bottom))
       # 下面对图片做了一些处理，能更好识别一些，相关处理再百度看吧
    img = img.convert('RGBA')  # 转换模式：L | RGB
    img = img.convert('L')  # 转换模式：L | RGB
    img = Image.Contrast(img)  # 增强对比度
    img = img.enhance(2.0)  # 增加饱和度
    img.save(screenImg)
    # 再次读取识别验证码
    img = Image.open(screenImg)
    code = pytesseract.image_to_string(img)
    # 打印识别的验证码
    # print(code.strip())

    # 识别出来验证码去特殊符号，用到了正则表达式，这是我第一次用，之前也没研究过，所以用的可能粗糙，请见谅
    b = ''
    for i in code.strip():
        pattern = re.compile(r'[a-zA-Z0-9]')
        m = pattern.search(i)
        if m != None:
            b += i
    # 输出去特殊符号以后的验证码
    print(b)
    # 把b的值输入验证码输入框
    driver.find_element_by_name("verificationCode").send_keys(b)
       # 点击登录按钮
    driver.find_element_by_class_name('login-form-btn-submit').click()
       # 定时等待5秒，如果验证码识别错误，提示验证码错误需要等一会儿才能继续操作
    time.sleep(5)
       # 获取cookie，并把cookie转化为字符串格式
    cookie1 = str(driver.get_cookies())
    print(cookie1)
    # 第二次用正则表达式，同样有点粗糙，代码实现的功能就是看cookie里是否有tokenId这个词，如果有说明登录成功，跳出循环，可以进行后面的自动化操作，如果没有，则表示登录失败，继续识别验证码
    matchObj = re.search(r'tokenId', cookie1, re.M | re.I)
    if matchObj:
        print(matchObj.group())
        break
    else:
        print("No match!!")
    print('结束')
