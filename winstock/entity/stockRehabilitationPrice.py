'''
Created on 2016年3月7日

@author: Administrator
'''

class StockRehabilitationPrice:
    '''
    classdocs
    '''
    stockCode = None
    tradeDate = None
    open = None
    high = None
    low = None
    close = None
    volume = None
    amount = None
    insertTime = None
    updateTime = None
    
    def setStockCode(self, stockCode):
        self.stockCode = stockCode
        
    def getStockCode(self):
        return self.stockCode
    
    def setTradDate(self, tradeDate):
        self.tradeDate = tradeDate
        
    def getTradeDate(self):
        return self.tradeDate
    
    def setOpen(self, open):
        self.openPrice = open
    
    def getOpen(self):
        return self.open
    
    def setHigh(self, high):
        self.high = high
    
    def getHigh(self):
        return self.high
    
    def setLow(self, low):
        self.low = low
    
    def getLow(self):
        return self.low
    
    def setClose(self, close):
        self.close = close
    
    def getClose(self):
        return self.close
    
    def setVolume(self, volume):
        self.volume = volume
    
    def getVolume(self):
        return self.volume
    
    def setAmount(self, amount):
        self.amount = amount
    
    def getAmount(self):
        return self.amount
    
    def setInsertTime(self, insertTime):
        self.insertTime = insertTime
    
    def getInsertTime(self):
        return self.insertTime
    
    def setUpdateTime(self, updateTime):
        self.updateTime = updateTime
    
    def getUpdateTime(self):
        return self.updateTime
    
    
    def toString(self):
        return "stockCode:[{}],tradeDate:[{}],open:[{}],high:[{}],low:[{}],close:[{}],volume:[{}],amount:[{}],insertTime:[{}],updateTime:[{}]".format(
                self.stockCode, 
                self.tradeDate,
                self.open,
                self.high,
                self.low,
                self.close,
                self.volume,
                self.amount,
                self.insertTime,
                self.updateTime)
    