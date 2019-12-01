import unittest
from ddt import ddt,file_data

@ddt

class Testcase1(unittest.TestCase):

    @file_data("testdata.json")
    def test_1(self,username,password):
        print(username,password)