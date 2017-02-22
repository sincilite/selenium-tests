from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

from Login.base import Login
import unittest

class LoginPage(Login):

    def test_login(self):
        driver = self.driver
        driver.get(Login.domain)
        self.assertIn("Username", driver.page_source)

    def test_login_success(self):
        driver = self.driver
        driver.get(Login.domain)

        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(Login.username)

        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(Login.password)

        #old_page = driver.find_element_by_tag_name('html')
        elem.send_keys(Keys.RETURN)

        #try:
        #    WebDriverWait(driver, 3).until(
                #expected_conditions.text_to_be_present_in_element(
                    #(By.XPATH, "/html/body/div[1]/div/div/span"),
                    #"Dashboardgh"
                #)
        #        expected_conditions.staleness_of(old_page)
        #    )

        #except:
        #    return False

        driver.implicitly_wait(10) # seconds
        elem = driver.find_element_by_xpath("/html/body/div[1]/div/div/span")
        self.assertIn("Dashboard", elem.text)



    def test_login_failure(self):
        driver = self.driver
        driver.get(Login.domain)

        elem = driver.find_element_by_name("username")
        elem.clear()
        elem.send_keys(Login.generate_random_string(6))

        elem = driver.find_element_by_name("password")
        elem.clear()
        elem.send_keys(Login.generate_random_string(6))
        elem.send_keys(Keys.RETURN)

        try:
            dashboardElement = WebDriverWait(driver, 3).until(
                expected_conditions.text_to_be_present_in_element(
                    (By.XPATH, "/html/body/div[1]/div/div/div[1]"),
                    "The username or password entered do not match any of our records."
                )
            )
        except:
            assert "The username or password entered do not match any of our records." not in driver.page_source

if __name__ == "__main__":
    unittest.main()