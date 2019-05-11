# #错误处理-找不到文件时-创建y or n-打开写入
# try:
#     file = open('eeee','r+')
# except Exception as e:  #接收错误并存储在e这个变量中
#     # print(e)
#     print('There is no file named as eeee')
#     response = input('do you want to create a new file')
#     if response == 'y':
#         file = open('eeee','w')
#     else:
#         pass
# else:
#     file.write('ssss')
# file.close()

# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b)))   #合并为二维数组
# for i,j in zip(a,b):
#     print(i/2,j*2)
# print(list(zip(a,a,b)))  #合并为三维数组

def fun1(x,y):
    return (x+y)
print(fun1(2,3))
# fun2 = lambda x,y:x+y   #用lambda定义简单的方程，一行即可实现
# print(fun2(2,3))
map(fun1,[1],[2])
list(map(fun1,[1],[2]))
print(list(map(fun1,[1],[2])))   #将已知功能用于所给参数的运算，如所给1和2运用fun1计算
print(list(map(fun1,[1,3],[2,7])))  #所给参数可以多组同时进行，如1+2；3+7
