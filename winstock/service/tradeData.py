'''
Created on 2016年2月29日

@author: adams zhou
'''
from winstock.utils import consts
import json
import time
from urllib.request import urlopen, Request
import pandas
from winstock.utils.dateUtils import DataUtils
import lxml.html
from xml.etree import ElementTree as etree
import numpy
from pandas.compat import StringIO
import re

class TradeData:
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
    
    def getHistoryData (self, code=None, start=None, end=None,
                  ktype='D', retry_count=3,
                  pause=0.001):
        symbol = self._code_to_symbol(code)
        url = ''
    
        url = consts.DAY_PRICE_URL%(consts.P_TYPE['http'], consts.DOMAINS['ifeng'],
                                consts.K_TYPE[ktype.upper()], symbol)
        
        print(url)
        for _ in range(retry_count):
            time.sleep(pause)
            try:
                request = Request(url)
                lines = urlopen(request, timeout = 10).read()
                if len(lines) < 15: #no data
                    return None
            except Exception as e:
                print(e)
            else:
                js = json.loads(lines.decode('utf-8'))
                cols = []
                if (code in consts.STOCK_MARKET_TYPE) & (ktype.upper() in consts.K_LABELS):
                    cols = consts.INX_DAY_PRICE_COLUMNS
                else:
                    cols = consts.DAY_PRICE_COLUMNS
                if len(js['record'][0]) == 14:
                    cols = consts.INX_DAY_PRICE_COLUMNS
                df = pandas.DataFrame(js['record'], columns=cols)
                if ktype.upper() in ['D', 'W', 'M']:
                    df = df.applymap(lambda x: x.replace(u',', u''))
                    df[df==''] = 0
                for col in cols[1:]:
                    df[col] = df[col].astype(float)
                if start is not None:
                    df = df[df.date >= start]
                if end is not None:
                    df = df[df.date <= end]
                if (code in consts.STOCK_MARKET_TYPE) & (ktype in consts.K_MIN_LABELS):
                    df = df.drop('turnover', axis=1)
                df = df.set_index('date')
                df = df.sort_index(ascending = False)
                return df
        raise IOError(consts.NETWORK_URL_ERROR_MSG)

    def getRehabilitationData(self, code, start=None, end=None, autype='qfq',
                   index=False, retry_count=3, pause=0.001, drop_factor=True):
        '''
                        获取历史复权数据
        Parameters
        ------
          code:string
                          股票代码 e.g. 600848
          start:string
                          开始日期 format：YYYY-MM-DD 为空时取当前日期
          end:string
                          结束日期 format：YYYY-MM-DD 为空时取去年今日
          autype:string
                          复权类型，qfq-前复权 hfq-后复权 None-不复权，默认为qfq
          retry_count : int, 默认 3
                         如遇网络等问题重复执行的次数 
          pause : int, 默认 0
                        重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
          drop_factor : bool, 默认 True
                        是否移除复权因子，在分析过程中可能复权因子意义不大，但是如需要先储存到数据库之后再分析的话，有该项目会更加灵活
        return
        -------
          DataFrame
              date 交易日期 (index)
              open 开盘价
              high  最高价
              close 收盘价
              low 最低价
              volume 成交量
              amount 成交金额
        '''
        #if no give start ,set start last year
        start = DataUtils.getDefaultLastYear() if start is None else start
        end = DataUtils.getStrToday() if end is None else end
        qs = DataUtils.getQuarters(start, end)
        qt = qs[0]
        consts._write_head()
        data = self._getRehabilitationByQuarter(self._get_index_url(index, code, qt), index,
                              retry_count, pause)
        if len(qs)>1:
            for d in range(1, len(qs)):
                qt = qs[d]
                consts._write_console()
                df = self._getRehabilitationByQuarter(self._get_index_url(index, code, qt), index,
                                    retry_count, pause)
                data = data.append(df, ignore_index=True)
        if len(data) == 0 or len(data[(data.date>=start)&(data.date<=end)]) == 0:
            return None
        data = data.drop_duplicates('date')
        if index:
            data = data[(data.date>=start) & (data.date<=end)]
            data = data.set_index('date')
            data = data.sort_index(ascending=False)
            return data
        if autype == 'hfq':
            if drop_factor:
                data = data.drop('factor', axis=1)
            data = data[(data.date>=start) & (data.date<=end)]
            for label in ['open', 'high', 'close', 'low']:
                data[label] = data[label].map(consts.FORMAT)
                data[label] = data[label].astype(float)
            data = data.set_index('date')
            data = data.sort_index(ascending = False)
            return data
        else:
            if autype == 'qfq':
                if drop_factor:
                    data = data.drop('factor', axis=1)
                df = self._parase_fq_factor(code, start, end)
                df = df.drop_duplicates('date')
                df = df.sort_values('date', ascending=False)
                firstDate = data.head(1)['date']
                frow = df[df.date == firstDate[0]]
                rt = self.get_realtime_quotes(code)
                if rt is None:
                    return None
                if ((float(rt['high']) == 0) & (float(rt['low']) == 0)):
                    preClose = float(rt['pre_close'])
                else:
                    if DataUtils.isHoliday(DataUtils.getStrToday()):
                        preClose = float(rt['price'])
                    else:
                        if (DataUtils.getTodayHour() > 9) & (DataUtils.getTodayHour() < 18):
                            preClose = float(rt['pre_close'])
                        else:
                            preClose = float(rt['price'])
                
                rate = float(frow['factor']) / preClose
                data = data[(data.date >= start) & (data.date <= end)]
                for label in ['open', 'high', 'low', 'close']:
                    data[label] = data[label] / rate
                    data[label] = data[label].map(consts.FORMAT)
                    data[label] = data[label].astype(float)
                data = data.set_index('date')
                data = data.sort_index(ascending = False)
                return data
            else:
                for label in ['open', 'high', 'close', 'low']:
                    data[label] = data[label] / data['factor']
                if drop_factor:
                    data = data.drop('factor', axis=1)
                data = data[(data.date>=start) & (data.date<=end)]
                for label in ['open', 'high', 'close', 'low']:
                    data[label] = data[label].map(consts.FORMAT)
                data = data.set_index('date')
                data = data.sort_index(ascending = False)
                data = data.astype(float)
                return data



    def _code_to_symbol(self, code):
        
        if code in consts.STOCK_MARKET_TYPE:
            return consts.STOCK_MARKET_LIST[code]
        else:
            if len(code) != 6 :
                return ''
            else:
                return 'sh%s'%code if code[:1] in ['5', '6', '9'] else 'sz%s'%code
    
    def _get_index_url(self, index, code, qt):
        if index:
            url = consts.HIST_INDEX_URL%(consts.P_TYPE['http'], consts.DOMAINS['vsf'],
                                  code, qt[0], qt[1])
        else:
            url = consts.HIST_FQ_URL%(consts.P_TYPE['http'], consts.DOMAINS['vsf'],
                                  code, qt[0], qt[1])
        return url
    
    def _getRehabilitationByQuarter(self, url, index, retry_count, pause):
        for _ in range(retry_count):
            time.sleep(pause)
            try:
                print(url)
                request = Request(url)
                text = urlopen(request, timeout=10).read()
                text = text.decode('GBK')
                html = lxml.html.parse(StringIO(text))
                res = html.xpath('//table[@id=\"FundHoldSharesTable\"]')
                
                sarr = [etree.tostring(node).decode('utf-8') for node in res]
                
                sarr = ''.join(sarr)
                df = pandas.read_html(sarr, skiprows = [0, 1])[0]
                if len(df) == 0:
                    return pandas.DataFrame()
                if index:
                    df.columns = consts.HIST_FQ_COLS[0:7]
                else:
                    df.columns = consts.HIST_FQ_COLS
                if df['date'].dtypes == numpy.object:
                    df['date'] = df['date'].astype(numpy.datetime64)
                df = df.drop_duplicates('date')
            except Exception as e:
                print(e)
            else:
                return df
        raise IOError(consts.NETWORK_URL_ERROR_MSG)

    def _parase_fq_factor(self, code, start, end):
        symbol = self._code_to_symbol(code)
        request = Request(consts.HIST_FQ_FACTOR_URL%(consts.P_TYPE['http'],
                                                 consts.DOMAINS['vsf'], symbol))
        text = urlopen(request, timeout=10).read()
        text = text[1:len(text)-1]
        text = text.decode('utf-8')
        text = text.replace('{_', '{"')
        text = text.replace('total', '"total"')
        text = text.replace('data', '"data"')
        text = text.replace(':"', '":"')
        text = text.replace('",_', '","')
        text = text.replace('_', '-')
        text = json.loads(text)
        df = pandas.DataFrame({'date':list(text['data'].keys()), 'factor':list(text['data'].values())})
        df['date'] = df['date'].map(self._fun_except) # for null case
        if df['date'].dtypes == numpy.object:
            df['date'] = df['date'].astype(numpy.datetime64)
        df = df.drop_duplicates('date')
        df['factor'] = df['factor'].astype(float)
        return df
    
    def _fun_except(self, x):
        if len(x) > 10:
            return x[-10:]
        else:
            return x


    def get_realtime_quotes(self, symbols=None):
        """
            获取实时交易数据 getting real time quotes data
           用于跟踪交易情况（本次执行的结果-上一次执行的数据）
        Parameters
        ------
            symbols : string, array-like object (list, tuple, Series).
            
        return
        -------
            DataFrame 实时交易数据
                  属性:0：name，股票名字
                1：open，今日开盘价
                2：pre_close，昨日收盘价
                3：price，当前价格
                4：high，今日最高价
                5：low，今日最低价
                6：bid，竞买价，即“买一”报价
                7：ask，竞卖价，即“卖一”报价
                8：volumn，成交量 maybe you need do volumn/100
                9：amount，成交金额（元 CNY）
                10：b1_v，委买一（笔数 bid volume）
                11：b1_p，委买一（价格 bid price）
                12：b2_v，“买二”
                13：b2_p，“买二”
                14：b3_v，“买三”
                15：b3_p，“买三”
                16：b4_v，“买四”
                17：b4_p，“买四”
                18：b5_v，“买五”
                19：b5_p，“买五”
                20：a1_v，委卖一（笔数 ask volume）
                21：a1_p，委卖一（价格 ask price）
                ...
                30：date，日期；
                31：time，时间；
        """
        symbols_list = ''
        if isinstance(symbols, list) or isinstance(symbols, set) or isinstance(symbols, tuple) or isinstance(symbols, pandas.Series):
            for code in symbols:
                symbols_list += self._code_to_symbol(code) + ','
        else:
            symbols_list = self._code_to_symbol(symbols)
            
        symbols_list = symbols_list[:-1] if len(symbols_list) > 8 else symbols_list 
        request = Request(consts.LIVE_DATA_URL%(consts.P_TYPE['http'], consts.DOMAINS['sinahq'],
                                                    self._random(), symbols_list))
        text = urlopen(request,timeout=10).read()
        text = text.decode('GBK')
        reg = re.compile(r'\="(.*?)\";')
        data = reg.findall(text)
        regSym = re.compile(r'(?:sh|sz)(.*?)\=')
        syms = regSym.findall(text)
        data_list = []
        syms_list = []
        for index, row in enumerate(data):
            if len(row)>1:
                data_list.append([astr for astr in row.split(',')])
                syms_list.append(syms[index])
        if len(syms_list) == 0:
            return None
        df = pandas.DataFrame(data_list, columns=consts.LIVE_DATA_COLS)
        df = df.drop('s', axis=1)
        df['code'] = syms_list
        ls = [cls for cls in df.columns if '_v' in cls]
        for txt in ls:
            df[txt] = df[txt].map(lambda x : x[:-2])
        return df

    def _random(self, n=13):
        from random import randint
        start = 10**(n-1)
        end = (10**n)-1
        return str(randint(start, end))

    def get_today_all(self):
        """
            一次性获取最近一个日交易日所有股票的交易数据
        return
        -------
          DataFrame
               属性：代码，名称，涨跌幅，现价，开盘价，最高价，最低价，最日收盘价，成交量，换手率，成交额，市盈率，市净率，总市值，流通市值
        """
        consts._write_head()
        df = self._parsing_dayprice_json(1)
        if df is not None:
            for i in range(2, consts.PAGE_NUM[0]):
                newdf = self._parsing_dayprice_json(i)
                df = df.append(newdf, ignore_index=True)
        return df

    def _parsing_dayprice_json(self, pageNum=1):
        """
               处理当日行情分页数据，格式为json
         Parameters
         ------
            pageNum:页码
         return
         -------
            DataFrame 当日所有股票交易数据(DataFrame)
        """
        consts._write_console()
        request = Request(consts.SINA_DAY_PRICE_URL%(consts.P_TYPE['http'], consts.DOMAINS['vsf'],
                                     consts.PAGES['jv'], pageNum))
        text = urlopen(request, timeout=10).read()
        if text == 'null':
            return None
        reg = re.compile(r'\,(.*?)\:') 
        text = reg.sub(r',"\1":', text.decode('gbk')) 
        text = text.replace('"{symbol', '{"symbol')
        text = text.replace('{symbol', '{"symbol"')

        jstr = json.dumps(text)
       
        js = json.loads(jstr)
        df = pandas.DataFrame(pandas.read_json(js, dtype={'code':object}),
                          columns=consts.DAY_TRADING_COLUMNS)
        df = df.drop('symbol', axis=1)
    #     df = df.ix[df.volume > 0]
        return df

    def get_tick_data(self, code=None, date=None, retry_count=3, pause=0.001):
        """
            获取分笔数据
        Parameters
        ------
            code:string
                      股票代码 e.g. 600848
            date:string
                      日期 format：YYYY-MM-DD
            retry_count : int, 默认 3
                      如遇网络等问题重复执行的次数
            pause : int, 默认 0
                     重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
         return
         -------
            DataFrame 当日所有股票交易数据(DataFrame)
                  属性:成交时间、成交价格、价格变动，成交手、成交金额(元)，买卖类型
        """
        if code is None or len(code)!=6 or date is None:
            return None
        symbol = self._code_to_symbol(code)
        for _ in range(retry_count):
            time.sleep(pause)
            try:
                re = Request(consts.TICK_PRICE_URL % (consts.P_TYPE['http'], consts.DOMAINS['sf'], consts.PAGES['dl'],
                                    date, symbol))
                lines = urlopen(re, timeout=10).read()
                lines = lines.decode('GBK') 
                if len(lines) < 20:
                    return None
                df = pandas.read_table(StringIO(lines), names=consts.TICK_COLUMNS,
                                   skiprows=[0])      
            except Exception as e:
                print(e)
            else:
                return df
        raise IOError(consts.NETWORK_URL_ERROR_MSG)


if __name__ == '__main__':
    
    td = TradeData()
    #df1 = td.getHistoryData("600011")
    #print (df1)
    df2 = td.getRehabilitationData("601633", start = "2016-03-04", autype='qfq')
    #print(df2)
    #print(df2.columns)
    #print(df2.values)
    for ind in df2.index:
        print(str(ind.year) + "-" + str(ind.month) + "-" + str(ind.day), df2.get_value(ind, 'open'), df2.get_value(ind, 'high'), 
              df2.get_value(ind, 'low'), df2.get_value(ind, 'close'))
    
    
    
    #df3 = td.get_realtime_quotes("601633")
    #print (df3)
    #df4 = td.get_today_all()
    #print(df4)
    #df5 = td.get_tick_data("601633", date = "2016-02-26")
    #print(df5)
    