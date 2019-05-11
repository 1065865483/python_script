import unittest

test_dir='./'   #此脚本路径下的代码
discovery=unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")  #寻找所有'test'开头，'.py'结尾的代码

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(discovery)