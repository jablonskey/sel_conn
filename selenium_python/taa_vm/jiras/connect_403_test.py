# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class Connect403Test(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_connect403(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.go_to_rechner()
        driver.implicitly_wait(2)
        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()

        # ### Antragstellerdaten ###
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_lebenspartner()
        self.antragsteller_fill_data_zahlungsdaten("uberweisung")
        self.antragsteller_fill_data_vorversicherung("nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))

        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH).text,
                             "ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH).text + "\" instead of \"ja\"")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))

        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH).text,
                             "ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH).text + "\" instead of \"ja\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_fill_data_lebenspartner()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        # Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH).text,
                             "nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH).text + "\" instead of \"nein\"")
        # Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH).text,
                             "ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH).text + "\" instead of \"ja\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_fill_data_lebenspartner(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        # Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH).text,
                             "nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH).text + "\" instead of \"nein\"")
        # Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH).text,
                             "nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH).text + "\" instead of \"nein\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_lebenspartner(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        # Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_ANTRAGSTELLER_NEIN_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH).text,
                             "ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                self.ANTRAG_ANTRAGSTELLER_JA_PARAGRAPH).text + "\" instead of \"ja\"")
        # Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH)))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, self.ANTRAG_LEBENSPARTNER_JA_PARAGRAPH)))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH).text,
                             "nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                self.ANTRAG_LEBENSPARTNER_NEIN_PARAGRAPH).text + "\" instead of \"nein\"")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
