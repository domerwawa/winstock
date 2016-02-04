'''
Created on 2016年2月4日

@author: Adams Zhou
'''

class StockPrice:
    
    stockCode = None
    tradeDate = None
    period = None
    openPrice = None
    highPrice = None
    lowPrice = None
    closePrice = None
    volume = None
    adjClose = None
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
    
    def setPeriod(self, period):
        self.period = period
        
    def getPeriod(self):
        return self.period
    
    def setOpenPrice(self, openPrice):
        self.openPrice = openPrice
    
    def getOpenPrice(self):
        return self.openPrice
    
    def setHighPrice(self, highPrice):
        self.highPrice = highPrice
    
    def getHighPrice(self):
        return self.highPrice
    
    def setLowPrice(self, lowPrice):
        self.lowPrice = lowPrice
    
    def getLowPrice(self):
        return self.lowPrice
    
    def setClosePrice(self, closePrice):
        self.closePrice = closePrice
    
    def getClosePrice(self):
        return self.closePrice
    
    def setVolume(self, volume):
        self.volume = volume
    
    def getVolume(self):
        return self.volume
    
    def setAdjClose(self, adjClose):
        self.adjClose = adjClose
    
    def getAdjClose(self):
        return self.adjClose
    
    def setInsertTime(self, insertTime):
        self.insertTime = insertTime
    
    def getInsertTime(self):
        return self.insertTime
    
    def setUpdateTime(self, updateTime):
        self.updateTime = updateTime
    
    def getUpdateTime(self):
        return self.updateTime
    
    
    def toString(self):
        return "stockCode:[{}],tradeDate:[{}],period:[{}],openPrice:[{}],highPrice:[{}],lowPrice:[{}],closePrice:[{}],volume:[{}],adjClose:[{}],insertTime:[{}],updateTime:[{}]".format(
                self.stockCode, 
                self.tradeDate,
                self.period,
                self.openPrice,
                self.highPrice,
                self.lowPrice,
                self.closePrice,
                self.volume,
                self.adjClose,
                self.insertTime,
                self.updateTime)
    