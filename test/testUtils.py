'''
Created on 2016年1月5日

@author: Administrator
'''
import unittest
import winstock
import os

class Test(unittest.TestCase):


    def setUp(self):
        self.propUtils = winstock.PropUtils()

    def tearDown(self):
        pass


    def testPropertiesUtils(self):
        self.propUtils.readResourceFile("../resources/db.properties")
        self.assertEqual("../sqlite3/winstock.db", self.propUtils.getPropertiesValue("sqlite3", "database_file"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()