import unittest

class StartEnd(unittest.TestCase):
    def setUp(self):
        print('test start')
    def tearDown(self):
        print('test end')