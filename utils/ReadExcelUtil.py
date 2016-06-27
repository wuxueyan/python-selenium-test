#coding:utf-8
import xdrlib ,sys
import xlrd
from selenium import webdriver
#读取Excel表格中的内容
class ReadExcelUtil:
    #获取Excel中所有的行和列，返回一个二维列表
    def getLocatorMap(self):
        f = xlrd.open_workbook("./est.xlsx")
        table = f.sheet_by_index(0)
        nrows = table.nrows
        ncols = table.ncols
        list = []

        for i in range(nrows):
            tmp = []
            for j in range(ncols):
                try:
                    tmp.append(table.cell(i,j).value)
                except Exception,e:
                    tmp.append(table.cell(i,j).value)
            list.append(tmp)
        return list

