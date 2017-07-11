# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service.common_tasks import CommonTasks


class SpeichernUnterTest(unittest.TestCase, CommonTasks):
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
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_specihern_unter_abbrechen_on_all_tabs(self):

        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()
        self.speichern_unter_helper(button_to_click="abbrechen")
        self.click_weiter_on_zusatzdaten_go_to_antrag()
        self.speichern_unter_helper(button_to_click="abbrechen")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
