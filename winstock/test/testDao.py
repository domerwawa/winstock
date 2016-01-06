'''
Created on 2016年1月5日

@author: Administrator
'''
import unittest
from winstock.dao import StockInfoDao
from winstock.model import StockInfo

class Test(unittest.TestCase):


    def setUp(self):
        self.stockInfoDao = StockInfoDao()


    def tearDown(self):
        pass


    def testStockInfoDao(self):
        stockInfo = StockInfo()
        stockInfo.stockName = "123456"
        stockInfo.stockCode = "abc"
        stockInfo.industrialCategory = 1
        stockInfo.totalMarketValue = 2
        stockInfo.generalCapital = 3
        stockInfo.circulationStock = 4
        
        self.stockInfoDao.insert(StockInfo)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()