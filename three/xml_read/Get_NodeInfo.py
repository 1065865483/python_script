#查看class_info.xml文件里class节点的属性（节点名称、节点的值、节点类型）
from  xml.dom import  minidom

#加载xml
dom = minidom.parse('class_info.xml')
#加载dom对象元素
root=dom.documentElement
#打印节点信息
print(root.nodeName)
print(root.nodeValue)
print(root.nodeType)