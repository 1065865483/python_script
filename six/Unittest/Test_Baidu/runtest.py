import unittest
test_dir="./test_case" #当前目录下的test_case文件夹(./ 表示当前目录)

discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")
if __name__ == "__main__":
    runer=unittest.TextTestRunner()
    runer.run(discover)