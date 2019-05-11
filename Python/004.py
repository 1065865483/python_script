# a=[1,2,3]
# b=[4,5,6]
# ab=zip(a,b)
# print(list(ab))  #需要加list来可视化这个功能

import random

answer = random.randint(0,100)
print(answer)
num = int(input('Please input a num:'))

while num != answer:
    if num>answer:
        num = int(input("your num is more,continue:"))
    elif num<answer:
        num = int(input("your num is less,continue:"))
print('you win the game!')




