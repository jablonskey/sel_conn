# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import Select

from service import common_tasks


class Connect534Test(unittest.TestCase, common_tasks.CommonTasks):
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
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect534(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.go_to_rechner()
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
                                 int(driver.find_element_by_id("berufsgruppe").get_attribute("value"))].text,
                             "Sonstige Berufsgruppe")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field berufsgruppe \ \"" + Select(driver.find_element_by_id("berufsgruppe")).options[
                    int(driver.find_element_by_id("berufsgruppe").get_attribute(
                        "value"))].text + "\" instead of \"Sonstige Berufsgruppe\"")

        self.antragsteller_fill_data_lebenspartner(taetigkeit="nicht berufstätig")

        try:
            self.assertFalse(driver.find_element_by_id("lebenspartner-berufsgruppe").is_enabled())
        except AssertionError as e:
            self.verificationErrors.append("Field lebenspartner-berufsgruppe enabled")

        try:
            self.assertEqual(Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[
                                 int(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute(
                                     "value"))].text,
                             "Sonstige Berufsgruppe")
        except AssertionError as e:
            self.verificationErrors.append(
                "Field berufsgruppe \ \"" + Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[
                    int(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute(
                        "value"))].text + "\" instead of \"Sonstige Berufsgruppe\"")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
