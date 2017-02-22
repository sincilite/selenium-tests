import unittest
import random
import string
from selenium import webdriver

class Base(unittest.TestCase):

    domain = 'http://ec2-52-212-152-82.eu-west-1.compute.amazonaws.com'

    def generate_random_string(size):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(size))

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.PhantomJS()

    def tearDown(self):
        self.driver.quit()
