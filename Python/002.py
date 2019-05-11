# def sale_car(price,color='red',brand='carmy',is_second_hand=True):
#     print(
#         'price:',price,
#         ',color:',color,
#         ',brand:',brand,
#         ',is_second_hand:',is_second_hand,
#     )
#
# # sale_car(100,'red','carmy',True)   #100为新参数，其余参数为函数默认参数
# # sale_car(200,'green','HimCar',True)  #打印新定义参数
#
# if __name__ =='__main__':
#     sale_car(200, 'green', 'HimCar', True)  # 打印新定义参数

#可变参数
# def report(name,*grades):
#     total_grade = 0
#     for grade in grades:
#         total_grade += grade
#         print(grade)
#     print(name,'total grade is',total_grade)
#
# report('cxl',4,5,6)

# #关键字参数
# def portrat(name,**kw):
#     print('name is',name)
#     for k,v in kw.items():
#         print(k,v)
#
# portrat('mike',age = 24,country='China',education='bachelor')

# def fun():
#     a = 10
#     print(a)
#     return a+100
# print(fun())

# apple = 100 #全局变量
# a = None
# def fun():
#     global a #使用之前在全局里定义的a
#     a = 20
#     return a+100
#
# print(apple)  #100
# print('a past.',a) #None
# fun()
# print('a now.',a) #20

# text1 = 'This is No.1.This is No.2.This is No.3'
# text2 = 'This is No.1.\nThis is No.2.\nThis is No.3'
# print(text1)  #无换行命令
# print(text2)  #有换行命令

# text='abc'
# my_file1 = open('my file1.txt','w')
# my_file1.write(text)
# my_file1.close()

# append_text = 'This is added'
# my_file1 = open('my file1.txt','w') #'a'=append以增加内容的形式打开
# my_file1.write(append_text)
# my_file1.close()

# file = open('my file1.txt','r')
# content = file.read()
# print(content)

# file = open('my file1.txt','r')
# content = file.readline()
# content2 = file.readline()
# print(content)
# print(content2)

# class Calculator:
#     name = 'Good calculator'
#     price = 18
#     def add(self,x,y):
#         # print(self.name)
#         result = x+y
#         print(result)
#
# cal = Calculator()
# cal.name
# print(cal.name,'1')
# cal.price
# cal.add(10,20)

# class Calculator:
#     name = 'Good calculator'
#     price = 18
#     def __init__(self,name,price,height,width,weight):
#         self.name=name
#         self.price=price
#         self.h=height
#         self.wi=width
#         self.we=weight
#
# c=Calculator('bad cal',15,16,17,18)
# print(c.name)
# print(c)

class Calculator:
    name = 'Good calculator'
    price = 18
    def __init__(self,name,price,height=10,width=14,weight=15):
        self.name=name
        self.price=price
        self.h=height
        self.wi=width
        self.we=weight

c=Calculator('bad cal',5,100)
print(c.name)
print(c.price)
print(c.h)





