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


class Connect720Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        self.profile = webdriver.FirefoxProfile()
        self.profile.native_events_enabled = False
        self.driver = webdriver.Firefox(self.profile)
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect720(self):
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
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("1")
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("1")
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(e)

        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("0")
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("0")

        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("4")
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("5")
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("6")
        try:
            self.assertEqual("1", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("7")
        try:
            self.assertEqual("2", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("8")
        try:
            self.assertEqual("2", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("9")
        try:
            self.assertEqual("2", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("10")
        try:
            self.assertEqual("2", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("11")
        try:
            self.assertEqual("3", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("12")
        try:
            self.assertEqual("3", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("13")
        try:
            self.assertEqual("3", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("14")
        try:
            self.assertEqual("3", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("15")
        try:
            self.assertEqual("4", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

        driver.find_element_by_xpath("(//input[@type='text'])[8]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[8]").send_keys("16")
        try:
            self.assertEqual("4", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        except AssertionError as e:
            self.verificationErrors.append(u"%s; Geringfugig: %s, Anzahl %s" % (
                e, driver.find_element_by_xpath("(//input[@type='text'])[8]").get_attribute("value"),
                driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value")))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
__author__ = 'Jablonski'
