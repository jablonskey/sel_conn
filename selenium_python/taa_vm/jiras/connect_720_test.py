# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class Connect720Test(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_connect720(self):
        self.Maxdiff = None
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("selbstandige")

        # -- Selbstandinge/Firmen/Freiberufler

        # -- Berechnungshilfe popup
        self.check_and_click_element_by_link_text("Berechnungshilfe")
        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("Berechnungshilfe", driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['vollzeitmitarbeiter']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['vollzeitmitarbeiter']["form_xpath"]).send_keys("1")
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['teilzeitmitarbeiter']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['teilzeitmitarbeiter']["form_xpath"]).send_keys("1")
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['teilzeitmitarbeiter']["form_xpath"]).clear()
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['vollzeitmitarbeiter']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['vollzeitmitarbeiter']["form_xpath"]).send_keys("0")
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['teilzeitmitarbeiter']["form_xpath"]).send_keys("0")

        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("4")
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("5")
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("6")
        try:
            self.assertEqual("1", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("7")
        try:
            self.assertEqual("2", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("8")
        try:
            self.assertEqual("2", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("9")
        try:
            self.assertEqual("2", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("10")
        try:
            self.assertEqual("2", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("11")
        try:
            self.assertEqual("3", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("12")
        try:
            self.assertEqual("3", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("13")
        try:
            self.assertEqual("3", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("14")
        try:
            self.assertEqual("3", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("15")
        try:
            self.assertEqual("4", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).clear()
        driver.find_element_by_xpath(
            self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).send_keys("16")
        try:
            self.assertEqual("4", driver.find_element_by_xpath(
                self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['geringfugig']["form_xpath"]).get_attribute("value"),
                driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BERECHNUNGSHILFE_POPUP_HELPER['anzahl']["form_xpath"]).get_attribute("value")))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
