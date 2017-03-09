import unittest
import sys
import os
import yaml
import random
import string
from selenium import webdriver

class Base(unittest.TestCase):

    appSettings = {}

    def loadConfig(self):
        environment = os.environ["APPLICATION_ENV"];

        with open("settings.yml", "r") as stream:
            try:
                config = yaml.load(stream)
            except yaml.YAMLError as exc:
                print (exc)

            appConfig = {}
            appConfig.update(config["global"])
            appConfig.update(config[environment])
            Base.appSettings = appConfig


    def getAppSettings(self):
        return self.appSettings

    def generate_random_string(size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

    def setUp(self):
        self.loadConfig()
        self.driver = webdriver.Firefox()
        #self.driver = webdriver.PhantomJS()

    def tearDown(self):
        self.driver.quit()