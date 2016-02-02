'''
Created on 2016年1月7日

@author: Administrator
'''
import unittest
import os
from winstock.utils import PropertiesUtils, Sqlite3DbUtils
from winstock.model import StockInfo
from winstock.service import StockInfoService
from winstock.model import StockPrice
from winstock.service import StockPriceService
import logging
import logging.config

class TestService(unittest.TestCase):
     
    @classmethod
    def setUpClass(cls):
        
        os.chdir("../")
        #get logger
        logging.config.fileConfig(fname = os.path.realpath("../resources/pylogconfig.ini"))
        
        cls.logger = logging.getLogger("winstock.test.testService")
        
        #get connection
        propUtils = PropertiesUtils()
        propUtils.readResourceFile("../resources/db.properties")
        dbFile = propUtils.getPropertiesValue("sqlite3", "database_file")
        dbUtils = Sqlite3DbUtils()
        dbUtils.readDbFile(dbFile)
        cls.conn = dbUtils.getConnection()
        
        #get service
        cls.stockInfoService = StockInfoService(cls.conn)
        cls.stockPriceService = StockPriceService(cls.conn)
    
    @classmethod
    def tearDownClass(cls):
        cls.conn.close()


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
        
        self.assertEqual(len(self.stockInfoService.getAllStockInfo()), 2785)
        
        self.stockInfoService.deleteStockInfoByKey("111111")
        self.stockInfoService.deleteStockInfoByKey("222222")
        
        self.logger.info("testStockInfoService end")
        
    def testStockPriceService(self):
        self.logger.info("testStockPriceService start")
        stockPrice1 = StockPrice()
        stockPrice1.setStockCode("111111")
        stockPrice1.setTradDate("2010-01-01")
        stockPrice1.setPeriod(1)
        stockPrice1.setOpenPrice(35.34)
        stockPrice1.setHighPrice(743.5)
        stockPrice1.setLowPrice(74.234)
        stockPrice1.setClosePrice(73.23)
        stockPrice1.setVolume(45345)
        stockPrice1.setAdjClose(345.73)
        
        stockPrice2 = StockPrice()
        stockPrice2.setStockCode("111111")
        stockPrice2.setTradDate("2010-01-02")
        stockPrice2.setPeriod(1)
        stockPrice2.setOpenPrice(95.23)
        stockPrice2.setHighPrice(523.63)
        stockPrice2.setLowPrice(52.63)
        stockPrice2.setClosePrice(44.22)
        stockPrice2.setVolume(7545)
        stockPrice2.setAdjClose(35.345)

        stockPriceList = []
        stockPriceList.append(stockPrice1)
        stockPriceList.append(stockPrice2)
        self.stockPriceService.importStockPrice(stockPriceList)
        
        stockPrice2.setStockCode("111111")
        stockPrice2.setTradDate("2010-01-02")
        stockPrice2.setPeriod(1)
        stockPrice2.setOpenPrice(222)
        stockPrice2.setHighPrice(333)
        stockPrice2.setLowPrice(444)
        stockPrice2.setClosePrice(555)
        stockPrice2.setVolume(666)
        stockPrice2.setAdjClose(777)
        self.stockPriceService.updateStockPrice(stockPrice2)
        
        self.assertEqual(len(self.stockPriceService.getAllStockPrice()), 2)
        
        
        stockPrice3 = StockPrice()
        stockPrice3.setStockCode("111111")
        stockPrice3.setTradDate("2010-01-01")
        stockPrice3.setPeriod(1)
        self.stockPriceService.deleteStockPriceByKey(stockPrice3)
        stockPrice3.setTradDate("2010-01-02")
        self.stockPriceService.deleteStockPriceByKey(stockPrice3)
        
        self.logger.info("testStockPriceService end")
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()