# import time
import random
from time import sleep

from three.School.Student import Students

# print(time.ctime())
#导入随机数模块显示随机整数
num=random.randint(1,10)
print('num=',num)
sleep(5)
print("Sleep over")

stu1=Students('jack','BeiJing')
stu1.talk()
stu2=Students('harry','ShangHai')
stu2.talk()