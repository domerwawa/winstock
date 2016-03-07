'''
Created on 2016年2月29日

@author: Administrator
'''
import datetime
import pandas as pd

class DataUtils:
    '''
    Data help class
    '''
    
    @staticmethod
    def getDefaultLastYear():
        
        year = datetime.datetime.today().date().year

        yearDay = 366 if DataUtils.checkLeapYear(year) else 365
        lastyear = datetime.datetime.today().date() + datetime.timedelta(-yearDay)
        return str(lastyear)
    
    @staticmethod
    def getStrToday():
        day = datetime.datetime.today().date()
        return str(day) 

    @staticmethod
    def getQuarters(start, end):
        idx = pd.period_range('Q'.join(DataUtils.getYearQuarter(start)), 'Q'.join(DataUtils.getYearQuarter(end)),
                              freq='Q-JAN')
        return [str(d).split('Q') for d in idx][::-1]
    
    @staticmethod
    def getYearQuarter(date):
        mon = date[5:7]
        mon = int(mon)
        return[date[0:4], DataUtils.getQuarter(mon)]
    
    @staticmethod
    def getQuarter(month):
        '''
        get Quarter from month
        '''
        if month in [1, 2, 3]:
            return '1'
        elif month in [4, 5, 6]:
            return '2'
        elif month in [7, 8, 9]:
            return '3'
        elif month in [10, 11, 12]:
            return '4'
        else:
            return None
    
    @staticmethod
    def isHoliday(date):
        holiday = ['2015-01-01', '2015-01-02', '2015-02-18', '2015-02-19', '2015-02-20', '2015-02-23', '2015-02-24',
                   '2015-04-06', '2015-05-01', '2015-06-22', '2015-09-03', '2015-09-04', '2015-10-01', '2015-10-02',
                   '2015-10-05', '2015-10-06', '2015-10-07',
                   '2016-01-01', '2016-02-08', '2016-02-09', '2016-02-10', '2016-02-11', '2016-02-12', '2016-04-04',
                   '2016-05-02', '2016-06-09', '2016-06-10', '2016-09-15', '2016-09-16', '2016-10-03', '2016-10-04',
                   '2016-10-05', '2016-10-06', '2016-10-07']

        if isinstance(date, str):
            today = datetime.datetime.strptime(date, '%Y-%m-%d')
    
        if today.isoweekday() in [6, 7] or date in holiday:
            return True
        else:
            return False
        
    @staticmethod  
    def getTodayHour():
        return datetime.datetime.today().hour
    
    @staticmethod
    def checkLeapYear(year):
            if (year%4 == 0 and (year%100 != 0 or year%400 == 0) ) :
                return True
            else:
                return False
            
if __name__ == "__main__":
    
    print(DataUtils.getDefaultLastYear())
    