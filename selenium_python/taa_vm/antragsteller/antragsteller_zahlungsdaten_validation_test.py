# -*- coding: utf-8 -*-
import os
import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # available since 2.26.0
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait  # available since 2.4.0

from service import common_tasks


class AntragstellerZahlungsdatenValidationTest(unittest.TestCase, common_tasks.CommonTasks):
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

    def test_antragsteller_zahlungsdaten_validation(self):
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

        # XXX Zahlungsdaten XXX
        self.antragsteller_fill_data_antragstellerdaten()
        self.check_and_click_element_by_name("zahlungsart")

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "iban")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "iban")))

        self.check_and_click_element_by_xpath(
            "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[2]/div/div[2]/label/input)")
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "kontoinhaber-strasse")))
        WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.ID, "kontoinhaber-strasse")))

        # -- IBAN INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("iban").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field iban empty but not invalid")

        self.validate_element_by_id("iban", ".", "invalid")
        self.validate_element_by_id("iban", "1111111111111111111", "invalid")
        self.validate_element_by_id("iban", "1 11111111111111111", "invalid")
        self.validate_element_by_id("iban", "DE 11111 11111 11111 111", "invalid")

        # -- IBAN VALID

        self.validate_element_by_id("iban", "1 111111111111111111111", "valid")
        self.validate_element_by_id("iban", "DE 11111 11111 11111 11111", "valid")

        self.validate_element_by_id("iban", "1111111111111111111111", "valid")
        self.validate_element_by_id("iban", "aaaaaaaaaaaaaaaaaaaaaa", "valid")
        self.validate_element_by_id("iban", "AAAAAAAAAAAAAAAAAAAAAA", "valid")
        self.validate_element_by_id("iban", "1a21a21a21a21a21a21a21", "valid")
        driver.find_element_by_id("iban").clear()
        try:
            self.assertRegexpMatches(driver.find_element_by_id("iban").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field iban empty but not invalid")

        self.validate_element_by_id("iban", "DE88300606010301156608", "valid")

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("bic").get_attribute("class"), r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Not required field bic empty but not valid")

        self.validate_element_by_id("bic", ".", "invalid")
        self.validate_element_by_id("bic", "1111111", "invalid")
        self.validate_element_by_id("bic", "111111111111", "invalid")
        self.validate_element_by_id("bic", "1a11111", "invalid")
        self.validate_element_by_id("bic", "1 11111111", "invalid")

        # -- BIC VALID

        self.validate_element_by_id("bic", "11111111", "valid")
        self.validate_element_by_id("bic", "aaaaaaaaa", "valid")
        self.validate_element_by_id("bic", "AAAAAAAAA", "valid")
        self.driver.find_element_by_id("bic").clear()
        self.driver.find_element_by_id("bic").send_keys("D")
        self.driver.find_element_by_id("bic").send_keys("A")
        self.driver.find_element_by_id("bic").send_keys("A")
        self.driver.find_element_by_id("bic").send_keys("E")
        self.driver.find_element_by_id("bic").send_keys("D")
        self.driver.find_element_by_id("bic").send_keys("E")
        self.driver.find_element_by_id("bic").send_keys("D")
        self.driver.find_element_by_id("bic").send_keys("D")
        self.driver.find_element_by_id("bic").send_keys("X")
        self.driver.find_element_by_id("bic").send_keys("X")
        self.driver.find_element_by_id("bic").send_keys("X")

        # self.check_and_click_element_by_id("iban")

        try:
            WebDriverWait(driver, 5).until(EC.text_to_be_present_in_element_value((By.XPATH,
                                                                                   "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[1]/div[3]/input)"),
                                                                                  "DEUTSCHE APOTHEKER- UND AERZTEBANK"))
        except Exception as e:
            self.verificationErrors.append("%s instead of %s in institut" % (driver.find_element_by_xpath(
                "(/html/body/div/div/div/section/div/div[2]/div/div[2]/div[3]/div/div[2]/form[2]/div[1]/div[3]/input)").get_attribute(
                "value"), "DEUTSCHE APOTHEKER- UND AERZTEBANK"))

        self.assertFalse(driver.find_element_by_id("kontoinhaber-anrede").is_selected())

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-anrede").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-anrede empty but not invalid")

        self.assertTrue(5, len(Select(driver.find_element_by_id("kontoinhaber-anrede")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[0].text)
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[1].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[2].text)
        self.assertEqual(u"Firma",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[3].text)
        self.assertEqual(u"Firma o.A.",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[4].text)
        # endregion
        # region kontoinhaber-titel
        # -- Akad. Titel

        self.assertFalse(driver.find_element_by_id("kontoinhaber-titel").is_selected())

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-titel").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Not required field kontoinhaber-titel empty but not valid")

        self.assertTrue(4, len(Select(driver.find_element_by_id("kontoinhaber-titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[1].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[2].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[3].text)

        Select(driver.find_element_by_id("kontoinhaber-titel")).select_by_index(1)

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-titel").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Not required select field kontoinhaber-titel  but not valid")

        self.assertTrue(4, len(Select(driver.find_element_by_id("kontoinhaber-titel")).options))
        self.assertEqual("",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[0].text)
        self.assertEqual(u"Dr.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[1].text)
        self.assertEqual(u"Prof.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[2].text)
        self.assertEqual(u"Prof. Dr.",
                         Select(driver.find_element_by_id("kontoinhaber-titel")).options[3].text)
        # endregion
        # region kontoinhaber-name
        # -- Name INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-name").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-name empty but not invalid")

        self.validate_element_by_id("kontoinhaber-name", ".", "valid")
        self.validate_element_by_id("kontoinhaber-name", "a", "valid")
        self.validate_element_by_id("kontoinhaber-name", "-", "valid")
        self.validate_element_by_id("kontoinhaber-name", "ab123", "valid")
        self.validate_element_by_id("kontoinhaber-name", "ab-.", "valid")

        self.validate_element_by_id("kontoinhaber-name", "a-", "valid")
        self.validate_element_by_id("kontoinhaber-name", "A-", "valid")
        self.validate_element_by_id("kontoinhaber-name", "a b", "valid")
        self.validate_element_by_id("kontoinhaber-name", u"Bü", "valid")
        self.validate_element_by_id("kontoinhaber-name", u"bü", "valid")
        driver.find_element_by_id("kontoinhaber-name").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-name").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-name empty but not invalid")

        self.validate_element_by_id("kontoinhaber-name", u"TESTnameKontoInhaber", "valid")

        # endregion
        # region kontoinhaber-vorname
        # -- Vorname INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-vorname").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-vorname empty but not invalid")

        self.validate_element_by_id("kontoinhaber-vorname", ".", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "a", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "-", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", u"bü", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "ab123", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "Ab123", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "ab-", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "a b", "valid")

        # -- Vorname VALID
        self.validate_element_by_id("kontoinhaber-vorname", u"Bü", "valid")
        self.validate_element_by_id("kontoinhaber-vorname", "A-", "valid")
        driver.find_element_by_id("kontoinhaber-vorname").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-vorname").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-vorname empty but not invalid")

        self.validate_element_by_id("kontoinhaber-vorname", "TESTvornameKontoInhaber", "valid")

        # endregion
        # region kontoinhaber-namenszusatz
        # -- Namenszusatz

        Select(driver.find_element_by_id("kontoinhaber-anrede")).select_by_visible_text("Firma o.A.")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kontoinhaber-namenszusatz")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "kontoinhaber-namenszusatz")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "kontoinhaber-vorname")))

        self.assertTrue(4, len(Select(driver.find_element_by_id("kontoinhaber-anrede")).options))
        self.assertEqual(u"Herr",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[0].text)
        self.assertEqual(u"Frau",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[1].text)
        self.assertEqual(u"Firma",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[2].text)
        self.assertEqual(u"Firma o.A.",
                         Select(driver.find_element_by_id("kontoinhaber-anrede")).options[3].text)

        try:
            self.assertTrue(driver.find_element_by_id("kontoinhaber-namenszusatz").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-namenszusatz visibility")
        try:
            self.assertFalse(driver.find_element_by_id("kontoinhaber-vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-vorname visibilty")

        Select(driver.find_element_by_id("kontoinhaber-anrede")).select_by_visible_text("Herr")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kontoinhaber-vorname")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "kontoinhaber-vorname")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "kontoinhaber-namenszusatz")))

        try:
            self.assertTrue(driver.find_element_by_id("kontoinhaber-vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-vorname visibilty")
        try:
            self.assertFalse(driver.find_element_by_id("kontoinhaber-namenszusatz").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-namenszusatz visibility")

        Select(driver.find_element_by_id("kontoinhaber-anrede")).select_by_visible_text("Firma")

        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "kontoinhaber-namenszusatz")))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "kontoinhaber-namenszusatz")))
        WebDriverWait(driver, 10).until(EC.invisibility_of_element_located((By.ID, "kontoinhaber-vorname")))

        try:
            self.assertTrue(driver.find_element_by_id("kontoinhaber-namenszusatz").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-namenszusatz visibility")
        try:
            self.assertFalse(driver.find_element_by_id("kontoinhaber-vorname").is_displayed())
        except AssertionError as e:
            self.verificationErrors.append("field kontoinhaber-vorname visibilty")

        # -- Namenszusatz INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-namenszusatz").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("NOT Required field kontoinhaber-namenszusatz empty but invalid")

        self.validate_element_by_id("kontoinhaber-namenszusatz", ".", "valid")
        self.validate_element_by_id("kontoinhaber-namenszusatz", "1", "valid")
        self.validate_element_by_id("kontoinhaber-namenszusatz", "a", "valid")
        self.validate_element_by_id("kontoinhaber-namenszusatz", u"bü", "valid")
        driver.find_element_by_id("kontoinhaber-namenszusatz").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-namenszusatz").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("NOT Required field kontoinhaber-namenszusatz empty but invalid")

        self.validate_element_by_id("kontoinhaber-namenszusatz", u"TESTnamenszusatzKontoInhaber", "valid")

        # endregion
        # region kontoinhaber-strasse
        # -- Strasse INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-strasse").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-strasse empty but not invalid")

        self.validate_element_by_id("kontoinhaber-strasse", ".", "valid")
        self.validate_element_by_id("kontoinhaber-strasse", "1", "valid")
        self.validate_element_by_id("kontoinhaber-strasse", "a", "valid")
        self.validate_element_by_id("kontoinhaber-strasse", u"bü", "valid")
        driver.find_element_by_id("kontoinhaber-strasse").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-strasse").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-strasse empty but not invalid")

        self.validate_element_by_id("kontoinhaber-strasse", u"TESTstrasseKontoInhaber", "valid")
        # endregion
        # region kontoinhaber-hausnummer
        # -- Hausnr INVALID
        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-hausnummer").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-hausnummer empty but not invalid")

        self.validate_element_by_id("kontoinhaber-hausnummer", ".", "valid")
        self.validate_element_by_id("kontoinhaber-hausnummer", "1", "valid")
        self.validate_element_by_id("kontoinhaber-hausnummer", "a", "valid")
        self.validate_element_by_id("kontoinhaber-hausnummer", u"bü", "valid")
        driver.find_element_by_id("kontoinhaber-hausnummer").clear()

        try:
            self.assertNotRegexpMatches(driver.find_element_by_id("kontoinhaber-hausnummer").get_attribute("class"),
                                        r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-hausnummer empty but not invalid")

        self.validate_element_by_id("kontoinhaber-hausnummer", u"99KontoInhaber", "valid")
        # endregion
        # region kontoinhaber-plz
        # -- PLZ INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-plz").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-plz empty but not invalid")

        self.validate_element_by_id("kontoinhaber-plz", ".", "invalid")
        self.validate_element_by_id("kontoinhaber-plz", "1", "invalid")
        self.validate_element_by_id("kontoinhaber-plz", "12345", "valid")
        self.validate_element_by_id("kontoinhaber-plz", "123456", "invalid")
        self.validate_element_by_id("kontoinhaber-plz", "1234a", "invalid")
        self.validate_element_by_id("kontoinhaber-plz", "a", "invalid")
        self.validate_element_by_id("kontoinhaber-plz", u"bü", "invalid")
        driver.find_element_by_id("kontoinhaber-plz").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-plz").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-plz empty but not invalid")

        self.validate_element_by_id("kontoinhaber-plz", "45612", "valid")
        # endregion
        # region kontoinhaber-ort
        # -- Ort INVALID
        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-ort").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-ort empty but not invalid")

        self.validate_element_by_id("kontoinhaber-ort", ".", "valid")
        self.validate_element_by_id("kontoinhaber-ort", "1", "valid")
        self.validate_element_by_id("kontoinhaber-ort", "a", "valid")
        self.validate_element_by_id("kontoinhaber-ort", u"bü", "valid")
        driver.find_element_by_id("kontoinhaber-ort").clear()

        try:
            self.assertRegexpMatches(driver.find_element_by_id("kontoinhaber-ort").get_attribute("class"),
                                     r"ng-invalid")
        except AssertionError as e:
            self.verificationErrors.append("Required field kontoinhaber-ort empty but not invalid")

        self.validate_element_by_id("kontoinhaber-ort", u"TESTortKontoInhaber", "valid")

        self.antragsteller_fill_data_vorversicherung("nein")

        self.antragsteller_weiter_zusatzdaten()

    def tearDown(self):
        self.driver.quit()
        # print self.verificationErrors
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
