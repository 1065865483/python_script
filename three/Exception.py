'''
#try...exception
try:
    fileName=input("Please input fileName:")
    open("%r.txt"%fileName)
except FileNotFoundError:
    print("File not found")

#NameError
try:
    stu='jack'
    print(stu)
except NameError:
    print("变量未定义！")

#BaseException
try:
    print(stu)
except BaseException:
    print("变量未定义！")

'''
def division(x,y):
    if y==0:
        raise ZeroDivisionError("Zero is not allow!")
    return x/y
try:
    division(8,0)
except BaseException as msg:
    print(msg)
