# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from service import common_tasks
from service.helpers import Helper
import unittest, time, re, sys, os
from service.common_tasks import CommonTasks


class ZielgruppeMaskTest(unittest.TestCase, common_tasks.CommonTasks):
    def setUp(self):
        profile = webdriver.FirefoxProfile()
        profile.native_events_enabled = False
        self.driver = webdriver.Firefox(profile)
        self.driver.implicitly_wait(10)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_anzahls_refreshing(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("selbstandige", 10)

        self.zielgruppe_btrklasse_select_by_name("familien")

        self.zielgruppe_btrklasse_select_by_name("arzte")
        try:
            self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-aerzte").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field anzahl-beschaeftigen-aerzte not refreshed / line %s" % (sys.exc_info()[-1].tb_lineno))
        driver.find_element_by_id("anzahl-beschaeftigen-aerzte").clear()
        driver.find_element_by_id("anzahl-beschaeftigen-aerzte").send_keys("5")

        self.zielgruppe_btrklasse_select_by_name("familien")

        self.zielgruppe_btrklasse_select_by_name("selbstandige")
        try:
            self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field anzahl-beschaeftigen-selbstaendige not refreshed / line %s" % (sys.exc_info()[-1].tb_lineno))
        driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").clear()
        driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").send_keys("5")

        self.zielgruppe_btrklasse_select_by_name("familien")

        self.zielgruppe_btrklasse_select_by_name("steuerberater")
        try:
            self.assertEqual("", driver.find_element_by_id("honorareinnahmen").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field honorareinnahmen not refreshed / line %s" % (sys.exc_info()[-1].tb_lineno))
        driver.find_element_by_id("honorareinnahmen").clear()
        driver.find_element_by_id("honorareinnahmen").send_keys("5")

        self.zielgruppe_btrklasse_select_by_name("familien")

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        try:
            self.assertEqual("", driver.find_element_by_id("betriebsflaeche").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field betriebsflaeche not refreshed / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_landwirte_radios_clean_and_not_red_after_popup_angaben_andern(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("landwirte")
        # -- JA JA
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.check_and_click_element_by_name("isLandwirteGewerbe")
        self.assertTrue(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Verwerfen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        try:
            self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        except AssertionError:
            self.verificationErrors.append(
                "Radio isLandwirteMitglied not cleaned after angaben_andern on popup / line %d" % (
                    sys.exc_info()[-1].tb_lineno))
        try:
            self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        except AssertionError:
            self.verificationErrors.append(
                "Radio isLandwirteGewerbe not cleaned after angaben_andern on popup / line %d" % (
                    sys.exc_info()[-1].tb_lineno))

        landwirte_radio_labels = driver.find_elements_by_xpath("(/html/body/div[1]/div/div/section/div/div[2]/div/form[2]/div[4]/div/div/div[2]/div[1]/div[*]/div[2]/div[*]/label)")

        self.is_elements_color(landwirte_radio_labels, "rgba(51, 63, 72, 1)")

    def test_landwirte_radios_clean_and_not_red_after_popup_angaben_andern_after_form_not_valid(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())
        self.check_and_click_element_by_link_text("Weiter")
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- JA JA
        self.check_and_click_element_by_name("isLandwirteGewerbe")
        self.assertTrue(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Verwerfen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        try:
            self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        except AssertionError:
            self.verificationErrors.append(
                "Radio isLandwirteMitglied not cleaned after angaben_andern on popup / line %d" % (
                    sys.exc_info()[-1].tb_lineno))
        try:
            self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        except AssertionError:
            self.verificationErrors.append(
                "Radio isLandwirteGewerbe not cleaned after angaben_andern on popup / line %d" % (
                    sys.exc_info()[-1].tb_lineno))

        landwirte_radio_labels = driver.find_elements_by_xpath("(/html/body/div[1]/div/div/section/div/div[2]/div/form[2]/div[4]/div/div/div[2]/div[1]/div[*]/div[2]/div[*]/label)")

        self.is_elements_color(landwirte_radio_labels, "rgba(51, 63, 72, 1)")

    def test_landwirte_popup_dismiss_disabled(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- JA JA
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.check_and_click_element_by_name("isLandwirteGewerbe")
        self.assertTrue(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Dismiss
        driver.find_element_by_xpath("(/html/body/div[3]/div/div)").send_keys(Keys.ESCAPE)
        try:
            WebDriverWait(driver, 4).until(
                EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))
        except Exception:
            pass
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        landwirte_radio_labels = driver.find_elements_by_xpath("(/html/body/div[1]/div/div/section/div/div[2]/div/form[2]/div[4]/div/div/div[2]/div[1]/div[*]/div[2]/div[*]/label)")
        self.is_elements_color(landwirte_radio_labels, "rgba(51, 63, 72, 1)")

    def landwirte_popup_test(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()
        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- JA JA
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.assertTrue(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.check_and_click_element_by_name("isLandwirteGewerbe")
        self.assertTrue(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Verwerfen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- NEIN JA
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.check_and_click_element_by_name("isLandwirteGewerbe")
        self.assertTrue(driver.find_element_by_name("isLandwirteGewerbe").is_selected())

        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Verwerfen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- NEIN JA
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        # -- Verwerfen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")
        WebDriverWait(driver, 4).until(EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        # -- NEIN NEIN
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        self.assertTrue(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())

        WebDriverWait(driver, 4).until(EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div)")))

        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        self.assertEqual("Hinweis zu den Tarifierungsdaten",
                         driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)

        # -- Ubernamen
        self.check_and_click_element_by_xpath("/html/body/div[3]/div/div/div[3]/div/div[3]/button")
        WebDriverWait(driver, 4).until(
            EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))

        # -- Selbstandinge/Firmen/Freiberufler
        self.zielgruppe_btrklasse_select_by_name("selbstandige")
        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["form_xpath"])

        self.zielgruppe_btrklasse_select_by_name("landwirte", 10)
        self.zielgruppe_weiter_tarifdaten()

    def test_berechnungshilfe_popup(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("selbstandige")

        # -- Selbstandinge/Firmen/Freiberufler

        # -- Berechnungshilfe popup
        self.check_and_click_element_by_link_text("Berechnungshilfe")
        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("Berechnungshilfe", driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("4")
        self.assertEqual("4", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()

        # CONNECT-720
        self.assertNotEqual("", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        self.assertEqual("4", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))

        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("2")
        self.assertEqual("5", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))



        # -- Abbrechen
        self.check_and_click_element_by_xpath("(//div[3]/div/div/button)")

        WebDriverWait(driver, 4).until(
            EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").get_attribute("value"))
        self.check_and_click_element_by_link_text("Berechnungshilfe")
        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("Berechnungshilfe", driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        self.assertEqual("0", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        self.assertEqual("0", driver.find_element_by_xpath("(//input[@type='text'])[5]").get_attribute("value"))
        self.assertEqual("0", driver.find_element_by_xpath("(//input[@type='text'])[6]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("4")
        self.assertEqual("4", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("2")
        self.assertEqual("5", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))

        # -- Ubernamen
        self.check_and_click_element_by_xpath(Helper.ERGANZUNGEN_POPUP_OK_BUTTON_XPATH)

        WebDriverWait(driver, 4).until(
            EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("5", driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").get_attribute("value"))

        self.check_and_click_element_by_link_text("Berechnungshilfe")
        WebDriverWait(driver, 4).until(
            EC.visibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("Berechnungshilfe", driver.find_element_by_xpath("(/html/body/div[3]/div/div/div[1]/h3)").text)
        driver.find_element_by_xpath("(//input[@type='text'])[5]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[5]").send_keys("6")
        self.assertEqual("6", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))
        driver.find_element_by_xpath("(//input[@type='text'])[6]").clear()
        driver.find_element_by_xpath("(//input[@type='text'])[6]").send_keys("2")
        self.assertEqual("7", driver.find_element_by_xpath("(//input[@type='text'])[13]").get_attribute("value"))

        # -- Abbrechen
        self.check_and_click_element_by_xpath("//div[3]/div/div/button")

        WebDriverWait(driver, 4).until(
            EC.invisibility_of_element_located((By.XPATH, "(/html/body/div[3]/div/div/div[1]/h3)")))
        self.assertEqual("5", driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").get_attribute("value"))

    def test_zielgruppe_mask(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()



        # -- Familien
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_btrklasse_select_by_name("selbstandige")
        try:
            self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-selbstaendige").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field anzahl-beschaeftigen-selbstaendige not empty / line %d" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("singles")
        self.zielgruppe_btrklasse_select_by_name("arzte")
        try:
            self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-aerzte").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field anzahl-beschaeftigen-aerzte not empty / line %d" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("steuerberater")
        try:
            self.assertEqual("", driver.find_element_by_id("honorareinnahmen").get_attribute("value"))
        except AssertionError:
            self.verificationErrors.append(
                "Field honorareinnahmen not empty / line %d" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("senioren")

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.assertFalse(driver.find_element_by_name("isLandwirteMitglied").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteMitglied'])[2]").is_selected())
        self.assertFalse(driver.find_element_by_name("isLandwirteGewerbe").is_selected())
        self.assertFalse(driver.find_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]").is_selected())


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
