class Math:
    def __init__(self,a,b):  #初始化一个方法
        self.a=int(a)  #强制转换为int型
        self.b=int(b)
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
