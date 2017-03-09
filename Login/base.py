import unittest
from base import Base
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Login(Base):

    """ Base class for login tests
    """

    """ Request the login page
    """
    def launch_login(self, driver):
        driver.get(Base.appSettings['domain'])
        return driver

    """ Populates the username and password fields with provided data
    """
    def provide_credentials(self, driver, username, password):
        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(username)

        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(password)
        elem.send_keys(Keys.RETURN)

        return driver

