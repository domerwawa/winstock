'''
Created on 2015年12月25日

@author: Administrator
'''

import sqlite3

conn = sqlite3.connect('winstock.db')
c = conn.cursor()

#drop table
c.execute("DROP TABLE stock_info")
# Create table
c.execute('''CREATE TABLE stock_info
            (
              stock_code text PRIMARY KEY NOT NULL,
              stock_name text,
              --所属行业
              industrial_category text,
              --总市值
              total_market_value decimal(15,3),
              --总股本
              general_capital decimal(15,0),
              --流通股本
              circulation_stock decimal(15,0),
              insert_time datetime,
              update_time datetime
            )''')
# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
