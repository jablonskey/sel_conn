# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service.common_tasks import CommonTasks
from service.helpers import Helper


class Connect415Test(unittest.TestCase, CommonTasks, Helper):
    def setUp(self):
        print os.environ.get('SELENIUM_BROWSER')
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

    def test_connect415(self):
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

        erganzungen_produkts_jurprivat = driver.find_elements_by_xpath(
            self.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)

        erganzungen_labels_jurprivat = []
        for e in erganzungen_produkts_jurprivat:
            erganzungen_labels_jurprivat.append(e.text)

        # region first_selected_erganz
        first_selected_erganz = self.tarifdaten_select_produkt_from_erganzungen_by_list_position(1)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_XPATH)))

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Helper.ERGANZUNGEN_POPUP_PRODUKT_LABELS_XPATH)))

        self.tarifdaten_select_produkt_on_daten_erfassen_popup_by_list_position(1)

        anzahl_fields = driver.find_elements_by_name("intItem")
        anzahl_fields[0].send_keys("10")
        self.check_and_click_element_by_xpath(self.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)
        self.tarifdaten_wait_for_price_reload()

        fourth_selected_erganz = self.tarifdaten_select_produkt_from_erganzungen_by_list_position(4)
        self.tarifdaten_wait_for_price_reload()
        self.tarifdaten_select_produkt_from_rechtschutz("Privat- und Verkehrs-RS")

        WebDriverWait(driver, 10).until_not(
            EC.text_to_be_present_in_element((By.XPATH, self.get_tarifdaten_erganzungen_label_xpath(4)),
                                             fourth_selected_erganz))
        self.tarifdaten_wait_for_price_reload()

        erganzungen_produkts_privat_berufs = driver.find_elements_by_xpath(
            self.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)
        erganzungen_labels_privat_berufs = []
        for e in erganzungen_produkts_privat_berufs:
            erganzungen_labels_privat_berufs.append(e.text)
        self.assertNotEqual(erganzungen_labels_jurprivat, erganzungen_labels_privat_berufs)

        self.tarifdaten_select_produkt_from_erganzungen_by_name("Spezial-Straf-RS")
        self.tarifdaten_wait_for_price_reload()

        self.tarifdaten_select_produkt_from_rechtschutz("JURPRIVAT")
        WebDriverWait(driver, 10).until_not(
            EC.text_to_be_present_in_element((By.XPATH, self.get_tarifdaten_erganzungen_label_xpath(4)),
                                             erganzungen_labels_privat_berufs[3]))
        self.tarifdaten_wait_for_price_reload()

        erganzungen_produkts_jurprivat_2 = driver.find_elements_by_xpath(
            self.TARIFDATEN_PRODUKT_ELEMENTS_LABELS_ERGANZUNGEN_XPATH)

        erganzungen_labels_jurprivat_2 = []
        for e in erganzungen_produkts_jurprivat_2:
            erganzungen_labels_jurprivat_2.append(e.text)

        self.assertEqual(erganzungen_labels_jurprivat, erganzungen_labels_jurprivat_2)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
