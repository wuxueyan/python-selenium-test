#coding:utf-8
import unittest
from selenium import webdriver
from action.CommonLogin import CommonLogin
class loginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
    def test_login(self):
        page = CommonLogin()
        page.setDriver(self.driver)
        loginpage  = page.loginExprMobilePasswordNull("","");
        loginpage  = page.loginExprMobileNull("","123456")
        loginpage  = page.loginExprPasswordNull("18270720030","")
        loginpage  = page.loginExprMobileError("18270","123456")
        loginpage  = page.loginExprPasswordError("18270720030","654321")
        homepage = page.login()
        homepage = page.settingPage(homepage)
        homepage = page.photoPage(homepage)
        homepage = page.addressPage(homepage)
        homepage = page.orderPage(homepage)


    def tearDown(self):
        self.driver.close()

