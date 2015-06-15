# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from service.common_tasks import CommonTasks


class DocsKurzangebotTests(unittest.TestCase, CommonTasks):


    def setUp(self):

        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_docs_kurzangebot_on_tarifdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        self.check_and_click_element_by_name("mitgliedschaft")
        Select(driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div/div/div[2]/table[1]/tbody/tr[1]/td[8]/select)")).select_by_visible_text(
            "ohne SB")
        self.check_and_click_element_by_name("rechtschutz")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[1]/h4)"), u"Ergänzungen"))

        self.documents_popup_generate_document((u"Kurzangebot", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])"),

                                             u"Vorschlag für Ihre KS/AUXILIA Rechtsschutz-Versicherung"))

    def test_docs_kurzangebot_on_antragsteller(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        self.check_and_click_element_by_name("mitgliedschaft")
        Select(driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div/div/div[2]/table[1]/tbody/tr[1]/td[8]/select)")).select_by_visible_text(
            "ohne SB")
        self.check_and_click_element_by_name("rechtschutz")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[1]/h4)"), u"Ergänzungen"))

        self.tarifdaten_weiter_antrastellerdaten()

        self.documents_popup_generate_document((u"Kurzangebot", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[2])"),

                                             u"Vorschlag für Ihre KS/AUXILIA Rechtsschutz-Versicherung"))

    def test_docs_kurzangebot_on_zusatzdaten(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

        self.check_and_click_element_by_name("mitgliedschaft")
        Select(driver.find_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[4]/div/div/div[2]/table[1]/tbody/tr[1]/td[8]/select)")).select_by_visible_text(
            "ohne SB")
        self.check_and_click_element_by_name("rechtschutz")
        WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[5]/div/div/div[1]/h4)"), u"Ergänzungen"))

        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()
        driver.find_element_by_xpath("//input[@placeholder=\"Kennzeichen\"]").send_keys("kenn123")
        self.documents_popup_generate_document((u"Kurzangebot", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[3])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[3])"),
                                             u"Vorschlag für Ihre KS/AUXILIA Rechtsschutz-Versicherung"))

        #endregion

    def test_docs_kurzangebot_on_antrag(self):

        driver = self.driver

        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.driver.implicitly_wait(2)
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_select_sb_for_produkt_from_rechtschutz(produkt_name="JURPRIVAT", sb="ohne SB")
        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data()
        self.antragsteller_weiter_zusatzdaten()

        driver.find_element_by_xpath("//input[@placeholder=\"Kennzeichen\"]").send_keys("kenn123")
        self.check_and_click_element_by_xpath("(/html/body/div/div/div/section/div/div[2]/div/form/div/div[2]/div[2]/form/div/div[1]/div[2]/label/input)")
        self.zusatzdaten_weiter_antrag()

        self.documents_popup_generate_document((u"Kurzangebot", ))

        WebDriverWait(driver, 10).until_not(self.no_more_than_one_window_open)
        driver.switch_to.window(driver.window_handles[-1])

        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[3])")))
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.XPATH, "(/html/body/div[1]/div[2]/div[4]/div/div/div[2]/div[3])"),

                                             u"Vorschlag für Ihre KS/AUXILIA Rechtsschutz-Versicherung"))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
