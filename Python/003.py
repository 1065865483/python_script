# a_input = input('Please input a number:')
# print('This number is',a_input)

# a_input=int(input('please input a number:'))
# if a_input==1:
#     print('This is a good one')
# elif a_input==2:
#     print('see u next time')
# else:
#     print('good luck')

# myScore = int(input("Please input your score:"))
# if myScore >=90:
#     print('A')
# elif 80<myScore<90:
#     print('B')
# elif 70<myScore<80:
#     print('C')
# else:
#     print('D')
#
# a_tuple = (12, 3, 5, 15 , 6)
# another_tuple = 12, 3, 5, 15 , 6
# print(a_tuple)

# a = [1,2,3,4,1,1,-1]
# print(a.index(2))
# print(a[2])

# a = [1,2,3,4,1,3,4,5,6,1,-1]
# print(a.count(1))
# # print(a.count(a[]))
# re=set(a)
# print(re)
# for i in re:
#     print(i,'出现次数：',a.count(i))
#     a_list = [a.count(i)]

# a={1, 2, 3, 4, 5, 6, -1}
# print(a[0])

# a_list = [1,2,3,4,5,6,7,8]
# d1 = {'apple':1, 'pear':2, 'orange':3}
# d2 = {1:'a', 2:'b', 3:'c'}
# d3 = {1:'a', 'b':2, 'c':3}
#
# print(d1['apple'])  # 1
# print(a_list[0])    # 1
#
# del d1['pear']  #删除字典中的元素
# print(d1)   # {'orange': 3, 'apple': 1}
#
# d1['b'] = 20   #在字典中插入元素
# print(d1)   # {'orange': 3, 'b': 20, 'pear': 2, 'apple': 1}

# def func():
#     return 0
#
# d4 = {'apple':[1,2,3], 'pear':{1:3, 3:'a'}, 'orange':func}
# print(d4['pear'][3])    # a
# print(d4['orange'][func()])    # a

# lists = [5,3,2]
# count = len(lists)
# for i in range(0, count):
#     for j in range(i + 1, count):
#         if lists[i] > lists[j]:
#             lists[i], lists[j] = lists[j], lists[i]
#             # return lists
#             print(lists)
#             print(i)
#             print(j)
# print(lists)

#冒泡排序
lists = [6,3,2,7,5,9,8,1,4]
for i in range(len(lists)-1):
    for j in range(len(lists)-1-i):
        if lists[j] >lists[j+1]:
            lists[j], lists[j+1] = lists[j+1], lists[j]
            # print(lists)
print(lists)
