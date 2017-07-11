# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class ZielgruppeVmnrComboTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_zielgruppe_vmnr_combo(self):
        driver = self.driver
        vmnr_number = "100063"

        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_enter_vmnr(vmnr_number)
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_FORM_AFTER_CLICK_XPATH).text,
                             vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR combo empty")

        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.click_zuruck_on_tarifdaten_go_to_zielgruppe()

        try:
            self.assertEqual(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_FORM_AFTER_CLICK_XPATH).text,
                             vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR combo empty")

        self.click_weiter_on_zielgruppe_go_to_tarifdaten()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
