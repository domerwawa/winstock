'''
Created on 2016年2月4日

@author: Adams Zhou
'''

class StockInfo:
    
    stockCode = None
    stockName = None
    industrialCategory = None
    totalMarketValue = None
    generalCapital = None
    circulationStock = None
    insertTime = None
    updateTime = None

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
    