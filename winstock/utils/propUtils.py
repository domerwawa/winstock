'''
Created on 2016年2月4日

@author: Adams Zhou
'''
import configparser
import os

class PropUtils:
    def __init__(self):
        self.conf = configparser.ConfigParser()
        
    def readResourceFile(self, resFile):
        self.conf.read(os.path.realpath(resFile))

    def getPropertiesValue(self, groupName, keyName):
        return self.conf[groupName][keyName]
