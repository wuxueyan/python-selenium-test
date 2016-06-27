#coding:utf-8
class Locator:
    #通过测试对象实体、定位方式、等待时间构造 Locator对象
    # @element:测试描述
    # @byType:元素定位方式
    # @waitSec:找该元素的等待时间
    def __init__(self,element,byType="id",waitSec=3,expert=""):
        self.element = element
        self.waitSec = waitSec
        self.byType = byType
        self.expert = expert
    #获得测试描述
    def getElement(self):
        return self.element
    #获得等待时间
    def getWaitSec(self):
        return self.waitSec
    #获得定位方式
    def getBy(self):
        return self.byType
    def getExpert(self):
        return self.expert
    #设置定位方式
    def setBy(self,byType):
        self.byType=byType
