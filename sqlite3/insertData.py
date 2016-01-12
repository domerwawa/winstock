'''
Created on 2015年12月25日

@author: Administrator
'''

import sqlite3
from datetime import datetime

conn = sqlite3.connect('winstock.db')
c = conn.cursor()

# delete data
print("I just deleted", c.execute("delete from stock_info").rowcount, "rows")

# insert data
c.execute('''INSERT INTO stock_info
            (stock_code, stock_name, industrial_category, total_market_value, general_capital, circulation_stock, insert_time, update_time) values 
            ('111111', '股票1', '计算机', 123456789123456.34, 1, 1, ?, ?)''', (datetime.now(), datetime.now())
            )
c.execute('''INSERT INTO stock_info
            (stock_code, stock_name, industrial_category, total_market_value, general_capital, circulation_stock, insert_time, update_time) values 
            ('222222', '股票2', '计算机', 2, 2, 2, ?, ?)''', (datetime.now(), datetime.now())
            )
c.execute('''INSERT INTO stock_info
            (stock_code, stock_name, industrial_category, total_market_value, general_capital, circulation_stock, insert_time, update_time) values 
            ('333333', '股票1', '计算机', 3, 3, 3, ?, ?)''', (datetime.now(), datetime.now())
            )
# Save (commit) the changes
conn.commit()

for row in c.execute("select * from stock_info"):
    print(row)

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
