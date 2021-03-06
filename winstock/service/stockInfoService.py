'''
Created on 2016年2月4日

@author: Adams Zhou
'''

from winstock.dao.stockInfoDao import StockInfoDao
import logging

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
    