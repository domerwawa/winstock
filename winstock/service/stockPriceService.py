'''
Created on 2016年2月4日

@author: Adams Zhou
'''
from winstock.dao.stockPriceDao import StockPriceDao
import logging

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
    