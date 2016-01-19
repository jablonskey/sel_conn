# -*- coding: utf-8 -*-
from selenium import webdriver
import os
import unittest, time, re
from service import common_tasks
from selenium.webdriver.support.ui import Select

class ZielgruppeVmnrComboTest(unittest.TestCase, common_tasks.CommonTasks):

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
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_zielgruppe_vmnr_combo(self):
        driver = self.driver
        vmnr_number = "100063"

        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).select_by_visible_text(vmnr_number)
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR combo empty")

        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertEqual(Select(self.driver.find_element_by_xpath(self.ZIELGRUPPE_VMNR_COMBO_XPATH)).first_selected_option.text, vmnr_number)
        except AssertionError as e:
            self.verificationErrors.append("VMNR combo empty")

        self.zielgruppe_weiter_tarifdaten()


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
