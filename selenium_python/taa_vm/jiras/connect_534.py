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


class Connect534Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect534(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()

        # ### Antragstellerdaten ###
        self.antragsteller_fill_data_antragstellerdaten(taetigkeit="nicht berufstätig")

        self.assertEqual("",
                         Select(driver.find_element_by_id("titel")).options[0].text)

        try:
            self.assertFalse(driver.find_element_by_id("berufsgruppe").is_enabled())
        except AssertionError as e:
            self.verificationErrors.append("Field berufsgruppe enabled")

        try:
            self.assertEqual(Select(driver.find_element_by_id("berufsgruppe")).options[
                                 int(driver.find_element_by_id("berufsgruppe").get_attribute("value"))-1].text,
                             "Sonstige Berufsgruppe")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field berufsgruppe \ \"" + Select(driver.find_element_by_id("berfusgruppe")).options[
                    int(driver.find_element_by_id("berufsgruppe").get_attribute(
                        "value"))-1].text + "\" instead of \"Sonstige Berufsgruppe\"")

        self.antragsteller_fill_data_lebenspartner(taetigkeit="nicht berufstätig")

        try:
            self.assertFalse(driver.find_element_by_id("lebenspartner-berufsgruppe").is_enabled())
        except AssertionError as e:
            self.verificationErrors.append("Field lebenspartner-berufsgruppe enabled")

        try:
            self.assertEqual(Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[
                                 int(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute("value"))-1].text,
                             "Sonstige Berufsgruppe")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field berufsgruppe \ \"" + Select(driver.find_element_by_id("lebenspartner-berfusgruppe")).options[
                    int(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute(
                        "value"))-1].text + "\" instead of \"Sonstige Berufsgruppe\"")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
