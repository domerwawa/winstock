'''
Created on 2016年1月5日

@author: Administrator
'''
class StockInfo(object):
    
    stockCode = None
    stockName = None
    industrialCategory = None
    totalMarketValue = None
    generalCapital = None
    circulationStock = None
    insertTime = None
    updateTime = None
    
    def __init__(self):
        self.stockCode = ""
        self.stockName = ""
        self.industrialCategory = 0
        self.totalMarketValue = 0
        self.generalCapital = 0
        self.circulationStock = 0
    
    #need add get set