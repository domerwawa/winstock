#!/usr/bin/python3
'''
Created on 2016年1月5日

@author: Administrator
'''
import os
import configparser
import sqlite3
import csv

class PropertiesUtils(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        
    def readResourceFile(self, resFile):
        self.conf.read(os.path.realpath(resFile))

    def getPropertiesValue(self, groupName, keyName):
        return self.conf[groupName][keyName]

class DatabaseUtils:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(DatabaseUtils, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
    
class Sqlite3DbUtils(DatabaseUtils):
    conn = None
    def readDbFile(self, dbFile):
        if not self.conn:
            self.conn = sqlite3.connect(os.path.realpath(dbFile))
        
    def getConnection(self):
        return self.conn

class CsvFileUtils(object):
    def __init__(self):
        pass
    
    def readCsvFile(self, csvFileName):
        dataList = []
        with open(csvFileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                dataList.append(row)
            
        return dataList
    