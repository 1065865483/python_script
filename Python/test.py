# #定义自变量
# a = 1
# b = a*2
# c = 1
#
# print(a,b,c)
#
# #循环语句
# con=1
# while con <10:
#     print(con)
#     con=con+1

# while True:
#     print(' I\'m true ')

# example_list = [1,2,3,4,5,6,99,3,2,2,23,2332]
example_list = {1,2,3,4,5,6,99,3,2,2,23,2332}
for i in example_list:
    # print('1')
  # print(i)
    print(i)
    print(example_list.count('i'))

# for i in range(1,5):
#     print(i)
#     print('inner of for')
# print('outer of for')

# for i in range(1,10,2):
#     print(i)

# x=1
# y=2
# z =3
# if x<y<z:
#     print("x is more than y")

# x=2
# y=2
# z=3
# if x>2:
#     print('x>2')
# elif x<2:
#     print('x<2')
# else:
#     print('x=2')

# def count():
#     a=1
#     b=2
#     c=a+b
#     print(c)
#
# def count1(a,b):
#     c=a+b
#     print(c)

# def function():
#     print("this is a function")
#     a=1+2
#     print(a)
#
# function()

# def function(a,b):
#     c=a*b
#     print('the c is',c)
#
# function(2,4)

# def fun():
#     a=10
#     print(a)
#     return a +100
# print(fun())

# APPLE=100  #全局变量
# a=None
# def fun():
#     global a
#     a = 20
#     return a+100
#
# print(APPLE) #全局变量能打印
# print('a past=',a)
# # print(a)  #局部变量不能打印
# print(fun())
# print('a now =',a)

# text = 'this is my first test.\nThis is next line.\nThis is the last line '
# append_text = '\nThis is appended file.'  #要追加的内容
# my_file = open('my file.txt','a')  #以追加形式打开文件
# my_file.write(append_text)
# my_file.close()

# file = open('my file.txt','r') #以读文件的形式打开文件
# content = file.readline()  #仅读取第一行
# content = file.readlines()  #读取所有行，并以列表形式存储
# print(content)


# class Calculator:
#     def __init__(self,name,price,high,width,weight):
#         self.name = name
#         self.price = price
#         self.high = high
#         self.wi = width
#         self.we = weight
#     def add(self,x,y):
#         result_add = x+y
#         print('result_add =',result_add)
#     def minus(self,x,y):
#         result = x-y
#         print(result)
#     def times(self,x,y):
#         result =x*y
#         print(result)
#     def divide(self,x,y):
#         print(x/y)
        
# calcul=Calculator()
# print('name:',calcul.name)
# print('price:',calcul.price)
# calcul.add(15,10)
# calcul.minus(15,10)
# calcul.times(15,10)
# calcul.divide(15,10)

# c=Calculator('Good Calculator',12,30,34,50)
# print(c.name)
# c.name='bad Calculator'
# print(c.name)
# c.add(10,20)

