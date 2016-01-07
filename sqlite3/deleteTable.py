'''
Created on 2015年12月25日

@author: Administrator
'''

import sqlite3

conn = sqlite3.connect('winstock.db')
c = conn.cursor()

# delete data
print("I just deleted", c.execute("delete from stock_info").rowcount, "rows")

# Save (commit) the changes
conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
conn.close()
