'''
Created on 2016年2月4日

@author: Adams Zhou
'''
from winstock.utils.databaseUtils import DatabaseUtils
import sqlite3
import os

class Sqlite3DbUtils(DatabaseUtils):
    conn = None
    def readDbFile(self, dbFile):
        if not self.conn:
            self.conn = sqlite3.connect(os.path.realpath(dbFile))
        
    def getConnection(self):
        return self.conn
