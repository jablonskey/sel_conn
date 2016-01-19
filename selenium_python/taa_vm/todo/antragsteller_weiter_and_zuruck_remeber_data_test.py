# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException

from service import common_tasks


class AntragstellerAntragstellerdatenValidationTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        print os.environ.get('SELENIUM_BROWSER')
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
        self.driver.maximize_window()

        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_antragsteller_antragstellerdaten_validation(self):
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
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_lebenspartner()
        self.antragsteller_fill_data_lebenspartner_anschrift()
        self.antragsteller_fill_data_zahlungsdaten("nein")
        self.antragsteller_fill_data_vorversicherung("nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()

        self.antragsteller_fill_data_antragstellerdaten()




    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException, e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
