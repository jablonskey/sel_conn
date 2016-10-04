# -*- coding: utf-8 -*-
import datetime
import os
import unittest

from selenium import webdriver
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
                self.driver = webdriver.Ie()
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

        # region vermittler main page
        self.open_taa_vm()

        # endregion

        # region zielgruppe page
        self.zielgruppe_btrklasse_select_by_name("familien")
        self.zielgruppe_weiter_tarifdaten()
        self.tarifdaten_weiter_antrastellerdaten()
        # ### Antragstellerdaten ###

        self.antragsteller_fill_data_zahlungsdaten("uberweisung")
        self.antragsteller_fill_data_vorversicherung("nein")

        # region anrede
        # -- Anrede
        self.assertFalse(driver.find_element_by_id("anrede").is_selected())

        try:
            self.assertRegexpMatches(driver.find_element_by_id("anrede").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field anrede empty but not invalid")

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
        # endregion
        # region titel
        # -- Akad. Titel

        self.assertFalse(driver.find_element_by_id("titel").is_selected())

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("titel").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Not required field titel empty but not valid")

        self.assertTrue(4, len(Select(driver.find_element_by_id("titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("titel")).options[1].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("titel")).options[2].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("titel")).options[3].text)

        Select(driver.find_element_by_id("titel")).select_by_index(1)

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("titel").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Not required select field titel  but not valid")

        self.assertTrue(4, len(Select(driver.find_element_by_id("titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("titel")).options[1].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("titel")).options[2].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("titel")).options[3].text)
        # endregion
        # region name
        # -- Name INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("name").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field name empty but not invalid")

        self.validate_element_by_id("name", ".", "valid")
        self.validate_element_by_id("name", "a", "valid")
        self.validate_element_by_id("name", "-", "valid")
        self.validate_element_by_id("name", "ab123", "valid")
        self.validate_element_by_id("name", "ab-.", "valid")

        self.validate_element_by_id("name", "a-", "valid")
        self.validate_element_by_id("name", "A-", "valid")
        self.validate_element_by_id("name", "a b", "valid")
        self.validate_element_by_id("name", u"Bü", "valid")
        self.validate_element_by_id("name", u"bü", "valid")
        driver.find_element_by_id("name").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("name").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field name empty but not invalid")

        self.validate_element_by_id("name", u"TESTname", "valid")

        # endregion
        # region vorname
        # -- Vorname INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("vorname").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field vorname empty but not invalid")

        self.validate_element_by_id("vorname", ".", "valid")
        self.validate_element_by_id("vorname", "a", "valid")
        self.validate_element_by_id("vorname", "-", "valid")
        self.validate_element_by_id("vorname", u"bü", "valid")
        self.validate_element_by_id("vorname", "ab123", "valid")
        self.validate_element_by_id("vorname", "Ab123", "valid")
        self.validate_element_by_id("vorname", "ab-", "valid")
        self.validate_element_by_id("vorname", "a b", "valid")

        # -- Vorname VALID
        self.validate_element_by_id("vorname", u"Bü", "valid")
        self.validate_element_by_id("vorname", "A-", "valid")
        driver.find_element_by_id("vorname").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("vorname").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field vorname empty but not invalid")

        self.validate_element_by_id("vorname", "TESTvorname", "valid")

        # endregion
        # region namenszusatz
        # -- Namenszusatz

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Firma o.A.")
        # self.scroll_to_element(driver.find_element_by_id("anrede"))

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "namenszusatz")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "namenszusatz")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "vorname")))

        self.assertTrue(4, len(Select(driver.find_element_by_id("anrede")).options))
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("anrede")).options[0].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("anrede")).options[1].text)
        self.assertEqual(u"Firma",
                         Select(driver.find_element_by_id("anrede")).options[2].text)
        self.assertEqual(u"Firma o.A.",
                         Select(driver.find_element_by_id("anrede")).options[3].text)

        try:
            self.assertTrue(driver.find_element_by_xpath("//div[5]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field namenszusatz visibility")
        try:
            self.assertFalse(driver.find_element_by_xpath("//div[4]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field vorname visibilty")

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Herr")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "vorname")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "vorname")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "namenszusatz")))

        try:
            self.assertTrue(driver.find_element_by_xpath("//div[4]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field vorname visibilty")
        try:
            self.assertFalse(driver.find_element_by_xpath("//div[5]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field namenszusatz visibility")

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Firma")

        self.check_and_click_element_by_xpath(self.ANTRAGSTELLER_ANTRAGSTELLERDATEN_FORMS["name"]["xpath"])
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "namenszusatz")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "namenszusatz")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "vorname")))

        try:
            self.assertTrue(driver.find_element_by_xpath("//div[5]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field namenszusatz visibility")
        try:
            self.assertFalse(driver.find_element_by_xpath("//div[4]/label").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field vorname visibilty")

        # -- Namenszusatz INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("namenszusatz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("NOT Required field namenszusatz empty but invalid")

        self.validate_element_by_id("namenszusatz", ".", "valid")
        self.validate_element_by_id("namenszusatz", "1", "valid")
        self.validate_element_by_id("namenszusatz", "a", "valid")
        self.validate_element_by_id("namenszusatz", u"bü", "valid")
        driver.find_element_by_id("namenszusatz").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("namenszusatz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("NOT Required field namenszusatz empty but invalid")

        self.validate_element_by_id("namenszusatz", u"TESTnamenszusatz", "valid")

        Select(driver.find_element_by_id("anrede")).select_by_visible_text("Herr")

        # endregion
        # region strasse
        # -- Strasse INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("strasse").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field strasse empty but not invalid")

        self.validate_element_by_id("strasse", ".", "valid")
        self.validate_element_by_id("strasse", "1", "valid")
        self.validate_element_by_id("strasse", "a", "valid")
        self.validate_element_by_id("strasse", u"bü", "valid")
        driver.find_element_by_id("strasse").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("strasse").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field strasse empty but not invalid")

        self.validate_element_by_id("strasse", u"TESTstrasse", "valid")
        # endregion
        # region hausnummer
        # -- Hausnr INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("hausnummer").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field hausnummer empty but not invalid")

        self.validate_element_by_id("hausnummer", ".", "valid")
        self.validate_element_by_id("hausnummer", "1", "valid")
        self.validate_element_by_id("hausnummer", "a", "valid")
        self.validate_element_by_id("hausnummer", u"bü", "valid")
        driver.find_element_by_id("hausnummer").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("hausnummer").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field hausnummer empty but not invalid")

        self.validate_element_by_id("hausnummer", u"12TEST", "valid")
        # endregion
        # region plz
        # -- PLZ INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("plz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field plz empty but not invalid")

        self.validate_element_by_id("plz", ".", "invalid")
        self.validate_element_by_id("plz", "1", "invalid")
        self.validate_element_by_id("plz", "12345", "valid")
        self.validate_element_by_id("plz", "123456", "invalid")
        self.validate_element_by_id("plz", "1234a", "invalid")
        self.validate_element_by_id("plz", "a", "invalid")
        self.validate_element_by_id("plz", u"bü", "invalid")
        driver.find_element_by_id("plz").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("plz").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field plz empty but not invalid")

        self.validate_element_by_id("plz", "12345", "valid")
        # endregion
        # region ort
        # -- Ort INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("ort").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field ort empty but not invalid")

        self.validate_element_by_id("ort", ".", "valid")
        self.validate_element_by_id("ort", "1", "valid")
        self.validate_element_by_id("ort", "a", "valid")
        self.validate_element_by_id("ort", u"bü", "valid")
        driver.find_element_by_id("ort").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("ort").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field ort empty but not invalid")

        self.validate_element_by_id("ort", u"TESTort", "valid")
        # endregion

        # region taetigkeit
        # -- Taetigkeit INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("taetigkeit").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("combo taetigkeit")
        # -- Taetigkeit VALID
        self.assertTrue(4, len(Select(driver.find_element_by_id("taetigkeit")).options))
        self.assertEqual("", Select(driver.find_element_by_id("taetigkeit")).options[0].text)
        self.assertEqual(u"nichtselbständig", Select(driver.find_element_by_id("taetigkeit")).options[1].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("taetigkeit")).options[2].text)
        self.assertEqual(u"nicht berufstätig", Select(driver.find_element_by_id("taetigkeit")).options[3].text)
        Select(driver.find_element_by_id("taetigkeit")).select_by_index(1)
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("taetigkeit").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("combo taetigkeit")
        self.assertTrue(3, len(Select(driver.find_element_by_id("taetigkeit")).options))
        self.assertEqual(u"nichtselbständig",
                         Select(driver.find_element_by_id("taetigkeit")).options[0].text)
        self.assertEqual(u"selbständig / freiberuflich",
                         Select(driver.find_element_by_id("taetigkeit")).options[1].text)
        self.assertEqual(u"nicht berufstätig",
                         Select(driver.find_element_by_id("taetigkeit")).options[2].text)
        # endregion

        # region berufsgruppe
        # -- Berufsgruppe INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("berufsgruppe").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("combo berufsgruppe")
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

        Select(driver.find_element_by_id("berufsgruppe")).select_by_index(1)
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("berufsgruppe").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("combo berufsgruppe")
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

        # region geburtsdatum
        # -- Geburts INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("geburtsdatum").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append(str(e))

        self.validate_element_by_id("geburtsdatum", "xxxxxxxxx", "notaccepted")
        self.validate_element_by_id("geburtsdatum", "xx.xx.xxxx", "notaccepted")
        self.validate_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() + datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() + datetime.timedelta(days=1)).year).zfill(2)), "invalid")
        self.validate_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str(datetime.datetime.now().day).zfill(2), str(datetime.datetime.now().month).zfill(2),
            str(datetime.datetime.now().year).zfill(2)), "valid")
        self.validate_element_by_id("geburtsdatum", "%s.%s.%s" % (
            str((datetime.datetime.today() - datetime.timedelta(days=1)).day).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).month).zfill(2),
            str((datetime.datetime.today() - datetime.timedelta(days=1)).year).zfill(2)), "valid")
        self.validate_element_by_id("geburtsdatum", "31.09.2013", "invalid")
        self.validate_element_by_id("geburtsdatum", "30.09.2013", "valid")

        self.validate_date_field_by_id_not_refreshing("geburtsdatum")

        self.validate_element_by_id("geburtsdatum", "29.02.2013", "invalid")
        self.validate_element_by_id("geburtsdatum", "28.02.2013", "valid")
        self.validate_element_by_id("geburtsdatum", "29.02.2012", "valid")
        self.validate_element_by_id("geburtsdatum", "01.01.2014", "valid")
        # endregion

        self.antragsteller_weiter_zusatzdaten()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        for e in self.verificationErrors: print e


if __name__ == "__main__":
    unittest.main()
