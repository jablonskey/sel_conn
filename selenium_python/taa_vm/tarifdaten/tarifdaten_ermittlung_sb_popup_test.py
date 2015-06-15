# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

from service.helpers import Helper
from service.common_tasks import CommonTasks
import unittest, time, re, sys


class TarifdatenEmittlungSbPopupTest(unittest.TestCase, CommonTasks, Helper):

    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(30)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_400_popup_behavior(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler(None, "400", 1)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler(None, "400", 2)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler(None, "400", 3)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler(None, "400", 3)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "400", 4)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "400", 3)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "400", 3, "checked")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler(None, "400", None, "checked")
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[2]/div[4]/label)")

        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_400_check_sb_combo_with_chosen_option(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "400", 1, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "400", 2, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "400", 3, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "400", 4, "checked")

    def test_1000_popup_behavior(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("selbstandige", "10")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", 1)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", 2)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", 3)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", 4)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", 4)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "1000", 5)
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "1000", 4)
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.tarifdaten_ermittlung_alert_handler(None, "1000", 4, "checked")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))
        self.check_and_click_element_by_xpath(self.TARIFDATEN_SB_POPUP_ABBRECHEN_BUTTON_XPATH)

        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler(None, "1000", None, "checked")
        try:
            WebDriverWait(self.driver, 10).until_not(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.check_and_click_element_by_xpath("(/html/body/div[3]/div/div/div[2]/div[4]/label)")
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, Helper.TARIFDATEN_SB_POPUP_UBERNAHMEN_BUTTON_XPATH)))
        except AssertionError as e:
            self.verificationErrors.append(str(e))

    def test_1000_check_sb_combo_with_chosen_option(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("selbstandige", "10")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "1000", 1, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "1000", 2, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "1000", 3, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "1000", 4, "checked")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURAFIRM")
        self.tarifdaten_ermittlung_alert_handler("ubernahmen", "1000", 5, "checked")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()

