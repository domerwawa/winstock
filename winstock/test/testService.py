'''
Created on 2016年1月7日

@author: Administrator
'''
import unittest
from winstock.utils import PropertiesUtils
from winstock.utils import Sqlite3DbUtils
from winstock.service import StockInfoService
from winstock.model import StockInfo

class TestService(unittest.TestCase):


    def setUp(self):
        #get connection
        propUtils = PropertiesUtils()
        propUtils.readResourceFile("//resources//db.properties")
        dbFile = propUtils.getPropertiesValue("sqlite3", "database_file")
        dbUtils = Sqlite3DbUtils(dbFile)
        self.conn = dbUtils.getConnection()
        #get service
        self.stockInfoService = StockInfoService(self.conn)
        
    def tearDown(self):
        self.conn.close()


    def testStockInfoService(self):
        stockInfo1 = StockInfo()
        stockInfo1.stockCode = "111111"
        stockInfo1.stockName = "远光软件"
        stockInfo1.industrialCategory = "计算机软件"
        stockInfo1.totalMarketValue = 341223
        stockInfo1.generalCapital = 421213
        stockInfo1.circulationStock = 5232
        
        stockInfo2 = StockInfo()
        stockInfo2.stockCode = "222222"
        stockInfo2.stockName = "科大讯飞"
        stockInfo2.industrialCategory = "计算机软件"
        stockInfo2.totalMarketValue = 5224
        stockInfo2.generalCapital = 2522
        stockInfo2.circulationStock = 562
        
        stockInfoList = []
        stockInfoList.append(stockInfo1)
        stockInfoList.append(stockInfo2)
        self.stockInfoService.importStockInfo(stockInfoList)
        
        stockInfo2.stockCode = "222222"
        stockInfo2.stockName = "科大讯飞"
        stockInfo2.industrialCategory = "计算机软件"
        stockInfo2.totalMarketValue = 54563
        stockInfo2.generalCapital = 4234
        stockInfo2.circulationStock = 5234
        self.stockInfoService.updateStockInfo(stockInfo2)
        
        
        self.assertEqual(len(self.stockInfoService.getAllStockInfo()), 2)
        
        self.stockInfoService.deleteStockInfoByKey("111111")
        self.stockInfoService.deleteStockInfoByKey("222222")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()