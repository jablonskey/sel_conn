# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

from service import common_tasks


class Connect11522Test(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_connect1152(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_zahlungsdaten(zahlungsart="uberweisung")
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_zuruck_on_antragsteller_go_tarifdaten()
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_LEBENSPARTNER_J_N_HELPER["nein"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ lebenspartner should not be selected")
        try:
            self.assertTrue(self.driver.find_element_by_xpath(
                self.ANTRAGSTELLER_ZAHLUNGSDATEN_ZAHLUNGSART_HELPER["uberweisung"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append(str(e) + "\\ uberweisung not selected")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
