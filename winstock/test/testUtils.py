'''
Created on 2016年1月5日

@author: Administrator
'''
import unittest
from winstock import utils

class Test(unittest.TestCase):


    def setUp(self):
        self.propUtils = utils.PropertiesUtils()

    def tearDown(self):
        pass


    def testPropertiesUtils(self):
        self.propUtils.readResourceFile("//resources//db.properties")
        self.assertEqual("winstock", self.propUtils.getPropertiesValue("sqlite3", "db"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()