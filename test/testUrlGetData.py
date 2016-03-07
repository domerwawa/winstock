'''
Created on 2016年2月29日

@author: Administrator
'''
from urllib.request import urlopen, Request

def main():
    url = "http://finance.ifeng.com/app/hq/stock/sh600011/"
    print("hello world")
    try:
        request = Request(url)
        lines = urlopen(request, timeout = 10).read()
        print(lines)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()