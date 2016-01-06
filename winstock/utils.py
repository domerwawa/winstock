#!/usr/bin/python3
'''
Created on 2016年1月5日

@author: Administrator
'''
import os
import sys
import configparser

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
        self.conf.read(getResourceFilePath(resFile))

    def getPropertiesValue(self, groupName, keyName):
        return self.conf[groupName][keyName]
    
class DatabaseUtils(object):
    pass

class DateUtils(object):
    pass