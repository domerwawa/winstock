'''
Created on 2016年1月5日

@author: Administrator
'''
from winstock.model import StockInfo
import sqlite3
from winstock.utils import DatabaseUtils
from winstock.utils import PropertiesUtils

class StockInfoDao(object):
    '''
    classdocs
    '''
    def __init__(self, params):
        '''
        Constructor
        '''
    
    def insert(self, StockInfo):
        