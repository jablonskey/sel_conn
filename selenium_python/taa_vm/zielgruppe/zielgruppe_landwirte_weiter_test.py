# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks
from service.helpers import Helper


class ZielgruppeLandwirteTest(unittest.TestCase, common_tasks.CommonTasks, Helper):
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
        self.driver.implicitly_wait(0)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_zielgruppe_landwirte(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        landwirte_anzahl = 10

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("landwirte")

        mitglied_ja = driver.find_element_by_name("isLandwirteMitglied")
        mitglied_nein = driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]")
        gewerbe_ja = driver.find_element_by_name("isLandwirteGewerbe")
        gewerbe_nein = driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")

        self.assertFalse(mitglied_ja.is_selected())
        self.assertFalse(mitglied_nein.is_selected())
        self.assertFalse(gewerbe_ja.is_selected())
        self.assertFalse(gewerbe_nein.is_selected())

        # -- JA JA
        mitglied_ja.click()
        self.assertTrue(mitglied_ja.is_selected())

        gewerbe_ja.click()
        self.assertTrue(gewerbe_ja.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()

        self.assertFalse(mitglied_ja.is_selected())
        self.assertFalse(mitglied_nein.is_selected())
        self.assertFalse(gewerbe_ja.is_selected())
        self.assertFalse(gewerbe_nein.is_selected())

        # -- Nein Ja
        mitglied_nein.click()
        self.assertTrue(mitglied_nein.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()
        self.assertFalse(mitglied_nein.is_selected())

        gewerbe_ja.click()
        self.assertTrue(gewerbe_ja.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()

        mitglied_nein.click()
        self.assertTrue(mitglied_nein.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()

        self.assertFalse(mitglied_ja.is_selected())
        self.assertFalse(mitglied_nein.is_selected())
        self.assertFalse(gewerbe_ja.is_selected())
        self.assertFalse(gewerbe_nein.is_selected())

        # -- Nein Nein
        mitglied_nein.click()
        self.assertTrue(mitglied_nein.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()
        self.assertFalse(mitglied_nein.is_selected())

        gewerbe_nein.click()
        self.assertTrue(gewerbe_nein.is_selected())

        mitglied_nein.click()
        self.assertTrue(mitglied_nein.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()

        self.assertFalse(mitglied_ja.is_selected())
        self.assertFalse(mitglied_nein.is_selected())
        self.assertFalse(gewerbe_ja.is_selected())
        self.assertFalse(gewerbe_nein.is_selected())

        # -- Ja Ja
        mitglied_ja.click()
        self.assertTrue(mitglied_ja.is_selected())
        gewerbe_ja.click()
        self.assertTrue(gewerbe_ja.is_selected())
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        WebDriverWait(driver, 3).until(EC.text_to_be_present_in_element((By.XPATH,
                                                                         "(/html/body/div[3]/div/div/div[1]/h3)"),
                                                                        "Hinweis zu den Tarifierungsdaten"))
        driver.find_element_by_xpath("//div[3]/div/div/button").click()

        # -- Ja Nein

        mitglied_ja.click()
        self.assertTrue(mitglied_ja.is_selected())

        gewerbe_nein.click()
        self.assertTrue(gewerbe_nein.is_selected())

        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "betriebsflaeche")))
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "betriebsflaeche")))
        # endregion

        self.zielgruppe_btrklasse_select_by_name("selbstandige")
        self.check_and_click_element_by_xpath(
            self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"])

        # -- Landwirte
        self.zielgruppe_btrklasse_select_by_name("landwirte", landwirte_anzahl, landwirte_anzahl)
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())
        WebDriverWait(driver, 4).until(EC.presence_of_element_located((By.ID, "betriebsflaeche")),
                                       "Field betriebsflaeche not present")
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.ID, "betriebsflaeche")),
                                       "Field betriebsflaeche not visible")

        self.zielgruppe_weiter_tarifdaten()

        self.tarifdaten_zuruck_zielgruppe()

        try:
            self.assertTrue(driver.find_element_by_xpath(
                self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["radio_xpath"]).is_selected())
        except AssertionError as e:
            self.verificationErrors.append("Landwirte not selected")

        el = driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["form_xpath"])

        try:
            self.assertEqual(driver.find_element_by_xpath(
                self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["form_xpath"]).get_attribute('value'),
                             str(landwirte_anzahl))
        except AssertionError as e:
            self.verificationErrors.append("%s instead of %s" % (driver.find_element_by_xpath(
                self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["landwirte"]["form_xpath"]).get_attribute('value'),
                                                                 str(landwirte_anzahl)))

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
