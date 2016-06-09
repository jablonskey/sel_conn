# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service.common_tasks import CommonTasks


class DocsFehlendeAngabenTests(unittest.TestCase, CommonTasks):


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
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_docs_fehlende_angaben_on_tarifdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        main_window = driver.current_window_handle
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")

        self.documents_popup_generate_document((u"fehlende Angaben für Antrag", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)

        document_tab = driver.window_handles[-1]
        driver.switch_to.window(document_tab)

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])"),

                                             u"Fehlende Angaben"))

        driver.close()
        driver.switch_to.window(main_window)
        driver.close()

    def test_docs_fehlende_angaben_on_antragsteller(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        main_window = driver.current_window_handle
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.tarifdaten_weiter_antrastellerdaten()

        self.documents_popup_generate_document((u"fehlende Angaben für Antrag", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        document_tab = driver.window_handles[-1]
        driver.switch_to.window(document_tab)

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])"),

                                             u"Fehlende Angaben"))

        driver.close()
        driver.switch_to.window(main_window)
        driver.close()

    def test_docs_fehlende_angaben_on_zusatzdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        main_window = driver.current_window_handle
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()

        driver.find_element_by_xpath("//input[@placeholder=\"Kennzeichen\"]").send_keys("kenn123")
        self.documents_popup_generate_document((u"fehlende Angaben für Antrag", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        document_tab = driver.window_handles[-1]
        driver.switch_to.window(document_tab)

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[1])"),

                                             u"Fehlende Angaben"))

        driver.close()
        driver.switch_to.window(main_window)
        driver.close()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
