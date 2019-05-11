from xml.dom import minidom

dom=minidom.parse("class_info.xml")

root=dom.documentElement

tags=root.getElementsByTagName('student')
print(tags[0].nodeName)
print(tags[0].nodeType)
print(tags[0].nodeValue)