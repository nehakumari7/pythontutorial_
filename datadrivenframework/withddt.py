import unittest
from ddt import ddt,data

@ddt
class TestCase1(unittest.TestCase):

    @data(5,4,9,2,3)
    def test_1(self,i):
        print (i)
        self.assertGreater(7,i)