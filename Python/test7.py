# #pickle存放数据
# import pickle
#
# #通过pickle打开并保存文件
# a_dict={'da':111,2:[23,1,4],'23':{1:2,'d':'sad'}}
# file = open('pickle_example.pickle','wb') #以写入二进制形式打开
# pickle.dump(a_dict,file)  #dump文件并将其装载如file中
# file.close()
#
# #通过pickle打开并继续加工文件
# file = open('pickle_example.pickle','rb')  #以读的形式打开
# a_dict = pickle.load(file)  #保存到另一个文件a_dict中
# file.close()
# print(a_dict)
#
# #注意：可以使用with打开，使用with打开后不用自己关闭
# with open('pickle_example.pickle','rb') as file:   #以读的形式打开
#     a_dict = pickle.load(file)  #保存到另一个文件a_dict中
# print(a_dict)

# char_list = ['a','b','c','c','d','d','d']
# print(set(char_list))   #去除重复元素,并重新排序
# print(type(set(char_list)))  #打印列表的类型

# sentence = 'Welcome Back to This Tutorial'
# print(set(sentence))

# char_list = ['a','b','c','c','d','d','d']
# unique_char = set(char_list)  #找出不同的字母并存储
# unique_char.add('x')  #加入元素
# print(unique_char)
# # unique_char.clear()  #清除
# # print(unique_char)  #清除后set打印为空
# print(unique_char.remove('x')) #减掉某个元素-->将返回减掉的元素，即返回None
# print(unique_char)   #重新打印减掉元素后的列表

s = "abcdeaaabbffeeeeccd"
unique = set(s)  #找出不同字母并存储
print(unique)

print('a的个数：',s.count("a"))
print('b的个数：',s.count("b"))


#对比两个列表的不同
# unique_char = {'a','b','c','d'}
# set1 = unique_char
# set2 = {'a','e','i'}
# print(set1.difference(set2))  #打印两个列表不同的地方
# print(set1.intersection(set2))  #打印两个列表相同的部分



