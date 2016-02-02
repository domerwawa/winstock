'''
Created on 2016年1月5日

@author: Administrator
'''
class StockInfo:
    
    def setStockCode(self, stockCode):
        self.stockCode = stockCode
    
    def getStockCode(self):
        return self.stockCode
    
    def setStockName(self, stockName):
        self.stockName = stockName
        
    def getStockName(self):
        return self.stockName
    
    def setIndustrialCategory(self, industrialCategory):
        self.industrialCategory = industrialCategory
    
    def getIndustrialCategory(self):
        return self.industrialCategory
    
    def setTotalMarketValue(self, totalMarketValue):
        self.totalMarketValue = totalMarketValue
    
    def getTotalMarketValue(self):
        return self.totalMarketValue
    
    def setGeneralCapital(self, generalCapital):
        self.generalCapital = generalCapital
    
    def getGeneralCapital(self):
        return self.generalCapital
    
    def setCirculationStock(self, circulationStock):
        self.circulationStock = circulationStock
        
    def getCirculationStock(self):
        return self.circulationStock
    
    def setInsertTime(self, insertTime):
        self.insertTime = insertTime
    
    def getInsertTime(self):
        return self.insertTime
    
    def setUpdateTime(self, updateTime):
        self.updateTime = updateTime
    
    def getUpdateTime(self):
        return self.updateTime
    
    def toString(self):
        return "stockCode:[{}],stockName:[{}],industrialCategory:[{}],totalMarketValue:[{}],generalCapital:[{}],circulationStock:[{}],insertTime:[{}],updateTime:[{}]".format(
                self.stockCode, 
                self.stockName,
                self.industrialCategory,
                self.totalMarketValue,
                self.generalCapital,
                self.circulationStock,
                self.insertTime,
                self.updateTime)
    
class StockPrice:
    
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
    
    