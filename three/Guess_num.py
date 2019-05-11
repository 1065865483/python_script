'''
需求：猜数游戏
思路：
1.生成随机数
2.玩家输入数值
3.判断输入数值的大小
4.输入数字正确，游戏结束
'''

import random
#生成随机数
answer=random.randint(1,100)
print (answer)
#玩家输入数值
n=int(input('Please input num(1-100):'))
#判断输入数值大小
while n!=answer:
    if n>answer:
        n=int(input("num is more,continue:"))
    elif n<answer:
        n=int(input("num is less,continue:"))
#输入数字正确，游戏结束
print('you win the game!')