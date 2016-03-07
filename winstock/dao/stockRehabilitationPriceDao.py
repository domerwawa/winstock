'''
Created on 2016年3月6日

@author: Adams Zhou
'''
from datetime import datetime

class StockRehabilitationPriceDao:
    '''
    classdocs
    '''
    tableName = "stock_rehabilitation_price"
    
    def __init__(self, conn):
        self.c = conn.cursor()
    
    def insert(self, stockRehabilitationPrice):
        self.c.execute("insert into " + self.tableName + ''' (
                        stock_code,
                        trade_date,
                        open,
                        high,
                        low,
                        close,
                        volume,
                        amount,
                        insert_time,
                        update_time) values (?, ?, ?, ?, ?, ?, ? ,?, ?, ?)
                        ''', 
                        [stockRehabilitationPrice.getStockCode(),
                        stockRehabilitationPrice.getTradeDate(),
                        stockRehabilitationPrice.getOpen(),
                        stockRehabilitationPrice.getHigh(),
                        stockRehabilitationPrice.getLow(),
                        stockRehabilitationPrice.getClose(),
                        stockRehabilitationPrice.getVolume(),
                        stockRehabilitationPrice.getAmount(),
                        datetime.now(),
                        datetime.now()]
                       )
    
    def update(self, stockRehabilitationPrice):
        self.c.execute("update " + self.tableName + ''' set
                        open = ?,
                        high = ?,
                        low = ?,
                        close = ?,
                        volume = ?,
                        amount = ?,
                        update_time = ?
                        where stock_code = ? and
                        trade_date = ? ''', 
                        [stockRehabilitationPrice.getOpen(),
                         stockRehabilitationPrice.getHigh(),
                         stockRehabilitationPrice.getLow(),
                         stockRehabilitationPrice.getClose(),
                         stockRehabilitationPrice.getVolume(),
                         stockRehabilitationPrice.getAmount(),
                         datetime.now(),
                         stockRehabilitationPrice.getStockCode(),
                         stockRehabilitationPrice.getTradeDate()]
                        )
    
    
    def deleteByKey(self, stockRehabilitationPrice):
        self.c.execute("delete from " + self.tableName + ''' where stock_code = ? and
        trade_date = ? ''', 
        [stockRehabilitationPrice.getStockCode(), 
        stockRehabilitationPrice.getTradeDate()])
        
    def getByKey(self, stockRehabilitationPrice):
        self.c.execute("select * from " + self.tableName + ''' where stock_code = ? and
        trade_date = ? ''', 
        [stockRehabilitationPrice.getStockCode(), 
        stockRehabilitationPrice.getTradeDate()])
        return self.c.fetchall()
        
    def getAll(self):
        self.c.execute("select * from  " + self.tableName)
        return self.c.fetchall()
    
    def getCountByKey(self, stockRehabilitationPrice):
        self.c.execute("select count(1) from " + self.tableName + ''' where stock_code = ? and 
        trade_date = ? ''', 
        [stockRehabilitationPrice.getStockCode(), 
        stockRehabilitationPrice.getTradeDate()])
        return self.c.fetchone()[0]
    