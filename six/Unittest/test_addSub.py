from calculator import *
import unittest

#同时对add和sub进行测试
class Test_add(unittest.TestCase):
    def setUp(self):
        print("Test is start")

    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)
        # print("assertEqual ok")
    def test_add1(self):
        j=Math(10,20)
        self.assertEqual(j.add(),30)

    def tearDown(self):
        print("Test end")

class Test_sub(unittest.TestCase):
    def setUp(self):
        print("Test is start")
    def test_sub(self):
        i=Math(5,5)
        self.assertEqual(i.sub(),0)
        print("assertEqual is ok")
    def test_sub1(self):
        i=Math(6,5)
        self.assertEqual(i.sub(),1)
    def tearDown(self):
        print("Test end")

if __name__=='__main__':
    suite=unittest.TestSuite()
    suite.addTest(Test_add("test_add"))
    suite.addTest(Test_add("test_add1"))
    suite.addTest(Test_add("test_sub"))
    suite.addTest(Test_add("test_sub1"))
    runner=unittest.TextTestRunner()
    runner.run(suite)