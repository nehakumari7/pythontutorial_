import unittest
from ddt import ddt,data,unpack

@ddt
class TestCase1(unittest.TestCase):

    @unpack
    @data(("uname1","pass1"),("uname2","pass2"),("uname3","pass3"))
    def testcase1(self,x,y):
        print(x,y)