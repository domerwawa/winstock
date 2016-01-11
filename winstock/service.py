'''
Created on 2016年1月7日

@author: Administrator
'''
from winstock.dao import StockInfoDao
import logging
import logging.config

class StockInfoService(object):
    def __init__(self, conn):
        self.logger = logging.getLogger("winstock.service.StockInfoService")
        self.stockInfoDao = StockInfoDao(conn)
        self.conn = conn
    
    def importStockInfo(self, stockInfoList):
        self.logger.info("StockInfoService.importStockInfo start")
        try:
            for stockInfo in stockInfoList:
                
                count = self.stockInfoDao.getCountByKey(stockInfo.stockCode)
                
                if count == 0:
                    self.stockInfoDao.insert(stockInfo)
                else:
                    self.stockInfoDao.update(stockInfo)
        except Exception as ex:
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
    
    