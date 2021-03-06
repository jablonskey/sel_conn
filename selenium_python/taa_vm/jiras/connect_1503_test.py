# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0


from service import common_tasks
from service.helpers import Helper

class Connect1503Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        if os.environ.has_key("SELENIUM_BROWSER"):
            if os.environ['SELENIUM_BROWSER'] == "chrome":
                self.driver = webdriver.Chrome()
            elif os.environ['SELENIUM_BROWSER'] == "ie":
                caps = DesiredCapabilities.INTERNETEXPLORER
                caps['ignoreZoomSetting'] = True
                self.driver = webdriver.Ie(capabilities=caps)
            elif os.environ['SELENIUM_BROWSER'] == "firefox":
                profile = webdriver.FirefoxProfile()
                profile.native_events_enabled = False
                self.driver = webdriver.Firefox(profile)
        else:
            profile = webdriver.FirefoxProfile()
            profile.native_events_enabled = False
            self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    @unittest.skip("default aktservice credentials issue")
    def test_login_aktservice_then_go_to_vermittler(self):
        driver = self.driver
        self.login_to_aktservice(self.base_url)
        self.go_to_vermittler_login_page(self.base_url)
        self.driver.switch_to.frame(self.driver.find_element_by_tag_name("iframe"))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))

    @unittest.skip("default aktservice credentials issue")
    def test_login_aktservice_then_go_to_admin(self):
        driver = self.driver
        self.login_to_aktservice(self.base_url)
        self.go_to_admin_panel_page(self.base_url)
        self.assertFalse(self.is_element_present(By.LINK_TEXT, "Logout"))

    @unittest.skip("default aktservice credentials issue")
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
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))

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
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.VERMITTLER_IFRAME_ANMELDEN_XPATH)))

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
