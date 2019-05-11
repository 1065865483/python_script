#案例：分别打印出class_info.xml里的学生和老师的详细信息（姓名、年龄、城市）

#导入xml文件
from xml.dom import minidom
#获取标签对的值
#打开文件
dom=minidom.parse('class_info.xml')
#获取文档对象元素
root=dom.documentElement

#根据标签名称获取标签对象
names = root.getElementsByTagName('name')
ages=root.getElementsByTagName('age')
citys=root.getElementsByTagName('city')

#分别打印显示xml文档标签对里面的内容
for i in range(4):
    print(names[0].firstChild.data)
    print(ages[0].firstChild.data)
    print(citys[0].firstChild.data)

