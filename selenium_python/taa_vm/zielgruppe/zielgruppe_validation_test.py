# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks
from service.helpers import Helper

# from service import common_tasks

import unittest, sys, os


class ZielgruppeValidationTest(unittest.TestCase, common_tasks.CommonTasks, Helper):
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

    def test_no_zielgruppe_checked_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.check_and_click_element_by_link_text("Weiter")

        # TODO
        # Alerts/warnings handling in service/common_tasks

        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url, )
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_selbstandige_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("selbstandige")

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['selbstandige']["header_xpath"])
        try:
            self.assertRegexpMatches(
                    driver.find_element_by_xpath(
                            self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"]).get_attribute(
                        "class"),
                    r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append(
                    "anzahl-beschaeftigen-selbstaendige not invalid // empty but required / line %s" % (
                        sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath((self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"]),
                                       "asd", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"], "*",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"], ".",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"],
                                       "-10", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"],
                                       "10a", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"],
                                       "10", "valid")
        self.zielgruppe_weiter_tarifdaten()

    def test_arzte_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("arzte")

        # TODO
        # try:
        #     self.assertEqual("", driver.find_element_by_id("anzahl-beschaeftigen-aerzte").get_attribute("value"))
        # except AssertionError:
        #     self.verificationErrors.append("Field anzahl-beschaeftigen-aerzte not refreshed / line %s" % (sys.exc_info()[-1].tb_lineno))

        driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"]).clear()

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"])))
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"])))
        try:
            self.assertRegexpMatches(driver.find_element_by_xpath(
                    self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"]).get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("anzahl-beschaeftigen-aerzte not invalid // empty but required / line %s" % (
                sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "asd", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "*", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], ".", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "10-", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "-10", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "10a", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["arzte"]["form_xpath"], "10", "valid")
        self.zielgruppe_weiter_tarifdaten()

    def test_steuerberater_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("steuerberater")

        self.driver.find_element_by_xpath(
                self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"]).clear()

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + self.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"])))
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(
                (By.XPATH, self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"])))

        # Honorareinahmen required on zielgruppe page
        # try:
        #     self.assertRegexpMatches(driver.find_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"]).get_attribute("class"),
        #                              r"ng-invalid")
        # except AssertionError:
        #     self.verificationErrors.append("honorareinnahmen not invalid // empty but required")

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "asd",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "*",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], ".",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "10-",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "-10",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "10a",
                                       "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + "ng/#/taa//tarifdaten", self.driver.current_url)
        except AssertionError as e:
            pass
        else:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form2_xpath"], "10",
                                       "valid")
        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["steuerberater"]["form1_xpath"], "10",
                                       "valid")
        self.zielgruppe_weiter_tarifdaten()

    def test_landwirte_no_radios_selected_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_landwirte_no_right_radios_selected_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_landwirte_no_left_radios_selected_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_landwirte_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
                (By.ID, "betriebsflaeche")))
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(
                (By.ID, "betriebsflaeche")))

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.check_and_click_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST['landwirte']["form_xpath"])
        try:
            self.assertRegexpMatches(
                    driver.find_element_by_id("betriebsflaeche").get_attribute("class"),
                    r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append(
                    "anzahl-beschaeftigen-selbstaendige not invalid // empty but required / line %s" % (
                        sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", "asd", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", "*", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", ".", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", "-10", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", "10a", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))
        self.validate_element_by_id("betriebsflaeche", "10", "valid")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_landwirte_no_radios_checked(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

    def test_familien_after_landwirte_no_left_radios_checked(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_landwirte_no_right_radios_checked(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")
        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_landwirte(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
                (By.ID, "betriebsflaeche")))
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(
                (By.ID, "betriebsflaeche")))

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_landwirte_form_not_valid(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("landwirte")

        self.check_and_click_element_by_name("isLandwirteMitglied")
        self.check_and_click_element_by_xpath("(//input[@name='isLandwirteGewerbe'])[2]")
        WebDriverWait(self.driver, 4).until(EC.presence_of_element_located(
                (By.ID, "betriebsflaeche")))
        WebDriverWait(self.driver, 4).until(EC.visibility_of_element_located(
                (By.ID, "betriebsflaeche")))

        self.validate_element_by_id("betriebsflaeche", "asd", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_selbstandige(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("selbstandige")

        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def test_familien_after_selbstandige_anzahl_not_valid(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.open_taa_vm()

        self.zielgruppe_btrklasse_select_by_name("selbstandige")

        self.validate_element_by_xpath(self.ZIELGRUPPE_BTRKLASSES_HELPER_LIST["selbstandige"]["anzahl_form_xpath"],
                                       "asd", "invalid")
        self.check_and_click_element_by_link_text("Weiter")
        try:
            self.assertEqual(self.base_url + Helper.ZIELGRUPPE_PAGE_ADDRESS_COMPLETION, self.driver.current_url)
        except AssertionError as e:
            self.verificationErrors.append(
                    "Tarifdaten reached, validation did not work / line %s" % (sys.exc_info()[-1].tb_lineno))

        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
