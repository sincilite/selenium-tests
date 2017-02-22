import unittest
from base import Base
from selenium import webdriver

class Login(Base):

    """Base class for login tests

    Attributes:
        username    The username for a demo account
        password    The pasword for a demo account

    """

    username = "demo_user22"

    password = "demoadmin"
