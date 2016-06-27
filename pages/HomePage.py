#coding:utf-8
from common.BasePage import BasePage
from utils.Locator import Locator
class HomePage(BasePage):
    def __init__(self,driver):
        self.memberSetting = self.getLocator("memberSetting")
        self.memberPhoto = self.getLocator("memberPhoto")
        self.memberAddress = self.getLocator("memberAddress")
        self.memberOrder = self.getLocator("memberOrder")
        self.memberSettingProfile = self.getLocator("memberSettingProfile")
        self.memberPhotoProfile = self.getLocator("memberPhotoProfile")
        self.memberAddressProfile = self.getLocator("memberAddressProfile")
        self.memberOrderProfile = self.getLocator("memberOrderProfile")
        BasePage.__init__(self,driver)
    def clickOnMemberSetting(self):
        self.click(self.memberSetting)
    def isMemberSettingProfile(self):
        element = self.getElement(self.memberSettingProfile)
        if element.text == u"安全设置":
            return True
        else:
            return False
    def clickOnMemberPhoto(self):
        self.click(self.memberPhoto)
    def isMemberPhotoProfile(self):
        element = self.getElement(self.memberPhotoProfile)
        if element.text == u"修改我的头像":
            return True
        else:
            return False
    def clickOnMemberAddress(self):
        self.click(self.memberAddress)
    def isMemberAddressProfile(self):
        element = self.getElement(self.memberAddressProfile)
        if element.text == u"收货地址":
            return True
        else:
            return False
    def clickOnMemberOrder(self):
        self.click(self.memberOrder)
    def isMemberOrderProfile(self):
        return self.isElementPresent(self.memberOrderProfile,30)
