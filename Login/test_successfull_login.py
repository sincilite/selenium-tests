from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from Login.base import Login
from base import Base
import unittest

class LoginPage(Login):

    def test_login(self):
        driver = Login.launch_login(self, self.driver);
        driver.get(Login.appSettings['domain'])
        self.assertIn("Username", driver.page_source)


    def test_login_success(self):
        driver = Login.launch_login(self, self.driver);
        driver.get(Login.appSettings['domain'])
        Login.provide_credentials(self, driver, Login.appSettings["credentials"]["username"], Login.appSettings["credentials"]["password"])

        driver.implicitly_wait(10) # seconds
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/span")
        self.assertIn("Dashboard", elem.text)


    def test_login_failure(self):
        driver = Login.launch_login(self, self.driver);
        driver.get(Login.appSettings['domain'])
        Login.provide_credentials(self, driver, Login.appSettings["credentials"]["incorrect_username"], Login.appSettings["credentials"]["incorrect_password"])

        driver.implicitly_wait(10) # seconds
        result = driver.find_element_by_class_name("alert")
        self.assertIn("The username or password entered do not match any of our records.", result.text)