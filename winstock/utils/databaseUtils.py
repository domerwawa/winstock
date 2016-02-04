'''
Created on 2016年2月4日

@author: Adams Zhou
'''

class DatabaseUtils:
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(DatabaseUtils, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
    