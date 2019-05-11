# # a=1
# # b=a
# # print(a,b)
# #
# # for i in range(1,10,2):
# #     print(i)
#
# def fun():
#     a=10
#     print(a)
#     return a +100
#
# sun = fun()
# # sun + 100
#
# print(fun())
# print(sun)

file = open('my file.txt','r') #以读文件的形式打开文件
# content = file.readline() 仅读取第一行
content = file.readlines() #读取所有行，并以列表形式存储
content[3]
print(content[3])
