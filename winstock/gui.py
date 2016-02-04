import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import *
from winstock.service.stockInfoService import StockInfoService
from winstock.utils.propUtils import PropUtils
from winstock.utils.sqlite3DbUtils import Sqlite3DbUtils
from winstock.utils.csvFileUtils import CsvFileUtils
from winstock.dao.stockInfoDao import StockInfoDao
from winstock.entity.stockInfo import StockInfo
import logging
import logging.config
import csv

class MainFrame(tk.Frame):
    def __init__(self, master=None):
        
        #get logger
        logging.config.fileConfig(fname = os.path.realpath("..//resources//pylogconfig.ini"))
        self.logger = logging.getLogger("winstock.gui.MainFrame")
        
        tk.Frame.__init__(self, master)
        master.title("winstock v0.1")
        self.pack()
        self.createWidgets() 
        
    def createWidgets(self):
        
        nb = ttk.Notebook(self.master)
        nb.pack(fill='both', expand='yes')
        
        # create a child frame for each page
        uploadStockinfo = UploadStockInfoFrame(self.master)
        twoFrame = TwoFrame(self.master)
        treeFrame = ThreeFrame(self.master)
        
        # create the pages
        nb.add(uploadStockinfo, text="导入股票信息")
        nb.add(twoFrame, text='page2')
        nb.add(treeFrame, text='page3')
        
class UploadStockInfoFrame(tk.Frame):
    def __init__(self, master=None):
        
        self.logger = logging.getLogger("winstock.gui.UploadStockInfoFrame")
        
        tk.Frame.__init__(self, master)
        self.pack(fill='both', expand='yes')
        self.createWidgets()

    def createWidgets(self):
        # put a button widget on child frame f1 on page1
        #self.btn1 = tk.Button(self, text='button1')
        #self.btn1.pack(side='left', anchor='nw', padx=3, pady=5)
        
        self.label1 = tk.Label(self, text="导入股票基本信息:")
        
        self.contents1 = StringVar()
        self.contents1.set("../input/allstock.csv")
        self.entry1 = tk.Entry(self, textvariable = self.contents1, width = 50)
        self.button1 = tk.Button(self, text="选择文件")
        self.button1["command"] = lambda: self.selectFile(fileFlag = 0)
        self.buttonUploadStockInfo = tk.Button(self, text="upload")
        self.buttonUploadStockInfo["command"] = self.uploadStockInfo
        
        self.label1.grid(row = 0, sticky=E, pady = 5)
        self.entry1.grid(row = 0, column = 1, padx = 5)
        self.button1.grid(row = 0, column = 2, padx = 5)
        self.buttonUploadStockInfo.grid(row = 0, column=3)
        
        self.label2 = tk.Label(self, text="导入股票交易信息:")
        self.contents2 = StringVar()
        self.contents2.set("input file")
        self.entry2 = tk.Entry(self, textvariable = self.contents2, width = 50)
        self.button2 = tk.Button(self, text="选择文件")
        self.button2["command"] = lambda: self.selectFile(fileFlag = 1)
        self.buttonUploadTradeInfo = tk.Button(self, text="upload")
        
        
        self.label2.grid(row = 1, sticky=E, pady = 5)
        self.entry2.grid(row = 1, column = 1, padx = 5)
        self.button2.grid(row = 1, column = 2, padx = 5)
        self.buttonUploadTradeInfo.grid(row = 1, column = 3)
        
    def selectFile(self, fileFlag=None):
        fileName = tk.filedialog.askopenfilename(filetypes=[("csv", "*.csv"), ("All", "*.*")])
        if fileFlag == 0:
            self.contents1.set(fileName)
            self.entry1["textvariable"] = self.contents1
        else:
            self.contents2.set(fileName)
            self.entry2["textvariable"] = self.contents2
    
    def uploadStockInfo(self):
        
        #get connection
        propUtils = PropUtils()
        propUtils.readResourceFile("../resources/db.properties")
        dbFile = propUtils.getPropertiesValue("sqlite3", "database_file")
        dbUtils = Sqlite3DbUtils()
        dbUtils.readDbFile(dbFile)
        conn = dbUtils.getConnection()
        
        stockInfoService = StockInfoService(conn)
        
        stockInfoList = []
        self.logger.debug("csv file:" + self.contents1.get())
        csvFileName = self.contents1.get()
        
        with open(csvFileName, newline='') as csvfile:
            reader = csv.reader(csvfile)
            try:
                for row in reader:
                    stockInfo = StockInfo()
                    stockInfo.setStockCode(row[0])
                    stockInfo.setStockName(row[1])
                    stockInfo.setIndustrialCategory(row[2])
                    stockInfo.setTotalMarketValue(row[3])
                    stockInfo.setGeneralCapital(row[4])
                    stockInfo.setCirculationStock(row[5])
                    
                    self.logger.debug(stockInfo.toString())
                    stockInfoList.append(stockInfo)
            except csv.Error as e:
                self.logger.error(e)
                sys.exit('file {}, line {}: {}'.format(csvFileName, reader.line_num, e))

        stockInfoService.importStockInfo(stockInfoList)
        
        conn.close()
                    
class TwoFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill='both', expand='yes')
        self.createWidgets()

    def createWidgets(self):
        # put a button widget on child frame f1 on page1
        self.btn1 = tk.Button(self, text='button2')
        self.btn1.pack(side='left', anchor='nw', padx=3, pady=5)

    
class ThreeFrame(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(fill='both', expand='yes')
        self.createWidgets()

    def createWidgets(self):
        self.btn1 = tk.Button(self, text='button3')
        self.btn1.pack(side='left', anchor='nw', padx=3, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    #root.geometry('800x600+400+200')
    app = MainFrame(master=root)
    app.mainloop()
