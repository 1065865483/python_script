import copy
# a = [1,2,3]
# b = a  #a和b的索引和数值都一样
# print(id(a))  #a在硬盘中所用的索引
# print(id(b))  #b在硬盘中所用的索引
# print(id(a)==id(b))
# c = copy.copy(a)  #浅复制---数值相同;id不同;其中一个列表中的数值变化时另一个不变
# print(id(a)==id(c))
# print(c)
# print(a)
# print(id(a))  #a在硬盘中所用的索引
# print(id(c))  #b在硬盘中所用的索引
# a[1]=33
# print(c)
# print(a)
# print(id(a))  #列表a在硬盘中所用的索引
# print(id(a[2]))  #列表a中第2个元素在硬盘中所用的索引
# print(id(c))  #b在硬盘中所用的索引

# a=[1,2,3,[4,5]]
# b=copy.copy(a)
# print(b)
# a[1]=22   #将列表a中第一个元素改为22
# print(a)
# print(b)  #列表b中此元素没有变化
# a[3][1]=55  #将a列表中第3个元素中的第一个元素改为55
# print(a)
# print(b)   #列表b中的此元素也发生改变

#深复制
# a=[1,2,3,[4,5]]
# e = copy.deepcopy(a)
# print(a)
# print(e)
# print(id(a[2]))
# print(id(e[2]))
# print(id(e[2])==id(a[2]))