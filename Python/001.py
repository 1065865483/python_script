# print('apple'+str(4))
# print('apple'+'4')
# print(int(1.3)+4)
# print(1)
# a=1
# while a < 10:
#     print(a)
#     a = a+1
#
# while True:
#     print('I\'m True')

# example_list = [1,2,3,3,4,4,5]
# example_list1 = {1,2,3,3,3,5}
# unique = set(example_list)
# print(unique)
# for i in unique:
#     print(i)
#     print(i,'出现次数：',example_list.count(i))
#     print('inner of for')
# print('outter of for')


# #打印列表中出现次数最多的元素 并打印出现次数
# list_s = [1,2,3,3,3,5,2,1]
# unique = set(list_s)
# print('列表中元素有：',unique)
# # print(list_s.count(5))
# for i in unique:
#     print(i,'出现次数为：',list_s.count(i))

# w =('python',2.7,64)
# for i in w:
#     print(i)

# dic = {}
# dic['lan'] = 'python'
# dic['version'] = '3.5'
# dic['paltform'] = '64'
# for key in dic:
#     print(key,dic[key])
#
# s = set(['python','python5','python3','python'])
# print(s)
# for item in s:
#     print(item)

# #define a Fib class
# class Fib(object):
#     def __init__(self,max):
#         self.max = max
#         self.n,self.a,self.b=0,0,1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.n < self.max:
#             r = self.b
#             self.a,self.b = self.b,self.a+self.b
#             self.n = self.n + 1
#             return r
#         raise StopIteration()
#
# #using  Fib object
# for i in Fib(5):
#     print(i)

# var = 12 if 1<2 else 13
# print(var)

# x = 1
# y = 2
# z = 3
# if x>1:
#     print('x>1')
# elif x<1:
#     print('x<1')
# else:
#     print('x=1')
# print('finish')

# def function():
#     print('This is a function')
#     a = 1+2
#     print(a)
#
# function()

def func(a,b):
    c = a+b
    print('the c is',c)

func(1,2)
