# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from service.common_tasks import CommonTasks


class LoginRefreshTests(unittest.TestCase, CommonTasks):


    def setUp(self):

        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login_logout_refresh_login(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        # self.open_taa_vm()
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath(self.VERMITTLER_IFRAME_LOGOUT_XPATH)
        driver.switch_to_default_content()
        driver.refresh()
        self.login_to_connect_vermittler(self.base_url)

    def test_passwort_vergessen_login(self):

        driver = self.driver
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Passwort vergessen")
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath(self.VERMITTLER_IFRAME_LOGIN_XPATH)
        driver.switch_to_default_content()
        self.login_to_connect_vermittler(self.base_url)

    def test_registrieren_login(self):

        driver = self.driver
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text("Registrieren")
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath(self.VERMITTLER_IFRAME_LOGIN_XPATH)
        driver.switch_to_default_content()
        self.login_to_connect_vermittler(self.base_url)

    def test_anmeldung_fur_nutzer_erstellen_login(self):

        driver = self.driver
        self.go_to_vermittler_login_page(self.base_url)
        self.check_and_click_element_by_link_text(u"Anmeldung für Nutzer des bisherigen Dokumentenzugriffs")
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        self.check_and_click_element_by_xpath(self.VERMITTLER_IFRAME_LOGIN_XPATH)
        driver.switch_to_default_content()
        self.login_to_connect_vermittler(self.base_url)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
