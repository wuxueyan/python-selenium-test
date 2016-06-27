#coding:utf-8
from common.BasePage import BasePage
from utils.Locator import Locator
import time

#登录页面类

class LoginPage(BasePage):
    #构造登录页面对象，打开登录页面
    def __init__(self,driver):
        BasePage.__init__(self,driver)
        self.loginMobileInputBox = self.getLocator("loginMobileInputBox")
        self.loginPasswordInputBox = self.getLocator("loginPasswordInputBox")
        self.loginButton = self.getLocator("loginButton")
        self.exprMobilePasswordNull = self.getLocator("exprMobilePasswordNull")
        self.exprMobileNull = self.getLocator("exprMobileNull")
        self.exprPasswordNull = self.getLocator("exprPasswordNull")
        self.exprMobileError = self.getLocator("exprMobileError")
        self.exprPasswordError = self.getLocator("exprPasswordError")
        self.profile = self.getLocator("profile")
        driver.get('http://yun.d.easyder.com/mobile/login')
    #输入手机号
    #@mobile：手机号
    def typeMobileInputBox(self,mobile):
        self.type(self.loginMobileInputBox,mobile)
    #输入密码
    #@password:密码
    def typeLoginPasswordInputBox(self,password):
        self.type(self.loginPasswordInputBox,password)
    #点击登录按钮
    def typeClickOnLoginButton(self):
        self.click(self.loginButton)
    #判断期望元素是否存在
    def isProfilePresent(self):
        return self.isElementPresent(self.profile,20)
    def isExprMobilePasswordNull(self):
        print self.exprMobilePasswordNull.getExpert()
        element = self.getElement(self.exprMobilePasswordNull)
        if element.text == self.exprMobilePasswordNull.getExpert():
            return True
        else:
            return False
    def isExprMobileNull(self):
        element = self.getElement(self.exprMobileNull)
        if element.text == self.exprMobileNull.getExpert():
            return True
        else:
            return False
    def isExprPasswordNull(self):
        element = self.getElement(self.exprPasswordNull)
        if element.text == self.exprPasswordNull.getExpert():
            return True
        else:
            return False
    def isExprMobileError(self):
        element = self.getElement(self.exprMobileError)
        if element.text == self.exprMobileError.getExpert():
            return True
        else:
            return False
    def isExprPasswordError(self):
        element = self.getElement(self.exprPasswordError)
        if element.text == self.exprPasswordError.getExpert():
            return True
        else:
            return False
    #等待页面加载
    def waitForPreLoad(self):
        self.getDriver().set_page_load_timeout(30)
