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


class Connect794Test(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect794(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()

        self.neues_angebot_helper(button_to_click="ok")
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_check_default_antragstellerdaten()
        self.antragsteller_check_default_kontaktdaten()
        self.antragsteller_check_default_lebenspartner()
        self.antragsteller_check_default_zahlungsdaten()
        self.antragsteller_check_default_vorversicherung()



    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
