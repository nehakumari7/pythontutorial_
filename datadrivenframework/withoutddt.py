import unittest

class Testcases1(unittest.TestCase):
    def test_1(self):
        li=[2,3,8,4,5]
        for i in li:
            self.assertGreater(7,i)
