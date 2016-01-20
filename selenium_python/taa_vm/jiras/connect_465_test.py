# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service.common_tasks import CommonTasks
from service.helpers import Helper


class Connect465Test(unittest.TestCase, CommonTasks):
    def setUp(self):

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
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_connect465(self):
        driver = self.driver
        driver.maximize_window()

        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name('familien')
        self.zielgruppe_weiter_tarifdaten()

        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")

        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, Helper.ERGANZUNGEN_HEADER_XPATH), u"Ergänzungen"))

        self.tarifdaten_select_produkt_from_erganzungen_by_name("Kleinunternehmer-Rechtsschutz")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))

        self.check_and_click_element_by_xpath(Helper.ERGANZUNGEN_CHECKBOX_XPATH)
        self.check_and_click_element_by_xpath(Helper.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)

        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))

        self.tarifdaten_select_produkt_from_erganzungen_by_name("Selbstgenutzte Immobilien")
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))
        self.tarifdaten_select_produkt_on_daten_erfassen_popup_by_name("Garagen als Einzelrisiko")
        driver.find_elements_by_name("intItem")[0].send_keys("10")
        self.check_and_click_element_by_xpath(self.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)

        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))

        self.tarifdaten_weiter_antrastellerdaten()

        antragstellerdaten_produktauswahl_list = [l.text for l in
                                                  driver.find_elements_by_xpath(
                                                      self.PRODUKTAUSWAHL_ELEMENTS_LABEL_XPATH)]

        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()

        zusatzdaten_produktauswahl_list = [l.text for l in
                                           driver.find_elements_by_xpath(self.PRODUKTAUSWAHL_ELEMENTS_LABEL_XPATH)]

        self.assertEqual(antragstellerdaten_produktauswahl_list, zusatzdaten_produktauswahl_list)

        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/form/div/div[1]/div[2]/label/input)")

        self.zusatzdaten_weiter_antrag()

        antrag_produktauswahl_list = [l.text for l in
                                      driver.find_elements_by_xpath(self.PRODUKTAUSWAHL_ELEMENTS_LABEL_XPATH)]

        self.assertEqual(zusatzdaten_produktauswahl_list, antrag_produktauswahl_list)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
