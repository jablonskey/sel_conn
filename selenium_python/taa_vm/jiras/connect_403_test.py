# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
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
                self.driver = webdriver.Ie()
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
        self.open_taa_vm()
        driver.implicitly_wait(2)
        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()

        # ### Antragstellerdaten ###
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_lebenspartner()
        self.antragsteller_fill_data_lebenspartner_anschrift()
        self.antragsteller_fill_data_zahlungsdaten("uberweisung")
        self.antragsteller_fill_data_vorversicherung("nein")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))

        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])").text,
                             "Ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])").text + "\" instead of \"Ja\"")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))

        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])").text,
                             "Ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])").text + "\" instead of \"Ja\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_fill_data_lebenspartner()
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        # Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])").text,
                             "Nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])").text + "\" instead of \"Nein\"")
        #Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])").text,
                             "Ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])").text + "\" instead of \"Ja\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_fill_data_lebenspartner(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        #Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])").text,
                             "Nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])").text + "\" instead of \"Nein\"")
        #Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])").text,
                             "Nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])").text + "\" instead of \"Nein\"")

        self.antrag_zuruck_zusatzdaten()
        self.zusatzdaten_zuruck_antrastellerdaten()
        self.antragsteller_fill_data_antragstellerdaten()
        self.antragsteller_fill_data_lebenspartner(berufsgruppe="Sonstige Berufsgruppe")
        self.antragsteller_weiter_zusatzdaten()
        self.zusatzdaten_weiter_antrag()

        #Antragsteller ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[1])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])").text,
                             "Ja")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Antragsteller: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[2])").text + "\" instead of \"Ja\"")
        #Lebens ja/nein
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located(
            (By.XPATH, "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[2])")))
        try:
            self.assertEqual(driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])").text,
                             "Nein")
        except AssertionError:
            self.verificationErrors.append("Antrag \ Lebenspartner: \"" + driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[1]/div[1]/div[2]/ul/li[8]/span[3]/span[1])").text + "\" instead of \"Nein\"")

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
