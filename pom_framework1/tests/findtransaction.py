import unittest
from pom_framework1.Base.BaseTest import BaseTest
from pom_framework1.pages.homepage import HomePage

class Findtransaction(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        base=BaseTest("Chrome","http://zero.webappsecurity.com")
        home=HomePage(base.driver)
        home.click_signin()

    def setUp(self):
        pass

    def testfindtransaction(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass
