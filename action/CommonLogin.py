#coding:utf-8
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
class CommonLogin:
    DRIVER=None
    def getDriver(self):
        return CommonLogin.DRIVER
    def loginExprMobilePasswordNull(self,mobile,password):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.exprMobilePasswordNull,30)
        assert True == loginpage.isExprMobilePasswordNull()
        return LoginPage(self.getDriver())

    def loginExprMobileNull(self,mobile,password):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.exprMobileNull,30)
        assert True == loginpage.isExprMobileNull()
        return LoginPage(self.getDriver())

    def loginExprPasswordNull(self,mobile,password):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.exprPasswordNull,30)
        assert True == loginpage.isExprPasswordNull()
        return LoginPage(self.getDriver())

    def loginExprMobileError(self,mobile,password):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.exprMobileError,30)
        assert True == loginpage.isExprMobileError()
        return LoginPage(self.getDriver())

    def loginExprPasswordError(self,mobile,password):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.exprPasswordError,30)
        assert True == loginpage.isExprPasswordError()
        return LoginPage(self.getDriver())








    def login(self,mobile="18270720030",password="123456"):
        loginpage = LoginPage(self.getDriver())
        loginpage.waitForPreLoad()
        loginpage.typeMobileInputBox(mobile)
        loginpage.typeLoginPasswordInputBox(password)
        loginpage.typeClickOnLoginButton()
        loginpage.isElementPresent(loginpage.profile,30)
        assert True == loginpage.isProfilePresent()

        return HomePage(self.getDriver())
    def settingPage(self,homepage):
        homepage.clickOnMemberSetting()
        homepage.isElementPresent(homepage.memberSettingProfile,30)
        assert True == homepage.isMemberSettingProfile()
        self.getDriver().back()
        return HomePage(self.getDriver())
        #return SettingPage(self.getDriver())
    def photoPage(self,homepage):
        homepage.clickOnMemberPhoto()
        homepage.isElementPresent(homepage.memberPhotoProfile,30)
        assert True == homepage.isMemberPhotoProfile()
        self.getDriver().back()
        return HomePage(self.getDriver())
        #return photoPage(self.getDriver())
    def addressPage(self,homepage):
        homepage.clickOnMemberAddress()
        homepage.isElementPresent(homepage.memberAddressProfile,30)
        assert True == homepage.isMemberAddressProfile()
        self.getDriver().back()
        return HomePage(self.getDriver())
        #return addressPage(self.getDriver())
    def orderPage(self,homepage):
        homepage.clickOnMemberOrder()
        homepage.isElementPresent(homepage.memberOrderProfile,30)
        assert True == homepage.isMemberOrderProfile()
        self.getDriver().back()
        return HomePage(self.getDriver())
        #return orderPage(self.getDriver())






    def setDriver(self,driver):
        CommonLogin.DRIVER = driver