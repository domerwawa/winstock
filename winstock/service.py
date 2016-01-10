'''
Created on 2016年1月7日

@author: Administrator
'''
from winstock.dao import StockInfoDao

class StockInfoService(object):
    def __init__(self, conn):
        self.stockInfoDao = StockInfoDao(conn)
        self.conn = conn
    
    def importStockInfo(self, stockInfoList):
        try:
            for stockInfo in stockInfoList:
                print(stockInfo.stockCode)
                count = self.stockInfoDao.getCountByKey(stockInfo.stockCode)
                print(count)
                if count == 0:
                    print("insert")
                    self.stockInfoDao.insert(stockInfo)
                else:
                    print("update")
                    self.stockInfoDao.update(stockInfo)
        except Exception as ex:
            self.conn.rollback()
            
        self.conn.commit()
        
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
    
    