import unittest
import sys
from datetime import datetime

#setupmodule is one which will execute everytime program is executed
#teardownmodule is one which will execute everytime running the program
#when a set of lines that has to be xecuted everytime before running program it is setup and at the end it is teardown

def setUpModule():
        print("setUpModule")

def tearDownModule():
        print("tearDownModule")

class TestCase1(unittest.TestCase):

        @classmethod
        def setUpClass(inst):
            print("setUpClass")

        def setUp(self):
            print("setUP")

        def test_method1(self):
            print("test method1")
#when aset of test cases that has to be skipped we have to use skip test
        @unittest.skip("Skip Test")
        def test_method2(self):
            print("test method2")

        @unittest.skipUnless(datetime.now().day >= 13, "Not yet delivered")
        def test_method3(self):
            print("test method3")

        @unittest.skipIf(sys.platform != "win32", "Not yet delivered")
        def test_method4(self):
            print("test04")

 #       @unittest.expectedFailure
     #   def test_method5(self):
           # self.assertEqual(33, 27, "not equal")

        def tearDown(self):
            print("tearDown")

        @classmethod
        def tearDownClass(inst):
            print("tearDownClass")

class TestCase3(unittest.TestCase):

        @classmethod
        def setUpClass(cls):
            print("setUpClass")

        @classmethod
        def tearDownClass(cls):
            print("tearDownClass")

        def setUp(self):
            print("setUp")

        def tearDown(self):
            print("teardown")

        def test_1(self):
            print("test1")

        def test_2(self):
            print("test2")

if __name__ == '__main__':
        unittest.main()