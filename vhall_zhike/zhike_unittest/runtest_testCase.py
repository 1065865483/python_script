import unittest
test_dir="./case" #当前目录下的case文件夹(./ 表示当前目录)

discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
if __name__ == "__main__":
    runer=unittest.TextTestRunner()
    runer.run(discover)