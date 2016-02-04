'''
Created on 2016年2月4日

@author: Adams Zhou
'''
import csv

class CsvFileUtils:
    def __init__(self):
        pass
    
    def readCsvFile(self, csvFileName):
        dataList = []
        with open(csvFileName, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            for row in spamreader:
                dataList.append(row)
            
        return dataList
    