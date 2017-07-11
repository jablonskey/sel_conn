# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service.common_tasks import CommonTasks
from service.helpers import Helper


class TarifdatenDatenErfassenSbPopupTest(unittest.TestCase, CommonTasks, Helper):
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

    def test_daten_erfassen_mandatory_risiko_not_filled_test(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.ERGANZUNGEN_HEADER_XPATH), u"Ergänzungen"))
        self.tarifdaten_select_produkt_from_erganzungen_by_name("Vermietung & Verpachtung")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_XPATH)))
        self.tarifdaten_select_produkt_on_daten_erfassen_popup_by_name(
            u"Wohneinheiten bis 12.000 EUR Jahresbruttomiete")
        self.check_and_click_element_by_xpath(self.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT)))
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT),
                                             u"Bitte ergänzen Sie die fehlenden Angaben."))

    def test_daten_erfassen_mandatory_risiko_filled_test(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz(u"JURPRIVAT")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.ERGANZUNGEN_HEADER_XPATH), u"Ergänzungen"))
        self.tarifdaten_select_produkt_from_erganzungen_by_name("Vermietung & Verpachtung")
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_XPATH)))
        self.tarifdaten_select_produkt_on_daten_erfassen_popup_by_name(
            u"Wohneinheiten bis 12.000 EUR Jahresbruttomiete")
        self.check_and_click_element_by_xpath(self.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT)))
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, self.ERGANZUNGEN_POPUP_VALIDATION_ALERT),
                                             u"Bitte ergänzen Sie die fehlenden Angaben."))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
