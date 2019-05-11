from calculator import Math
import unittest

class TestMath(unittest.TestCase):
    #测试准备
    def setUp(self):
        print("test start")

    #具体去测试方法-判断a==b
    def test_add(self):
        j=Math(5,10)
        self.assertEqual(j.add(),15)
        print('assertEqual is ok')
        # self.assertEqual(j.add(),12)

    #判断a!=b
    def test_add1(self):
        j=Math(5,10)
        self.assertNotEqual(j.add(),12)
        print('assertNotEqual is ok')

    # #判断布尔值真假
    def assertTrue_test(self):
        j=Math(5,10)
        self.assertTrue(j.add()>10)
        print('assertTrue_test is ok')

    def assertIn_test(self):
        self.assertIn("51zxw","hello,51zxw")
        print('assertIn_test is ok')
        # self.assertIn("888","hello,51zxw")

    def assetIs_test(self):
        self.assertIs("51zxw","51zxw")
        print('assertIs is ok')
        # self.assertIs("51","51zxw")

    #测试结束
    def tearDown(self):
        print("test end")

if __name__=='__main__':
    #调用TestSuite将用例整合
    suite=unittest.TestSuite()
    #调用addTest来装载这个方法
    suite.addTest(TestMath("test_add"))
    #调用TextTestRunner，相当于运行器
    runner=unittest.TextTestRunner()
    #运行suite
    runner.run(suite)
