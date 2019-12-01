import unittest
from ddt import ddt,data,unpack
from datadrivenframework.readexceldata import getdata

@ddt

class Testcase1(unittest.TestCase):

    @unpack
    @data(*getdata())
    def test_1(self,x,y):
        print(x,y)