# #多维列表
# a=[1,22,3,4,5,]   #一维列表，如一行5列
# #多维，如下三行三列
# multi_dim_a = [[1,2,3],   #第0行
#                [2,3,4],   #第1行
#                [3,4,5]]   #第2行
# print(a[1])
# print(multi_dim_a[2][2])  #第2行第2个数

# #字典-字典比列表具有更多的功能，字典是无序的内容
# #字典以{}表示，且被赋予一个key和一个value
# a_list = [1,2,3,5,4,5,4]  #列表
# d = {'apple':1,'pear':2,'orange':3}  #字典
# d2 = {1:'a',2:'b','c':'d'}  #字典
# print(d['apple'])  #取出字典d中的apple的值
# print('原字典：',d)
# del d['pear']  #删除字典中的pear
# print('删除元素后的字典：',d)
# d['b'] = '20'  #字典中添加元素'b'：20
# print('添加元素后的字典：',d)
#
# #字典可以更多样的呈现，如字典中的元素对应一个字典
# e = {'apple':[1,2,3],'pear':{1:2,3:'a'},'orange':2}
# print(e['pear'][3])

# #import载入模块
# # import time as t  #time模块简称t
# # from time import time,localtime  #导入time中的time和localtime功能
# from time import *  #导入time种的所有功能
#
# print(localtime())
# print(time())