'''
Created on 2016年3月7日

@author: Administrator
'''
from winstock.dao.stockRehabilitationPriceDao import StockRehabilitationPriceDao
import logging

class StockRehabilitationPriceService:
    
    def __init__(self, conn):
        self.logger = logging.getLogger("winstock.service.StockRehabilitationPrice")
        self.stockRehabilitationPriceDao = StockRehabilitationPriceDao(conn)
        self.conn = conn
    
    def importStockRehabilitationPrice(self, stockRehabilitationPriceList):
        self.logger.info("StockRehabilitationPrice.importStockRehabilitationPrice start")
        try:
            for stockRehabilitationPrice in stockRehabilitationPriceList:
                
                count = self.stockRehabilitationPriceDao.getCountByKey(stockRehabilitationPrice)
                
                if count == 0:
                    self.logger.info("insert")
                    self.stockRehabilitationPriceDao.insert(stockRehabilitationPrice)
                else:
                    self.logger.info("update")
                    self.stockRehabilitationPriceDao.update(stockRehabilitationPrice)
        except Exception as ex:
            self.logger.error(ex)
            self.conn.rollback()
            
        self.conn.commit()
        self.logger.info("stockRehabilitationPriceService.importStockRehabilitationPrice end")
        
    def updateStockRehabilitationPrice(self, stockRehabilitationPrice):
        self.stockRehabilitationPriceDao.update(stockRehabilitationPrice)
        self.conn.commit()
        
    def deleteStockRehabilitationPriceByKey(self, stockCode):
        self.stockRehabilitationPriceDao.deleteByKey(stockCode)
        self.conn.commit()
        
    def getStockRehabilitationPriceByKey(self, stockRehabilitationPrice):
        return self.stockRehabilitationPriceDao.getByKey(stockRehabilitationPrice)
    
    def getAllstockRehabilitationPrice(self):
        return self.stockRehabilitationPriceDao.getAll()
    