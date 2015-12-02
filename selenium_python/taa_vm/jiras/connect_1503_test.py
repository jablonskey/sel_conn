# -*- coding: utf-8 -*-
import unittest
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from service import common_tasks


class Connect1503Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.native_events_enabled = False
        self.driver = webdriver.Firefox(self.profile)
        self.driver.maximize_window()


        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_aktservice_then_go_to_vermittler(self):
        driver = self.driver
        self.login_to_aktservice(self.base_url)
        self.go_to_vermittler_login_page(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.assertNotEqual("Logout", driver.find_element_by_xpath(self.VERMITTLER_IFRAME_LOGOUT_XPATH))

    def test_login_aktservice_then_go_to_admin(self):
        driver = self.driver
        self.login_to_aktservice(self.base_url)
        self.go_to_admin_panel_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_aktservice_then_go_to_ses(self):
        driver = self.driver
        self.login_to_aktservice(self.base_url)
        self.go_to_secure_email_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_admin_then_go_to_vermittler(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)
        self.go_to_vermittler_login_page(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.assertNotEqual("Logout", driver.find_element_by_xpath(self.VERMITTLER_IFRAME_LOGOUT_XPATH))

    def test_login_admin_then_go_to_aktservice(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)
        self.go_to_aktservice_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_admin_then_go_to_ses(self):
        driver = self.driver
        self.login_to_admin_panel(self.base_url)
        self.go_to_secure_email_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_vermitler_then_go_to_admin(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_admin_panel_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_vermitler_then_go_to_aktservice(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_aktservice_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_vermitler_then_go_to_ses(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_secure_email_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_ses_then_go_to_vermittler(self):
        driver = self.driver
        self.login_to_secure_email(self.base_url)
        self.go_to_vermittler_login_page(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        self.assertNotEqual("Logout", driver.find_element_by_xpath(self.VERMITTLER_IFRAME_LOGOUT_XPATH))

    def test_login_ses_then_go_to_admin(self):
        driver = self.driver
        self.login_to_secure_email(self.base_url)
        self.go_to_admin_panel_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    def test_login_ses_then_go_to_aktservice(self):
        driver = self.driver
        self.login_to_secure_email(self.base_url)
        self.go_to_aktservice_login_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
