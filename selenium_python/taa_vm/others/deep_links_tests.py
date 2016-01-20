import os

from selenium import webdriver
import unittest
from service import common_tasks
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.common.by import By


class DeepLinksTests(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):

        if os.environ.has_key("SELENIUM_BROWSER"):
            if os.environ['SELENIUM_BROWSER'] == "chrome":
                self.driver = webdriver.Chrome()
            elif os.environ['SELENIUM_BROWSER'] == "ie":
                self.driver = webdriver.Ie()
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

    def test_deep_link_vermittler_login(self):
        driver = self.driver
        self.driver.get(self.base_url + self.STARTSEITE_ADDRES_COMPLETION + "?username=%s&password=%s" % (
            self.VERMITTLER_USER_LOGIN, self.VERMITTLER_USER_PASSWORD))
        self.check_if_on_vermittler_main_page()

    def test_deep_link_vermittler_login_correct_user_no_passwd(self):
        driver = self.driver
        self.driver.get(self.base_url + self.STARTSEITE_ADDRES_COMPLETION + "?username=%s" % (
            self.VERMITTLER_USER_LOGIN))
        self.check_if_on_vermittler_login_page()

    def test_deep_link_vermittler_login_correct_user_wrong_passwd(self):
        driver = self.driver
        self.driver.get(self.base_url + self.STARTSEITE_ADDRES_COMPLETION + "?username=%s&password=%s" % (
            self.VERMITTLER_USER_LOGIN, "wrong_password"))
        self.check_if_on_vermittler_login_page()

    def test_deep_link_to_rechner(self):
        driver = self.driver
        self.driver.get(self.base_url + self.ZIELGRUPPE_ADDRES_COMPLETION + "?username=%s&password=%s" % (
            self.VERMITTLER_USER_LOGIN, self.VERMITTLER_USER_PASSWORD))
        self.check_if_on_zielgruppe_page()

    def test_deep_link_to_kundensuche(self):
        driver = self.driver
        self.driver.get(self.base_url + self.KUNDENSUCHE_ADDRES_COMPLETION + "?username=%s&password=%s&search=%s" % (
            self.VERMITTLER_USER_LOGIN, self.VERMITTLER_USER_PASSWORD, "text_to_search"))
        self.check_if_on_kundensuche_page()

    def test_deep_link_to_mitgliedschaft(self):
        driver = self.driver
        self.driver.get(self.base_url + self.MITGLIEDSCHAFT_ADDRES_COMPLETION + "%s?username=%s&password=%s" % (
            "3137873000", self.VERMITTLER_USER_LOGIN, self.VERMITTLER_USER_PASSWORD))
        self.check_if_on_mitgliedschaft_page(u"3137873000")

    def test_meine_angebote_then_login(self):
        driver = self.driver
        self.driver.get(self.base_url + self.MEINE_ANGEBOTE_ADDRES_COMPLETION)
        self.check_if_on_vermittler_login_page()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.VERMITTLER_USER_LOGIN)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.VERMITTLER_USER_PASSWORD)
        self.check_and_click_element_by_xpath(self.VERMITTLER_LOGIN_BUTTON_XPATH)
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, self.CURRENT_PAGE_MAIN_HEADER), "Login"))
        self.check_if_on_meine_angebote_page()

    def test_mein_profil_then_login(self):
        driver = self.driver
        self.driver.get(self.base_url + self.MEIN_PROFIL_ADDRESS_COMPLETION)
        self.check_if_on_vermittler_login_page()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.VERMITTLER_USER_LOGIN)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.VERMITTLER_USER_PASSWORD)
        self.check_and_click_element_by_xpath(self.VERMITTLER_LOGIN_BUTTON_XPATH)
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, self.CURRENT_PAGE_MAIN_HEADER), "Login"))
        self.check_if_on_mein_profil_page()

    def test_kundensuche_then_login(self):
        driver = self.driver
        self.driver.get(self.base_url + self.KUNDENSUCHE_ADDRES_COMPLETION)
        self.check_if_on_vermittler_login_page()
        self.driver.find_element_by_id("username").clear()
        self.driver.find_element_by_id("username").send_keys(self.VERMITTLER_USER_LOGIN)
        self.driver.find_element_by_id("password").clear()
        self.driver.find_element_by_id("password").send_keys(self.VERMITTLER_USER_PASSWORD)
        self.check_and_click_element_by_xpath(self.VERMITTLER_LOGIN_BUTTON_XPATH)
        WebDriverWait(self.driver, 20).until_not(EC.text_to_be_present_in_element(
            (By.XPATH, self.CURRENT_PAGE_MAIN_HEADER), "Login"))
        self.check_if_on_kundensuche_page()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
