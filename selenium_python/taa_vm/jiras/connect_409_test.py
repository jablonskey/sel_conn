# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from service.common_tasks import CommonTasks
from service.helpers import Helper
import unittest, time, re


class Connect409Test(unittest.TestCase, CommonTasks, Helper):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect409(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element(
                (By.XPATH, self.TARIFDATEN_GESAMTBTR_LABEL_XPATH),
                u" jährlich:"))


        WebDriverWait(self.driver, 10).until_not(
            EC.text_to_be_present_in_element_value((By.XPATH, self.TARIFDATEN_GESAMTBTR_LABEL_XPATH), u"jährlich:"))

        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")

        try:
            self.assertEqual(self.get_tarifdaten_gesambeitrag_price(),
                                self.get_price_from_table_num("mitgliedschaft", 1) +
                                self.get_price_from_table_num("rechtschutz", 1))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_select_produkt_from_rechtschutz("Privat- und Berufs-RS")

        try:
            self.assertEqual(self.get_tarifdaten_gesambeitrag_price(),
                                self.get_price_from_table_num("mitgliedschaft", 1) +
                                self.get_price_from_table_num("rechtschutz", 3))
        except AssertionError as e:
            self.verificationErrors.append(str(e))



        def tearDown(self):
            self.driver.quit()
            self.assertEqual([], self.verificationErrors)


    if __name__ == "__main__":
        unittest.main()
