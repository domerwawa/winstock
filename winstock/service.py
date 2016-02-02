'''
Created on 2016年1月7日

@author: Administrator
'''
from winstock.dao import StockInfoDao
import logging
import logging.config

class StockInfoService:
    def __init__(self, conn):
        self.logger = logging.getLogger("winstock.service.StockInfoService")
        self.stockInfoDao = StockInfoDao(conn)
        self.conn = conn
    
    def importStockInfo(self, stockInfoList):
        self.logger.info("StockInfoService.importStockInfo start")
        try:
            for stockInfo in stockInfoList:
                
                count = self.stockInfoDao.getCountByKey(stockInfo.getStockCode())
                
                if count == 0:
                    self.logger.info("insert")
                    self.stockInfoDao.insert(stockInfo)
                else:
                    self.logger.info("update")
                    self.stockInfoDao.update(stockInfo)
        except Exception as ex:
            self.logger.error(ex)
            self.conn.rollback()
            
        self.conn.commit()
        self.logger.info("StockInfoService.importStockInfo end")
        
    def updateStockInfo(self, stockInfo):
        self.stockInfoDao.update(stockInfo)
        self.conn.commit()
        
    def deleteStockInfoByKey(self, stockCode):
        self.stockInfoDao.deleteByKey(stockCode)
        self.conn.commit()
        
    def getStockInfoByKey(self, stockCode):
        return self.stockInfoDao.getByKey(stockCode)
    
    def getAllStockInfo(self):
        return self.stockInfoDao.getAll()
    
from winstock.dao import StockPriceDao

class StockPriceService:
    def __init__(self, conn):
        self.logger = logging.getLogger("winstock.service.StockPriceService")
        self.stockPriceDao = StockPriceDao(conn)
        self.conn = conn
    
    def importStockPrice(self, stockPriceList):
        self.logger.info("StockPriceService.importStockPrice start")
        try:
            for stockPrice in stockPriceList:
                
                count = self.stockPriceDao.getCountByKey(stockPrice)
                
                if count == 0:
                    self.logger.info("insert")
                    self.stockPriceDao.insert(stockPrice)
                else:
                    self.logger.info("update")
                    self.stockPriceDao.update(stockPrice)
        except Exception as ex:
            self.logger.error(ex)
            self.conn.rollback()
            
        self.conn.commit()
        self.logger.info("StockPriceService.importStockPrice end")
        
    def updateStockPrice(self, stockPrice):
        self.stockPriceDao.update(stockPrice)
        self.conn.commit()
        
    def deleteStockPriceByKey(self, stockCode):
        self.stockPriceDao.deleteByKey(stockCode)
        self.conn.commit()
        
    def getStockPriceByKey(self, stockPrice):
        return self.stockPriceDao.getByKey(stockPrice)
    
    def getAllStockPrice(self):
        return self.stockPriceDao.getAll()
    