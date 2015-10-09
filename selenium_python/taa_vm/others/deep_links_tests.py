from selenium import webdriver
import unittest, time, re
from service import common_tasks
from selenium.webdriver.support.ui import Select


class DeepLinksTests(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
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


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
