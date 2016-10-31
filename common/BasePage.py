#-*- coding:utf-8 -*-
import xdrlib ,sys
import xlrd
from selenium import webdriver
import time
from utils.Locator import Locator
from utils.ReadExcelUtil import ReadExcelUtil

'''driver = webdriver.Chrome()
driver.find_element_by_css_selector().text'''


'''locator.getElement() = login
login //body/cd/aie/input
password //body/form/paasw

Locator a = new Locator('login',3,'cssSelector')
b = getElement(a)'''
#抽象页面类
#提供页面的公共方法，供子类使用
class BasePage:
    #构造方法
    #创建对象时自动调用
    #初始化类变量 driver，读取excel内容初始化locatorMap
    def __init__(self,driver):
        self.driver = driver
        excel = ReadExcelUtil()
        self.locatorMap = excel.getLocatorMap()
    #输入字符串到元素
    # @locator:元素对象
    # @values:输入的字符串
    def type(self,locator,values):
        e=self.findElement(locator)
        e.send_keys(values)
    #点击元素
    # @locator:元素对象
    def click(self,locator):
        e=self.findElement(locator)
        e.click()
    '''def clickAndHold(self,locator):
        e = self.findElement(locator)'''
    #获得类变量 driver
    def getDriver(self):
        return self.driver
    #设置类变量 driver
    def setDriver(self,driver):
        self.driver = driver
    #通过元素对象获取元素的WebElement对象
    #@locator:元素对象

    def getElement(self,locator):
        #locator = self.getLocator(locator.getElement())
        opertor = {"xpath" : self.xpath,
              "id" : self.id,
              "name" : self.name,
              "tagName" : self.tagName,
              "className" : self.className,
              "linkText" : self.linkText,
              "cssSelector":self.cssSelector,
              "default" : self.id
              }
    #好几个人问我为什么return opertor.get(locator.getBy())后面为什么会有(locator)
    #locator.getBy()得到的是一个字符串，这个字符串可以是css or id or xpath
    #也就是说这句话的意思其实是：opertor.getid（locator）oropertor.getcss(locator)等
        if(opertor.get(locator.getBy())):
            return opertor.get(locator.getBy())(locator)
        else:
            return opertor.get('default')(locator)
    #通过xpath获取元素的WebElement对象
    # @locator:元素对象
    def xpath(self,locator):
        e = self.driver.find_element_by_xpath(locator.getElement())
        return e
    #通过标签的id属性获取元素的WebElement对象
    # @locator:元素对象
    def id(self,locator):
        e = self.driver.find_element_by_id(locator.getElement())
        return e
    #通过标签的name属性获取元素的WebElement对象
    # @locator:元素对象
    def name(self,locator):
        e = self.driver.find_element_by_name(locator.getElement())
        return e
    #通过标签名称获取元素的WebElement对象
    # @locator:元素对象
    def tagName(self,locator):
        e = self.driver.find_element_by_tagName(locator.getElement())
        return e
    #通过标签的类名称获取元素的WebElement对象
    # @locator:元素对象
    def className(self,locator):
        e = self.driver.find_element_by_className(locator.getElement())
        return e
    #通过链接文本内容获取元素的WebElement对象
    # @locator:元素对象
    def linkText(self,locator):
        e = self.driver.find_element_by_link_text(locator.getElement())
        return e
    #通过css选择器获取元素的WebElement对象
    # @locator:元素对象
    def cssSelector(self,locator):
        e = self.driver.find_element_by_css_selector(locator.getElement())
        return e
    #判断元素的WebElement对象是否存在在当前页面中
    # @locator:元素对象
    # @timeOut:找locator元素的WebElement对象的最大等待时间
    def isElementPresent(self,locator,timeOut):
        while True:
            try:
                if self.getElement(locator):
                    return  True
            except Exception,e:
                print(locator.getElement() + u",By:" + locator.getBy()+ u",元素的WebElement对象查找中...")
            time.sleep(1)
            timeOut = timeOut - 1
            if timeOut <= 0:
                return False
    #在当前页面中找locator元素的WebElement对象
    # @locator:元素对象
    def findElement(self,locator):
        timeOut = locator.getWaitSec()
        while True:
            try:
                if self.getElement(locator):
                    return  self.getElement(locator)
            except Exception, e:
                print(locator.getElement() + u",By:" + locator.getBy()+ u",元素的WebElement对象查找中...")
            time.sleep(1)
            timeOut = timeOut - 1
            if timeOut <= 0:
                return None
    #通过locatorName字符串获取表格中Excel对应行描述的Locator元素对象，
    # @locatorName:测试描述
    def getLocator(self,locatorName):
        for i in range(len(self.locatorMap)):
            if self.locatorMap[i][0].endswith(locatorName):
                #通过excel的第四列（测试对象实体）和第二列（定位方式）返回一个Locator对象
                return Locator(self.locatorMap[i][4],self.locatorMap[i][2],3,self.locatorMap[i][5])
        #如果表格中没有找到测试描述，则通过该字符串返回一个Loacator对象
        return Locator(locatorName)

