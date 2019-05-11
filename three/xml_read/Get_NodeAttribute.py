from xml.dom import minidom

dom=minidom.parse('class_info.xml')
root=dom.documentElement

#获取login标签的username属性
for i in range(2):
    logins = root.getElementsByTagName('login')
    username = logins[i].getAttribute('username')
    print(username)
    password = logins[i].getAttribute('password')
    print(password)
