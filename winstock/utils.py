#!/usr/bin/python3
'''
Created on 2016年1月5日

@author: Administrator
'''
import os
import sys
import configparser
import sqlite3
import csv

#this method maybe no good enough
def getResourceFilePath(resFile):
    for syspath in sys.path:
        resourceFilePath = os.path.abspath(syspath + resFile)
        if os.path.exists(resourceFilePath):
            return resourceFilePath
    raise Exception("have no resource file:" + resFile)

class PropertiesUtils(object):
    def __init__(self):
        self.conf = configparser.ConfigParser()
        
    def readResourceFile(self, resFile):
        #self.conf.read(getResourceFilePath(resFile))
        self.conf.read(os.path.realpath(resFile))

    def getPropertiesValue(self, groupName, keyName):
        return self.conf[groupName][keyName]

class DatabaseUtils(object):
    def __init__(self):
        pass
    
    def getConnection(self):
        pass
    
class Sqlite3DbUtils(DatabaseUtils):
    def __init__(self, dbFile):
        #self.conn = sqlite3.connect(getResourceFilePath(dbFile))
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
    