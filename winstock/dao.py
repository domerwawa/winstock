'''
Created on 2016年1月5日

@author: Administrator
'''
from datetime import datetime

class StockInfoDao:
    '''
    classdocs
    '''
    tableName = "stock_info"
    
    def __init__(self, conn):
        self.c = conn.cursor()
    
    def insert(self, stockInfo):
        self.c.execute("insert into " + self.tableName + ''' (
                        stock_code,
                        stock_name,
                        industrial_category,
                        total_market_value,
                        general_capital,
                        circulation_stock,
                        insert_time,
                        update_time) values (?, ?, ?, ?, ?, ?, ? ,?)
                        ''', 
                        [stockInfo.getStockCode(),
                        stockInfo.getStockName(),
                        stockInfo.getIndustrialCategory(),
                        stockInfo.getTotalMarketValue(),
                        stockInfo.getGeneralCapital(),
                        stockInfo.getCirculationStock(),
                        datetime.now(),
                        datetime.now()]
                       )
    
    def update(self, stockInfo):
        self.c.execute("update " + self.tableName + ''' set
                        stock_name = ?,
                        industrial_category = ?,
                        total_market_value = ?,
                        general_capital = ?,
                        circulation_stock = ?,
                        update_time = ?
                        where stock_code = ? ''', 
                        [stockInfo.getStockName(),
                         stockInfo.getIndustrialCategory(),
                         stockInfo.getTotalMarketValue(),
                         stockInfo.getGeneralCapital(),
                         stockInfo.getCirculationStock(),
                         datetime.now(),
                         stockInfo.getStockCode()]
                        )
    
    
    def deleteByKey(self, stockCode):
        self.c.execute("delete from " + self.tableName + " where stock_code = ?", [stockCode])
        
    def getByKey(self, stockCode):
        self.c.execute("select * from " + self.tableName + " where stock_code = ?", [stockCode])
        return self.c.fetchall()
        
    def getAll(self):
        self.c.execute("select * from  " + self.tableName)
        return self.c.fetchall()
    
    def getCountByKey(self, stockCode):
        self.c.execute("select count(1) from " + self.tableName + " where stock_code = ?", [stockCode])
        return self.c.fetchone()[0]
    
class StockPriceDao:
    '''
    classdocs
    '''
    tableName = "stock_price"
    
    def __init__(self, conn):
        self.c = conn.cursor()
    
    def insert(self, stockPrice):
        self.c.execute("insert into " + self.tableName + ''' (
                        stock_code,
                        trade_date,
                        period,
                        open_price,
                        high_price,
                        low_price,
                        close_price,
                        volume,
                        adj_close,
                        insert_time,
                        update_time) values (?, ?, ?, ?, ?, ?, ? ,?, ?, ?, ?)
                        ''', 
                        [stockPrice.getStockCode(),
                        stockPrice.getTradeDate(),
                        stockPrice.getPeriod(),
                        stockPrice.getOpenPrice(),
                        stockPrice.getHighPrice(),
                        stockPrice.getLowPrice(),
                        stockPrice.getClosePrice(),
                        stockPrice.getVolume(),
                        stockPrice.getAdjClose(),
                        datetime.now(),
                        datetime.now()]
                       )
    
    def update(self, stockPrice):
        self.c.execute("update " + self.tableName + ''' set
                        open_price = ?,
                        high_price = ?,
                        low_price = ?,
                        close_price = ?,
                        volume = ?,
                        adj_close = ?,
                        update_time = ?
                        where stock_code = ? and
                        trade_date = ? and
                        period = ?''', 
                        [stockPrice.getOpenPrice(),
                         stockPrice.getHighPrice(),
                         stockPrice.getLowPrice(),
                         stockPrice.getClosePrice(),
                         stockPrice.getVolume(),
                         stockPrice.getAdjClose(),
                         datetime.now(),
                         stockPrice.getStockCode(),
                         stockPrice.getTradeDate(),
                         stockPrice.getPeriod()]
                        )
    
    
    def deleteByKey(self, stockPrice):
        self.c.execute("delete from " + self.tableName + ''' where stock_code = ? and
        trade_date = ? and
        period = ? ''', 
        [stockPrice.getStockCode(), 
        stockPrice.getTradeDate(), 
        stockPrice.getPeriod()])
        
    def getByKey(self, stockPrice):
        self.c.execute("select * from " + self.tableName + ''' where stock_code = ? and
        trade_date = ? and
        period = ? ''', 
        [stockPrice.getStockCode(), 
        stockPrice.getTradeDate(), 
        stockPrice.getPeriod()])
        return self.c.fetchall()
        
    def getAll(self):
        self.c.execute("select * from  " + self.tableName)
        return self.c.fetchall()
    
    def getCountByKey(self, stockPrice):
        self.c.execute("select count(1) from " + self.tableName + ''' where stock_code = ? and 
        trade_date = ? and
        period = ? ''', 
        [stockPrice.getStockCode(), 
        stockPrice.getTradeDate(), 
        stockPrice.getPeriod()])
        return self.c.fetchone()[0]
    