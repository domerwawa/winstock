'''
Created on 2016年1月5日

@author: Administrator
'''
class StockInfo(object):

    def __init__(self, stockCode, stockName, industrialCategory, totalMarketValue, generalCapital, circulationStock): 
        self.stockCode = stockCode
        self.stockName = stockName
        self.industrialCategory = industrialCategory
        self.totalMarketValue = totalMarketValue
        self.generalCapital = generalCapital
        self.circulationStock = circulationStock
    