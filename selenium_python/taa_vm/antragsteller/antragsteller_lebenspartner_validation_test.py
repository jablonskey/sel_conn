# -*- coding: utf-8 -*-
import datetime
import os
import unittest

from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class AntragstellerLebenspartnerValidationTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_antragsteller_lebenspartner_validation(self):
        driver = self.driver
        self.login_to_connect_vermittler(self.base_url)

        # region vermittler main page
        self.go_to_rechner()
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        # ### Lebensdaten ###
        self.check_and_click_element_by_name("eheLebensPartner")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "lebenspartner-anrede")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "lebenspartner-anrede")))
        self.check_and_click_element_by_name("abwAnschrift")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "lebenspartner-strasse")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "lebenspartner-strasse")))

        # region lebenspartner-anrede

        self.assertFalse(driver.find_element_by_id("lebenspartner-anrede").is_selected())

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-anrede").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("lebenspartner-anrede")

        self.assertTrue(3, len(Select(driver.find_element_by_id("lebenspartner-anrede")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("lebenspartner-anrede")).options[0].text)
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("lebenspartner-anrede")).options[1].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("lebenspartner-anrede")).options[2].text)

        Select(driver.find_element_by_id("lebenspartner-anrede")).select_by_visible_text("Herr")

        self.assertTrue(2, len(Select(driver.find_element_by_id("lebenspartner-anrede")).options))
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("lebenspartner-anrede")).options[0].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("lebenspartner-anrede")).options[1].text)

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-anrede").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("lebenspartner-anrede")

        Select(driver.find_element_by_id("lebenspartner-anrede")).select_by_index(1)

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-anrede").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("lebenspartner-anrede")
        # endregion
        # region lebenspartner-titel
        self.assertFalse(driver.find_element_by_id("lebenspartner-titel").is_selected())

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-titel").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("field lebenspartner-titel")

        self.assertTrue(5, len(Select(driver.find_element_by_id("lebenspartner-titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[1].text)
        self.assertEqual(u"Dr. med.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[2].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[3].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[4].text)

        Select(driver.find_element_by_id("lebenspartner-titel")).select_by_visible_text("Dr.")

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-titel").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("field lebenspartner-titel")

        self.assertTrue(5, len(Select(driver.find_element_by_id("lebenspartner-titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[1].text)
        self.assertEqual(u"Dr. med.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[2].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[3].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[4].text)

        Select(driver.find_element_by_id("lebenspartner-titel")).select_by_visible_text("")

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-titel").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("field lebenspartner-titel")

        self.assertTrue(5, len(Select(driver.find_element_by_id("lebenspartner-titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[1].text)
        self.assertEqual(u"Dr. med.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[2].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[3].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("lebenspartner-titel")).options[4].text)
        # endregion
        # region lebenspartner-name
        # -- Name INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-name").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("Required field lebenspartner-name empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "ab-.", "valid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "a-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "A-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", "a b", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", u"Bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", u"bü", "valid")
        driver.find_element_by_id("lebenspartner-name").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-name").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("Required field lebenspartner-name empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-name", u"TESTNameLeben", "valid")

        # endregion
        # region lebenspartner-vorname

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-vorname").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("Required field lebenspartner-vorname empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", u"bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "Ab123", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "ab-", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "a b", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", u"Bü", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "A-", "valid")
        driver.find_element_by_id("lebenspartner-vorname").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-vorname").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("Required field lebenspartner-vorname empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-vorname", "TESTvornameLeben", "valid")

        # endregion
        # region lebenspartner-geburtsdatum
        # -- Geburts INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-geburtsdatum").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "xxxxxxxxx", "notaccepted")
        self.enter_text_and_check_validation_in_element_by_id("geburtsdatum", "xx.xx.xxxx", "notaccepted")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "31.09.2013",
                                                              desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "30.09.2013", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "29.02.2013",
                                                              desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "28.02.2013", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "29.02.2012", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-geburtsdatum", "01.01.2014", "valid")
        self.validate_date_field_by_id_not_refreshing("lebenspartner-geburtsdatum")
        # endregion
        # region lebenspartner-taetigkeit
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-taetigkeit").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("combo lebenspartner-taetigkeit")
        # -- lebenspartner-taetigkeit VALID
        self.assertTrue(4, len(Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options))
        self.assertEqual("", Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[0].text)
        self.assertEqual(u"nichtselbständig",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[1].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[2].text)
        self.assertEqual(u"nicht berufstätig",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[3].text)
        Select(driver.find_element_by_id("lebenspartner-taetigkeit")).select_by_index(1)
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-taetigkeit").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("combo lebenspartner-taetigkeit")
        self.assertTrue(3, len(Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options))
        self.assertEqual(u"nichtselbständig",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[0].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[1].text)
        self.assertEqual(u"nicht berufstätig",
                         Select(driver.find_element_by_id("lebenspartner-taetigkeit")).options[2].text)
        # endregion
        # region lebenspartner-berufsgruppe
        # -- Berufsgruppe INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("combo lebenspartner-berufsgruppe")
        self.assertTrue(7, len(Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options))

        self.assertEqual("",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[0].text)
        self.assertEqual(u"Berufs-/Lizenzsportler / -trainer",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[1].text)
        self.assertEqual(u"Schauspieler/Moderator (Film, TV)",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[2].text)
        self.assertEqual(u"Wertpapierhändler, Börsenmakler",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[3].text)
        self.assertEqual(u"Investmentbanker",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[4].text)
        self.assertEqual(u"Rechtsanwalt",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[5].text)
        self.assertEqual(u"Vorstand / Aufsichtsrat börsennotierter AG",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[6].text)
        self.assertEqual(u"Sonstige Berufsgruppe",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[7].text)

        Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).select_by_index(1)
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-berufsgruppe").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("combo lebenspartner-berufsgruppe")
        self.assertTrue(6, len(Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options))

        self.assertEqual(u"Berufs-/Lizenzsportler / -trainer",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[0].text)
        self.assertEqual(u"Schauspieler/Moderator (Film, TV)",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[1].text)
        self.assertEqual(u"Wertpapierhändler, Börsenmakler",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[2].text)
        self.assertEqual(u"Investmentbanker",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[3].text)
        self.assertEqual(u"Rechtsanwalt",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[4].text)
        self.assertEqual(u"Vorstand / Aufsichtsrat börsennotierter AG",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[5].text)
        self.assertEqual(u"Sonstige Berufsgruppe",
                         Select(driver.find_element_by_id("lebenspartner-berufsgruppe")).options[6].text)
        # endregion
        # region lebenspartner-strasse
        # -- Strasse INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-strasse").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError:
            self.verificationErrors.append("Required field lebenspartner-strasse empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-strasse", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-strasse", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-strasse", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-strasse", u"bü", "valid")
        driver.find_element_by_id("lebenspartner-strasse").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-strasse").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-strasse empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-strasse", u"TESTstrasseLeben", "valid")
        # endregion
        # region lebenspartner-hausnummer
        # -- Hausnr INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-hausnummer").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-hausnummer empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-hausnummer", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-hausnummer", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-hausnummer", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-hausnummer", u"bü", "valid")
        driver.find_element_by_id("lebenspartner-hausnummer").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("lebenspartner-hausnummer").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("field lebenspartner-hausnummer")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-hausnummer", u"69TESTleben", "valid")
        # endregion
        # region lebenspartner-plz
        # -- PLZ INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-plz").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-plz empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", ".", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "1", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "12345", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "123456",
                                                              desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "1234a",
                                                              desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "a", desired_validation="invalid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", u"bü", desired_validation="invalid")
        driver.find_element_by_id("lebenspartner-plz").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-plz").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-plz empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-plz", "98765", "valid")
        # endregion
        # region lebenspartner-ort
        # -- Ort INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-ort").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-ort empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-ort", ".", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-ort", "1", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-ort", "a", "valid")
        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-ort", u"bü", "valid")
        driver.find_element_by_id("lebenspartner-ort").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("lebenspartner-ort").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field lebenspartner-ort empty but not invalid")

        self.enter_text_and_check_validation_in_element_by_id("lebenspartner-ort", u"TESTlebenspartner-ort", "valid")
        # endregion

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
