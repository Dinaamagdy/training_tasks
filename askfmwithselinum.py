from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from nose.tools import assert_equals
from dects import dec



class googleselinum(unittest.TestCase):
    """
    @classmethod

    def setUpClass(cls):
        # create a new Firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
    """
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    def test_googletitle(self):
        driver=self.driver
        driver.get(dec['google'])
        self.assertIn("Google", driver.title)

    def test_gotofindelements(self):
        driver=self.driver
        driver.get(dec['google'])
        self.assertIn("Google", driver.title)
        elem=driver.find_element_by_name(dec['google_search'])
        elem.send_keys("askfm")
        elemen=driver.find_element_by_name(dec['search_button'])
        elemen.click()
        self.assertIsNot("result not found",driver.page_source)
        self.assertIn("askfm", driver.current_url)
        elem=driver.find_element_by_link_text('Ask and Answer - ASKfm')
        elem.click()
        time.sleep(2)
        self.assertIn("ASKfm",driver.title)

    def test_sumbitform(self):
        driver=self.driver
        driver.get('http://ask.fm/')
        self.assertIn("ASKfm", driver.title)
        elem=driver.find_element_by_class_name(dec['sign up button'])
        elem.click()
        time.sleep(4)
        elem=driver.find_element_by_id(dec['user_login_name'])
        elem.send_keys('dinamagdymohammed9983nl20l')
        elem=driver.find_element_by_id(dec['user_password'])
        elem.send_keys('dinamagdymohammed930p3')
        elem=driver.find_element_by_id(dec['user_name'])
        elem.send_keys('dinamagdymohammed')
        elem=driver.find_element_by_id(dec['user_email'])
        elem.send_keys('dinajjjjjj2ljjjkkhlpi@gmail.com')
        select = Select(driver.find_element_by_id(dec['birth_day']))
        select.select_by_value('22')
        select = Select(driver.find_element_by_id(dec['birth_month']))
        select.select_by_value('2')
        select= Select(driver.find_element_by_id(dec['birth_year']))
        select.select_by_value('1993')
        select= Select(driver.find_element_by_id(dec['user_gender']))
        select.select_by_index(2)
        select= Select(driver.find_element_by_id(dec['user_language']))
        select.select_by_visible_text('English')
        elem=driver.find_element_by_class_name(dec['submit_button'])
        elem.click()
        time.sleep(3)
        self.assertIn("account", driver.current_url)
     #def test_sumbit(self):


    def test_login(self):
        driver=self.driver
        driver.get('http://ask.fm/')
        self.assertIn("ASKfm", driver.title)
        time.sleep(3)
        elem=driver.find_element_by_link_text(dec['log_in_button'])
        elem.click()
        time.sleep(3)
        elem=driver.find_element_by_class_name(dec['username'])
        elem.send_keys('dinamagdymohammed993nl20l')
        elem=driver.find_element_by_name('password')
        elem.send_keys('dinamagdymohammed930p3')
        elem=driver.find_element_by_class_name("btn-primary-wide")
        elem.click()
        time.sleep(2)
        self.assertIn("account", driver.current_url)
        elem=driver.find_element_by_link_text("Profile")
        elem.click()


    def tearDown(self):
        self.driver.quit()
    """
    #self.assertIn("askfm", self.driver.current_url)
    @classmethod
    def tearDownClass(cls):
        # close the browser window
        cls.driver.quit()
    """
if __name__ == "__main__":
    unittest.main()-v
