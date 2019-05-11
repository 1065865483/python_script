from calculator import *
import unittest

class Test_StartEnd(unittest.TestCase):
    def setUp(self):
        print("Test is start")
    def tearDown(self):
        print("Test is end")

class Test_add(Test_StartEnd):
    def test_add(self):
        j=Math(5,5)
        self.assertEqual(j.add(),10)
class Test_sub(Test_StartEnd):
    def test_sub(self):
        i=Math(8,7)
        self.assertEqual(i.sub(),1)

if __name__=='__main__':
    unittest.main