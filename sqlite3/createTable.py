'''
Created on 2015年12月25日

@author: Administrator
'''

import sqlite3

conn = sqlite3.connect('winstock.db')
c = conn.cursor()

#drop table
#c.execute("DROP TABLE stock_info")
# Create table
try:
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
except sqlite3.OperationalError as er:
    print("create table stock_info error")
# Save (commit) the changes
conn.commit()

#c.execute("DROP TABLE stock_price")
try:
    c.execute('''CREATE TABLE stock_price
                (
                  stock_code text,
                  --交易日期
                  trade_date date,
                  --期间  1:daily; 2:weekly; 3: monthly 4: yearly
                  period integer,
                  --开盘价
                  open_price decimal(15,3),
                  --最高价
                  high_price decimal(15,3),
                  --最低价
                  low_price decimal(15,3),
                  --收盘价
                  close_price decimal(15,3),
                  --成交量
                  volume decimal(15,0),
                  --调整后价格
                  adj_close decimal(15, 3),
                  insert_time datetime,
                  update_time datetime,
                  primary key(stock_code, trade_date, period)
                )''')
except sqlite3.OperationalError as er:
    print("create table stock_price error")
conn.commit()

#c.execute("DROP TABLE stock_rehabilitation_price")
try:
    c.execute('''CREATE TABLE stock_rehabilitation_price
                (
                  stock_code text,
                  --交易日期
                  trade_date date,
                  --开盘价
                  open decimal(15,3),
                  --最高价
                  high decimal(15,3),
                  --最低价
                  low decimal(15,3),
                  --收盘价
                  close decimal(15,3),
                  --成交量
                  volume decimal(15,0),
                  --成交金额
                  amount decimal(15,3),
                  insert_time datetime,
                  update_time datetime,
                  primary key(stock_code, trade_date)
                )''')
except sqlite3.OperationalError as er:
    print("create table stock_rehabilitation_price error")
conn.commit()


# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
