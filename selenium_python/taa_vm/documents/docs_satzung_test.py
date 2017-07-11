# -*- coding: utf-8 -*-
import os
import unittest

from nose.plugins.attrib import attr
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service.common_tasks import CommonTasks


@attr('documents')
class DocsSatzungTests(unittest.TestCase, CommonTasks):
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

    def test_docs_satzung_on_tarifdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")

        self.documents_popup_generate_document((u"Vertragsgrundlagen Club (Satzung)",))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])"),

                                             u"Satzung"))

    def test_docs_satzung_on_antragsteller(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()

        self.documents_popup_generate_document((u"Vertragsgrundlagen Club (Satzung)",))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])"),

                                             u"Satzung"))

    def test_docs_satzung_on_zusatzdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()

        driver.find_element_by_xpath("//input[@placeholder=\"Kennzeichen\"]").send_keys("kenn123")
        self.documents_popup_generate_document((u"Vertragsgrundlagen Club (Satzung)",))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])"),

                                             u"Satzung"))

    def test_docs_satzung_on_antrag(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.click_weiter_on_zielgruppe_go_to_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="250 EUR")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.click_weiter_on_tarifdaten_go_to_antragstellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.click_weiter_on_antragsteller_go_to_zusatzdaten()

        driver.find_element_by_xpath("//input[@placeholder=\"Kennzeichen\"]").send_keys("kenn123")
        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/form/div/div[1]/div[2]/label/input)")
        self.click_weiter_on_zusatzdaten_go_to_antrag()

        self.documents_popup_generate_document((u"Vertragsgrundlagen Club (Satzung)",))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div[1]/div[2]/div[796])"),

                                             u"Satzung"))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
