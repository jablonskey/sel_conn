# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from service import common_tasks
import unittest, time, re


class Connect11522Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
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
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz("JURPRIVAT", "ohne SB")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_zahlungsdaten(zahlungsart="uberweisung")
        self.antragsteller_fill_data_lebenspartner(ja_nein="nein")
        self.antragsteller_zuruck_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
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
