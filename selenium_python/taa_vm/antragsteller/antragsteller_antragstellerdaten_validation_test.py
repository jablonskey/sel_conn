# -*- coding: utf-8 -*-
import datetime
import os
import unittest

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class AntragstellerAntragstellerdatenValidationTest(unittest.TestCase, common_tasks.CommonTasks):
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

        self.driver.maximize_window()

        self.Maxdiff = None
        self.driver.implicitly_wait(2)
        self.base_url = "https://ctest.lodz.ks-software.com/"
        self.verificationErrors = []
        self.ignoredErrors = []
        self.accept_next_alert = True

    def test_antragsteller_antragstellerdaten_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name(btrklasse_name="familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        self.antragsteller_fill_data_lebenspartner(selected_radiobutton="nein")
        self.antragsteller_fill_data_zahlungsdaten(zahlungsart="uberweisung")
        self.antragsteller_fill_data_vorversicherung(selected_radiobutton="nein")

        self.assertFalse(driver.find_element_by_id("anrede").is_selected())
        self.check_if_anrede_form_state_is_invalid(driver,
                                                   err_msg="Required field ANREDE is empty but NOT in state INVALID")
        self.check_anrede_form_validation(driver)

        self.assertFalse(driver.find_element_by_id("titel").is_selected())
        self.check_if_titel_form_state_is_valid(driver,
                                                err_msg="NOT required field TITEL is empty but has NG-INVALID state")
        self.check_titel_form_validation(driver)

        self.check_if_name_form_state_is_invalid(driver,
                                                 err_msg="Required field NAME is empty but NOT in state INVALID")
        self.check_name_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("name", "TESTname", "valid")

        self.check_if_vorname_form_state_is_invalid(driver,
                                                    err_msg="Required field VORNAME is empty but NOT in state INVALID")
        self.check_vorname_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("vorname", "TESTvorname", "valid")

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Firma o.A.")
        self.check_namenszusatz_visibility_after_proper_anrede_is_selected(driver)
        self.check_anrede_combobox_available_options_after_selection(driver)

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Herr")
        self.check_vorname_visibility_after_proper_anrede_is_selected(driver)
        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Firma")

        self.check_and_click_element_by_xpath(self.ANTRAGSTELLER_ANTRAGSTELLERDATEN_FORMS["name"]["xpath"])
        self.check_namenszusatz_visibility_after_proper_anrede_is_selected(driver)

        self.check_if_namenszusatz_form_state_is_valid(driver,
                                                       err_msg="NOT required field NAMENSZUSATZ is empty"
                                                               " but has INVALID state")
        self.check_namenszusatz_form_validation(driver)
        self.check_if_namenszusatz_form_state_is_valid(driver,
                                                       err_msg="NOT required field NAMENSZUSATZ is empty"
                                                               " but has INVALID state")
        self.enter_text_and_check_validation_in_element_by_id("namenszusatz", u"TESTnamenszusatz", "valid")

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Herr")

        self.check_if_strasse_form_state_is_invalid(driver,
                                                    err_msg="Required field STRASSE is empty but NOT in state INVALID")
        self.check_strasse_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("strasse", u"TESTstrasse", "valid")

        self.check_if_hausnummer_form_is_invalid(driver,
                                                 err_msg="Required field HAUSNUMMER is empty but NOT in state INVALID")
        self.check_hausnummer_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("hausnummer", u"12TEST", "valid")

        self.check_if_plz_form_is_invalid(driver, err_msg="Required field PLZ is empty but NOT in state INVALID")
        self.check_plz_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("plz", "12345", "valid")

        self.check_if_ort_form_state_is_invalid(driver, err_msg="Required field ORT is empty but NOT in state INVALID")
        self.check_ort_form_validation(driver)
        self.enter_text_and_check_validation_in_element_by_id("ort", u"TESTort", "valid")

        self.check_if_taetigkeit_combobox_state_is_invalid(driver,
                                                           err_msg="Required combobox TAETIGKEIT"
                                                                   " has no option selected"
                                                                   " but NOT in state INVALID")
        self.check_taetigkeit_combobox_validation(driver)

        self.check_if_berufsgruppe_combobox_state_is_invalid(driver,
                                                             err_msg="Required combobox BERUFSGRUPPE"
                                                                     " has no option selected"
                                                                     " but NOT in state INVALID")
        self.check_berufsgruppe_combobox_validation(driver)

        # region geburtsdatum
        # -- Geburts INVALID
        self.check_if_geburtsdatum_field_state_is_invalid(driver, err_msg="Required field GEBURTSDATUM"
                                                                          " is empty but NOT in state INVALID")

        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "xxxxxxxxx", "notaccepted")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "xx.xx.xxxx", "notaccepted")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "valid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "valid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "31.09.2013", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "30.09.2013", "valid")

        self.validate_date_field_by_id_not_refreshing("geburtsdatum")

        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "29.02.2013", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "28.02.2013", "valid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "29.02.2012", "valid")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "01.01.2014", "valid")
        # endregion

        self.antragsteller_weiter_zusatzdaten()

    def check_if_geburtsdatum_field_state_is_invalid(self, driver, err_msg="Combobox TAETIGKEIT"
                                                                           " has incorrect VALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("geburtsdatum").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_berufsgruppe_combobox_validation(self, driver):
        self.check_berufsgruppe_combobox_available_options_before_selection(driver)
        Select(driver.find_element_by_id("berufsgruppe")).select_by_index(1)
        self.check_if_berufsgruppe_combobox_state_is_valid(driver)
        self.check_berufsgruppe_combobox_available_options_after_selection(driver)

    def check_berufsgruppe_combobox_available_options_after_selection(self, driver):
        self.assertTrue(6, len(Select(driver.find_element_by_id("berufsgruppe")).options))
        self.assertEqual(u"Berufs-/Lizenzsportler / -trainer",
                         Select(driver.find_element_by_id("berufsgruppe")).options[0].text)
        self.assertEqual(u"Schauspieler/Moderator (Film, TV)",
                         Select(driver.find_element_by_id("berufsgruppe")).options[1].text)
        self.assertEqual(u"Wertpapierhändler, Börsenmakler",
                         Select(driver.find_element_by_id("berufsgruppe")).options[2].text)
        self.assertEqual(u"Investmentbanker",
                         Select(driver.find_element_by_id("berufsgruppe")).options[3].text)
        self.assertEqual(u"Rechtsanwalt",
                         Select(driver.find_element_by_id("berufsgruppe")).options[4].text)
        self.assertEqual(u"Vorstand / Aufsichtsrat börsennotierter AG",
                         Select(driver.find_element_by_id("berufsgruppe")).options[5].text)
        self.assertEqual(u"Sonstige Berufsgruppe",
                         Select(driver.find_element_by_id("berufsgruppe")).options[6].text)

    def check_berufsgruppe_combobox_available_options_before_selection(self, driver):
        self.assertTrue(7, len(Select(driver.find_element_by_id("berufsgruppe")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("berufsgruppe")).options[0].text)
        self.assertEqual(u"Berufs-/Lizenzsportler / -trainer",
                         Select(driver.find_element_by_id("berufsgruppe")).options[1].text)
        self.assertEqual(u"Schauspieler/Moderator (Film, TV)",
                         Select(driver.find_element_by_id("berufsgruppe")).options[2].text)
        self.assertEqual(u"Wertpapierhändler, Börsenmakler",
                         Select(driver.find_element_by_id("berufsgruppe")).options[3].text)
        self.assertEqual(u"Investmentbanker",
                         Select(driver.find_element_by_id("berufsgruppe")).options[4].text)
        self.assertEqual(u"Rechtsanwalt",
                         Select(driver.find_element_by_id("berufsgruppe")).options[5].text)
        self.assertEqual(u"Vorstand / Aufsichtsrat börsennotierter AG",
                         Select(driver.find_element_by_id("berufsgruppe")).options[6].text)
        self.assertEqual(u"Sonstige Berufsgruppe",
                         Select(driver.find_element_by_id("berufsgruppe")).options[7].text)

    def check_if_berufsgruppe_combobox_state_is_valid(self, driver,
                                                      err_msg="Combobox BERUFSGRUPPE has incorrect NG-INVALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("berufsgruppe").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_if_berufsgruppe_combobox_state_is_invalid(self, driver,
                                                        err_msg="Combobox TAETIGKEIT has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("berufsgruppe").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_taetigkeit_combobox_validation(self, driver):
        self.check_taetigkeit_combobox_available_options_before_selection(driver)
        Select(driver.find_element_by_id("taetigkeit")).select_by_index(1)
        self.check_if_taetigkeit_combobox_state_is_valid(driver)
        self.check_taetigkeit_combobox_available_options_after_selection(driver)

    def check_taetigkeit_combobox_available_options_after_selection(self, driver):
        self.assertTrue(3, len(Select(driver.find_element_by_id("taetigkeit")).options))
        self.assertEqual(u"nichtselbständig",
                         Select(driver.find_element_by_id("taetigkeit")).options[0].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("taetigkeit")).options[1].text)
        self.assertEqual(u"nicht berufstätig",
                         Select(driver.find_element_by_id("taetigkeit")).options[2].text)

    def check_taetigkeit_combobox_available_options_before_selection(self, driver):
        self.assertTrue(4, len(Select(driver.find_element_by_id("taetigkeit")).options))
        self.assertEqual("", Select(driver.find_element_by_id("taetigkeit")).options[0].text)
        self.assertEqual(u"nichtselbständig", Select(driver.find_element_by_id("taetigkeit")).options[1].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("taetigkeit")).options[2].text)
        self.assertEqual(u"nicht berufstätig", Select(driver.find_element_by_id("taetigkeit")).options[3].text)

    def check_if_taetigkeit_combobox_state_is_valid(self, driver,
                                                    err_msg="Combobox TAETIGKEIT has incorrect NG-INVALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("taetigkeit").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_if_taetigkeit_combobox_state_is_invalid(self, driver,
                                                      err_msg="Combobox TAETIGKEIT has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("taetigkeit").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_ort_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("ort", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("ort", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("ort", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("ort", u"bü", "valid")
        driver.find_element_by_id("ort").clear()
        self.check_if_ort_form_state_is_invalid(driver, err_msg="Required field ORT is empty but NOT in state INVALID")

    def check_if_ort_form_state_is_invalid(self, driver, err_msg="Field ORT has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("ort").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_plz_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("plz", ".", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("plz", "1", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("plz", "12345", "valid")
        self.enter_text_and_check_validation_in_element_by_id("plz", "123456", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("plz", "1234a", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("plz", "a", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("plz", u"bü", desired_validation="invalid")
        driver.find_element_by_id("plz").clear()
        self.check_if_plz_form_is_invalid(driver, err_msg="Required field PLZ is empty but NOT in state INVALID")

    def check_if_plz_form_is_invalid(self, driver, err_msg="Field PLZ has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("plz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_hausnummer_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("hausnummer", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("hausnummer", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("hausnummer", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("hausnummer", u"bü", "valid")
        driver.find_element_by_id("hausnummer").clear()
        self.check_if_hausnummer_form_is_invalid(driver,
                                                 err_msg="Required field HAUSNUMMER is empty but NOT in state INVALID")

    def check_if_hausnummer_form_is_invalid(self, driver, err_msg="Field HAUSNUMMER has incorrect VALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("hausnummer").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_strasse_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("strasse", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("strasse", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("strasse", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("strasse", u"bü", "valid")
        driver.find_element_by_id("strasse").clear()
        self.check_if_strasse_form_state_is_invalid(driver,
                                                    err_msg="Required field STRASSE is empty but NOT in state INVALID")

    def check_if_strasse_form_state_is_invalid(self, driver, err_msg="Field STRASSE has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("strasse").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_vorname_visibility_after_proper_anrede_is_selected(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vorname")))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "vorname")))
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "namenszusatz")))
        except TimeoutException as e:
            self.verificationErrors.append("Field VORNAME not visible after proper anrede selected")

    def check_namenszusatz_visibility_after_proper_anrede_is_selected(self, driver):
        try:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "namenszusatz")))
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "namenszusatz")))
            WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "vorname")))
        except TimeoutException as e:
            self.verificationErrors.append("Field NAMENSZUSATZ not visible after proper anrede selected")

    def check_namenszusatz_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("namenszusatz", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("namenszusatz", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("namenszusatz", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("namenszusatz", u"bü", "valid")
        driver.find_element_by_id("namenszusatz").clear()

    def check_if_anrede_form_state_is_invalid(self, driver, err_msg="Field ANREDE has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("anrede").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_if_anrede_form_state_is_valid(self, driver, err_msg="Field ANREDE has incorrect NG-INVALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("anrede").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_anrede_form_validation(self, driver):
        self.check_anrede_combobox_available_options_before_selection(driver)
        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Herr")
        self.check_if_anrede_form_state_is_valid(driver)
        self.check_anrede_combobox_available_options_after_selection(driver)

    def check_anrede_combobox_available_options_before_selection(self, driver):
        self.assertTrue(5, len(Select(driver.find_element_by_id("anrede")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("anrede")).options[0].text)
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("anrede")).options[1].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("anrede")).options[2].text)
        self.assertEqual(u"Firma",
                         Select(driver.find_element_by_id("anrede")).options[3].text)
        self.assertEqual(u"Firma o.A.",
                         Select(driver.find_element_by_id("anrede")).options[4].text)

    def check_anrede_combobox_available_options_after_selection(self, driver):
        self.assertTrue(4, len(Select(driver.find_element_by_id("anrede")).options))
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("anrede")).options[0].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("anrede")).options[1].text)
        self.assertEqual(u"Firma",
                         Select(driver.find_element_by_id("anrede")).options[2].text)
        self.assertEqual(u"Firma o.A.",
                         Select(driver.find_element_by_id("anrede")).options[3].text)

    def check_titel_form_validation(self, driver):
        self.check_titel_combobox_available_options(driver)
        Select(driver.find_element_by_id("titel")).select_by_index(1)
        self.check_if_titel_form_state_is_valid(driver)
        self.check_titel_combobox_available_options(driver)

    def check_titel_combobox_available_options(self, driver):
        self.assertTrue(4, len(Select(driver.find_element_by_id("titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("titel")).options[1].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("titel")).options[2].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("titel")).options[3].text)

    def check_if_titel_form_state_is_valid(self, driver,
                                           err_msg="Field TITEL has incorrect NG-INVALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("titel").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_name_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("name", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "ab-.", "valid")

        self.enter_text_and_check_validation_in_element_by_id("name", "a-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "A-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", "a b", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", u"Bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("name", u"bü", "valid")
        driver.find_element_by_id("name").clear()

        self.check_if_name_form_state_is_invalid(driver, err_msg="Required field NAME empty but NOT in state INVALID")

        self.enter_text_and_check_validation_in_element_by_id("name", u"TESTname", "valid")
        driver.find_element_by_id("name").clear()

    def check_if_name_form_state_is_invalid(self, driver, err_msg="Field NAME has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("name").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_vorname_form_validation(self, driver):
        self.enter_text_and_check_validation_in_element_by_id("vorname", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", u"bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "Ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "ab-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "a b", "valid")

        # -- Vorname VALID
        self.enter_text_and_check_validation_in_element_by_id("vorname", u"Bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("vorname", "A-", "valid")
        driver.find_element_by_id("vorname").clear()

        self.check_if_vorname_form_state_is_invalid(driver,
                                                    err_msg="Required field VORNAME is empty but NOT in state INVALID")

    def check_if_vorname_form_state_is_invalid(self, driver, err_msg="Field VORNAME has incorrect VALID state"):
        try:
            self.assertRegexpMatches(driver.find_element_by_id("vorname").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def check_if_namenszusatz_form_state_is_valid(self, driver,
                                                  err_msg="Field NAMENSZUSATZ has incorrect INVALID state"):
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("namenszusatz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(err_msg)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        for e in self.verificationErrors: print e


if __name__ == "__main__":
    unittest.main()
