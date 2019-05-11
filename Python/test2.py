#input输入
# a_input = input('Plese give a number：') #return a strng '1'
# # a_input = int(input('Plese give a number：')) #或将其转化为数字
# print('This input number is：',a_input)
# if a_input == '1':
#     print('This is a good one')
# elif a_input == str(2):
#     print('See you next time')
# else:
#     print('Good Luck')

# welcome_input = input("Please input -Welcome to zhuanzhuan:")
# # print('the input content is:',welcome_input)
# if welcome_input == 'Welcome to zhuanzhuan':
#     print('Nice to meet you')
# else:
#     print("Please input -'Welcom to my zhuanzhuan'agin:")


# #元组和列表-都是一串有顺序的数字
# a_tuple = (12,3,4,15,6)
# a_list = [12,3,67,7,88]
# for index in range(len(a_list)): #list也可替换为元组
# # for index in range(len(a_tuple)):
# #     range(5)  #生成从0到4的迭代器 index就被赋予了0-4的值
#               #如len(a_list)长度就是5
#     print('index=',index,',number in list=',a_list[index])
#     # print(a_list[index])
#     if a_list[index] == 7:
#         print('7的下标为：',index)
    # print(a_list[1])

a_list = [12,3,67,7,88]
for index in range(len(a_list)):
    print('index=',index,',num in list =',a_list[index])
    if a_list[index] == 7:
        print('7在队列的第',index+1,'位')


#
# for index in range(len(a_tuple)): #
#     range(5)  #生成从0到4的迭代器 index就被赋予了0-4的值
#               #如len(a_list)长度就是5
#     print('index=',index,',number in list=',a_list[index])
    # print(a_list[1])

# a = [1,2,3,4,0,4,3,2,90]
# a.append(44) #在列表的最后面追加数值44
# a.insert(1,0)  #在列表的第一位添加0
# a.remove(3) #remove列表第一次出现的3
# print(a)
# print(a[-1]) #打印python的最后一位
# print(a[0:3]) #打印列表的前三位
# print(a[3:5]) #打印列表的第三位和第四位
# print(a[-3:]) #打印列表的最后三位
# print(a.index(2)) #打印第一次出现2的索引
# print(a.count(4)) #打印列表中出现4的次数
# a.sort()  #从小到大排序
# print(a)
# a.sort(reverse=True)  #从大到小排序
# print(a)

