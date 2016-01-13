'''
Created on 2016年1月7日

@author: Administrator
'''
import unittest
import os
from winstock.utils import PropertiesUtils, Sqlite3DbUtils
from winstock.service import StockInfoService
from winstock.model import StockInfo
import logging
import logging.config

class TestService(unittest.TestCase):
     
    def setUp(self):
        
        os.chdir("..//")
        #get logger
        logging.config.fileConfig(fname = os.path.realpath("..//resources//pylogconfig.ini"))
        
        self.logger = logging.getLogger("winstock.test.testService")
        
        #get connection
        propUtils = PropertiesUtils()
        propUtils.readResourceFile("..//resources//db.properties")
        dbFile = propUtils.getPropertiesValue("sqlite3", "database_file")
        dbUtils = Sqlite3DbUtils(dbFile)
        self.conn = dbUtils.getConnection()
        #get service
        self.stockInfoService = StockInfoService(self.conn)
        
    def tearDown(self):
        self.conn.close()


    def testStockInfoService(self):
        self.logger.info("testStockInfoService start")
        stockInfo1 = StockInfo()
        stockInfo1.setStockCode("111111")
        stockInfo1.setStockName("远光软件")
        stockInfo1.setIndustrialCategory("计算机软件")
        stockInfo1.setTotalMarketValue(341223)
        stockInfo1.setGeneralCapital(421213)
        stockInfo1.setCirculationStock(5232)
        
        stockInfo2 = StockInfo()
        stockInfo2.setStockCode("222222")
        stockInfo2.setStockName("科大讯飞")
        stockInfo2.setIndustrialCategory("计算机软件")
        stockInfo2.setTotalMarketValue(5224)
        stockInfo2.setGeneralCapital(2522)
        stockInfo2.setCirculationStock(562)
        
        stockInfoList = []
        stockInfoList.append(stockInfo1)
        stockInfoList.append(stockInfo2)
        self.stockInfoService.importStockInfo(stockInfoList)
        
        stockInfo2.setStockCode("222222")
        stockInfo2.setStockName("科大讯飞")
        stockInfo2.setIndustrialCategory("计算机软件")
        stockInfo2.setTotalMarketValue(54563)
        stockInfo2.setGeneralCapital(4234)
        stockInfo2.setCirculationStock(5234)
        self.stockInfoService.updateStockInfo(stockInfo2)
        
        
        self.assertEqual(len(self.stockInfoService.getAllStockInfo()), 2)
        
        self.stockInfoService.deleteStockInfoByKey("111111")
        self.stockInfoService.deleteStockInfoByKey("222222")
        
        self.logger.info("testStockInfoService end")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()